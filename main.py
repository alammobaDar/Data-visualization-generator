import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFrame, \
    QComboBox, QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt

import kind_of_plots
from kind_of_plots import x, y, _title
from Table import upload, show_df
from graphs import create_plot

class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matplotlib Generator")
        self.setGeometry(100, 100, 1200, 700)

        # Main widget to hold all layouts and widgets
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Title bar section
        self.title_bar = QFrame(self)
        self.title_bar.setFixedHeight(100)
        self.title_bar.setStyleSheet("background-color: green;")
        title_layout = QVBoxLayout(self.title_bar)
        self._title = QLabel("Data Visualization Tool", self)
        self._title.setAlignment(Qt.AlignCenter)
        self._title.setStyleSheet("font-size: 25px; font-weight: bold; color: white;")
        title_layout.addWidget(self._title)
        main_layout.addWidget(self.title_bar)

        # Main content section with dashboard and plot area
        content_layout = QHBoxLayout()
        main_layout.addLayout(content_layout)

        # Dashboard (left panel)
        self.dashboard = QFrame(self)
        self.dashboard.setStyleSheet("background-color: cyan;")
        self.dashboard.setFixedWidth(450)
        dashboard_layout = QGridLayout(self.dashboard)
        content_layout.addWidget(self.dashboard)

        # Main section (right panel)
        self.main_section = QFrame(self)
        self.main_section.setStyleSheet("background-color: red;")
        content_layout.addWidget(self.main_section)
        main_section_layout = QVBoxLayout(self.main_section)

        # Upload Frame
        self.upload_frame = QFrame(self.main_section)
        upload_layout = QVBoxLayout(self.upload_frame)
        self.upload_label = QLabel("Please upload your Excel file or CSV file", self)
        self.upload_button = QPushButton("Upload", self)
        self.upload_button.clicked.connect(self.load_and_display_data)

        upload_layout.addWidget(self.upload_label, alignment=Qt.AlignCenter)
        upload_layout.addWidget(self.upload_button, alignment=Qt.AlignCenter)
        main_section_layout.addWidget(self.upload_frame, alignment=Qt.AlignCenter)

        # ComboBox for selecting plot type

        self.combo_box_frame = QFrame(self.dashboard)
        combo_box_frame_layout = QVBoxLayout(self.combo_box_frame)
        self.select_label = QLabel("Please choose what kind of plot you want to use", self)
        self.selected_plot = QComboBox(self)
        self.selected_plot.addItems(["Plot", "Hist", "Scatter", "Bar", "Pie"])
        self.selected_plot.currentIndexChanged.connect(self.on_combo_box)


        combo_box_frame_layout.addWidget(self.select_label, alignment=Qt.AlignCenter | Qt.AlignTop)
        combo_box_frame_layout.addWidget(self.selected_plot, alignment=Qt.AlignCenter | Qt.AlignTop)
        dashboard_layout.addWidget(self.combo_box_frame, 0, 0, 1, 10, alignment=Qt.AlignCenter | Qt.AlignTop)

        # Creating instances of plots
        self.pl = kind_of_plots
        self.plot_instance = self.pl.Plot(self.dashboard)
        self.hist_instance = self.pl.Hist(self.dashboard)
        self.bar_instance = self.pl.Bar(self.dashboard)
        self.pie_instance = self.pl.Pie(self.dashboard)
        self.scatter_instance = self.pl.Scatter(self.dashboard)

        self.erase_frame()

    def erase_frame(self):
        # Clear plot frames when switching between plot types
        self.plot_instance.plot_frame.setVisible(False)
        self.hist_instance.hist_frame.setVisible(False)
        self.scatter_instance.scatter_frame.setVisible(False)
        self.bar_instance.bar_frame.setVisible(False)
        self.pie_instance.pie_frame.setVisible(False)

    def on_combo_box(self):
        selected_value = self.selected_plot.currentText()
        self.erase_frame()

        # Show the selected plot's frame
        if selected_value == "Plot":
            self.plot_instance.plot_frame.setVisible(True)
        elif selected_value == "Hist":
            self.hist_instance.hist_frame.setVisible(True)
        elif selected_value == "Scatter":
            self.scatter_instance.scatter_frame.setVisible(True)
        elif selected_value == "Bar":
            self.bar_instance.bar_frame.setVisible(True)
        elif selected_value == "Pie":
            self.pie_instance.pie_frame.setVisible(True)

    def load_and_display_data(self):
        df = upload()
        if df is not None:
            self.upload_frame.setVisible(False)
            show_df(df, self.main_section)

    def display_plot(self):
        create_plot(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())
