import sys

from PyQt5.QtGui import QColor, QFontDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QFrame, \
    QComboBox, QGridLayout, QSizePolicy, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QFile, QTextStream

import kind_of_plots
from Table import Table
from Table import Table


class UI(QMainWindow):
    def __init__(self):
        super().__init__()


        # Create drop self.shadow effect
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(10)
        self.shadow.setOffset(3, 3)
        self.shadow.setColor(QColor(0, 0, 0, 150))

        # Load some fonts
        QFontDatabase.addApplicationFont(".Poppins/Poppins-Regular.ttf")
        QFontDatabase.addApplicationFont(".Poppins/Poppins-Bold.ttf")


        #Setting up the main window
        self.setWindowTitle("Matplotlib Generator")
        self.setGeometry(100, 100, 1200, 800)

        # Main widget to hold all layouts and widgets
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setObjectName("central_widget")
        main_layout = QVBoxLayout(central_widget)

        # Title bar section
        self.title_bar = QFrame(self)
        self.title_bar.setFixedHeight(100)
        self.title_bar.setObjectName("title_bar")
        title_layout = QVBoxLayout(self.title_bar)
        self._title = QLabel("Data Visualization Tool", self)
        self._title.setAlignment(Qt.AlignCenter)
        self._title.setProperty("class", "title")
        title_layout.addWidget(self._title)
        main_layout.addWidget(self.title_bar)

        # Main content section with dashboard and plot area
        content_layout = QHBoxLayout()
        main_layout.addLayout(content_layout)

        # Dashboard (left panel)
        self.dashboard = QFrame(self)
        self.dashboard.setObjectName("dashboard")
        self.dashboard.setFixedWidth(450)
        dashboard_layout = QVBoxLayout(self.dashboard)
        content_layout.addWidget(self.dashboard)

        # Main section (right panel)
        self.main_section = QFrame(self)
        self.main_section.setObjectName("main_section")
        content_layout.addWidget(self.main_section)
        self.main_section_layout = QVBoxLayout(self.main_section)

        # Upload Frame
        self.upload_frame = QFrame(self.main_section)
        upload_layout = QVBoxLayout(self.upload_frame)
        self.upload_label = QLabel("Please upload your Excel file or CSV file", self)
        self.upload_label.setProperty("class", "font_color")
        self.upload_button = QPushButton("Upload", self)
        self.upload_button.clicked.connect(self.load_and_display_data)

        upload_layout.addWidget(self.upload_label, alignment=Qt.AlignCenter)
        upload_layout.addWidget(self.upload_button, alignment=Qt.AlignCenter)
        self.main_section_layout.addWidget(self.upload_frame, alignment=Qt.AlignCenter)

        # ComboBox for selecting plot type
        self.combo_box_frame = QFrame()
        combo_box_frame_layout = QVBoxLayout(self.combo_box_frame)
        self.combo_box_frame.setProperty("class", "frame")
        self.combo_box_frame.setGraphicsEffect(self.shadow)

        self.select_label = QLabel("Please choose what kind of plot you want to use", self)
        self.select_label.setProperty("class", "font_color")

        self.selected_plot = QComboBox(self)
        self.selected_plot.addItems(["Plot", "Hist", "Scatter", "Bar", "Pie"])
        self.selected_plot.currentIndexChanged.connect(self.on_combo_box)
        self.selected_plot.setObjectName("selected_plot")
        self.selected_plot.setGraphicsEffect(self.shadow)


        combo_box_frame_layout.addWidget(self.select_label, alignment=Qt.AlignCenter | Qt.AlignTop)
        combo_box_frame_layout.addWidget(self.selected_plot, alignment=Qt.AlignCenter | Qt.AlignTop)

        # creating a container for the kind_of_plots to be placed
        self.plots_frame = QFrame()
        plots_frame_layout = QVBoxLayout(self.plots_frame)
        self.plots_frame.setObjectName("dashboard")

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

        self.plot_instance.get_frame().setGraphicsEffect(self.shadow)
        self.hist_instance.get_frame().setGraphicsEffect(self.shadow)
        self.scatter_instance.get_frame().setGraphicsEffect(self.shadow)
        self.bar_instance.get_frame().setGraphicsEffect(self.shadow)
        self.pie_instance.get_frame().setGraphicsEffect(self.shadow)

        self.erase_frame()


        # Add plots frame to the layout
        dashboard_layout.addWidget(self.plots_frame)
        dashboard_layout.addWidget(self.combo_box_frame, alignment=Qt.AlignTop)

        # Set stretch factors
        dashboard_layout.setStretch(0, 0)  # Combo box frame takes up 1 part
        dashboard_layout.setStretch(1, 2)  # Plots frame takes up 2 parts

        #instantiate the table class
        self.tb = Table()

        #load the stylesheet
        self.load_stylesheet()

        #load the plot button
        self.plot_instance.submit.clicked.connect(self.submit_entry)

    def load_stylesheet(self):
        file = QFile("styles.qss")
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())



    def submit_entry(self):
        pl = self.plot_instance
        self.tb.get_value(pl.x_value, pl.y_value)

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
            self.tb.get_frame().setGraphicsEffect(self.shadow)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())
