import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFrame, \
    QComboBox, QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt

import kind_of_plots
from Table import Table
from kind_of_plots import x, y, _title
from Table import Table
from graphs import create_plot

class UI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matplotlib Generator")
        self.setGeometry(100, 100, 1200, 900)

        # Main widget to hold all layouts and widgets
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Title bar section
        self.title_bar = QFrame(self)
        self.title_bar.setFixedHeight(100)
        self.title_bar.setStyleSheet("background-color: gray;")
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
        self.dashboard.setStyleSheet("background-color: gray;")
        self.dashboard.setFixedWidth(450)
        dashboard_layout = QVBoxLayout(self.dashboard)
        content_layout.addWidget(self.dashboard)

        # Main section (right panel)
        self.main_section = QFrame(self)
        self.main_section.setStyleSheet("background-color: white;")
        content_layout.addWidget(self.main_section)
        self.main_section_layout = QVBoxLayout(self.main_section)

        # Upload Frame
        self.upload_frame = QFrame(self.main_section)
        upload_layout = QVBoxLayout(self.upload_frame)
        self.upload_label = QLabel("Please upload your Excel file or CSV file", self)
        self.upload_button = QPushButton("Upload", self)
        self.upload_button.clicked.connect(self.load_and_display_data)

        upload_layout.addWidget(self.upload_label, alignment=Qt.AlignCenter)
        upload_layout.addWidget(self.upload_button, alignment=Qt.AlignCenter)
        self.main_section_layout.addWidget(self.upload_frame, alignment=Qt.AlignCenter)

        # ComboBox for selecting plot type
        self.combo_box_frame = QFrame()
        combo_box_frame_layout = QVBoxLayout(self.combo_box_frame)
        self.combo_box_frame.setStyleSheet("background-color: gray; padding: 0px; margin: 0px")
        self.select_label = QLabel("Please choose what kind of plot you want to use", self)
        self.selected_plot = QComboBox(self)
        self.selected_plot.addItems(["Plot", "Hist", "Scatter", "Bar", "Pie"])
        self.selected_plot.currentIndexChanged.connect(self.on_combo_box)

        combo_box_frame_layout.addWidget(self.select_label, alignment=Qt.AlignCenter | Qt.AlignTop)
        combo_box_frame_layout.addWidget(self.selected_plot, alignment=Qt.AlignCenter | Qt.AlignTop)

        # creating a container for the kind_of_plots to be placed
        self.plots_frame = QFrame()
        plots_frame_layout = QVBoxLayout(self.plots_frame)
        self.plots_frame.setStyleSheet("background-color: gray; padding: 0px; margin: 0px")

        # Creating instances of plots
        self.pl = kind_of_plots
        self.plot_instance = self.pl.Plot(self.plots_frame)
        self.hist_instance = self.pl.Hist(self.plots_frame)
        self.bar_instance = self.pl.Bar(self.plots_frame)
        self.pie_instance = self.pl.Pie(self.plots_frame)
        self.scatter_instance = self.pl.Scatter(self.plots_frame)

        plots_frame_layout.addWidget(self.plot_instance.get_frame(), alignment=Qt.AlignTop)
        plots_frame_layout.addWidget(self.hist_instance.get_frame(),  alignment=Qt.AlignTop)
        plots_frame_layout.addWidget(self.scatter_instance.get_frame(), alignment=Qt.AlignTop)
        plots_frame_layout.addWidget(self.bar_instance.get_frame(), alignment=Qt.AlignTop)
        plots_frame_layout.addWidget(self.pie_instance.get_frame(), alignment=Qt.AlignTop)

        self.erase_frame()

        # Add plots frame to the layout
        dashboard_layout.addWidget(self.plots_frame)
        dashboard_layout.addWidget(self.combo_box_frame, alignment=Qt.AlignTop)

        # Set stretch factors
        dashboard_layout.setStretch(0, 0)  # Combo box frame takes up 1 part
        dashboard_layout.setStretch(1, 2)  # Plots frame takes up 2 parts

        #instantiate the table class
        self.tb = Table()
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
        df = self.tb.upload()
        if df is not None:
            self.upload_frame.setVisible(False)
            self.tb.show_df(df)
            self.main_section_layout.addWidget(self.tb.get_frame(), alignment=Qt.AlignTop | Qt.AlignCenter)

    def display_plot(self):
        create_plot(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())
