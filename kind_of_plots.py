import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QWidget, QGridLayout, QMainWindow

x = None
y = None
_title = None

def title(frame):
    global _title
    title_label = QLabel("Title:", frame)
    title_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: cyan;")
    frame.layout().addWidget(title_label, 6, 0)

    _title = QLineEdit(frame)
    frame.layout().addWidget(_title, 6, 2)

def required_part(frame, type_):
    global x, y

    required_label = QLabel("Required", frame)
    required_label.setStyleSheet("font-size: 30px; font-style: italic; background-color: cyan;")
    frame.layout().addWidget(required_label, 2, 0)

    if type_ != "bar":
        x_label = QLabel("X-axis:", frame)
        x_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: cyan;")
        frame.layout().addWidget(x_label, 3, 0)

        x = QLineEdit(frame)
        frame.layout().addWidget(x, 3, 2)

    if type_ != "hist" and type_ != "bar":
        y_label = QLabel("Y-axis:", frame)
        y_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: cyan;")
        frame.layout().addWidget(y_label, 4, 0)

        y = QLineEdit(frame)
        frame.layout().addWidget(y, 4, 2)

class Plot:
    def __init__(self, window):
        self.window = window
        self.plot_frame = QFrame(self.window)
        self.plot_frame.setStyleSheet("background-color: cyan; height: 400px;")
        layout = QGridLayout(self.plot_frame)
        self.plot_frame.setLayout(layout)

        required_part(self.plot_frame, "plot")

        self.optional_label = QLabel("Optional", self.plot_frame)
        self.optional_label.setStyleSheet("font-size: 30px; font-style: italic; background-color: cyan;")
        layout.addWidget(self.optional_label, 5, 0)

        title(self.plot_frame)

        self.x_label_label = QLabel("xlabel:", self.plot_frame)
        self.x_label_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: cyan;")
        layout.addWidget(self.x_label_label, 7, 0)

        self.x_label = QLineEdit(self.plot_frame)
        layout.addWidget(self.x_label, 7, 2)

        self.y_label_label = QLabel("ylabel:", self.plot_frame)
        self.y_label_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: cyan;")
        layout.addWidget(self.y_label_label, 8, 0)

        self.y_label = QLineEdit(self.plot_frame)
        layout.addWidget(self.y_label, 8, 2)

        self.submit = QPushButton("Submit", self.plot_frame)
        layout.addWidget(self.submit, 9, 9)

class Hist:
    def __init__(self, window):
        self.window = window
        self.hist_frame = QFrame(self.window)
        self.hist_frame.setStyleSheet("background-color: cyan; height: 400px;")
        layout = QGridLayout(self.hist_frame)
        self.hist_frame.setLayout(layout)

        required_part(self.hist_frame, "hist")

        self.optional_label = QLabel("Optional", self.hist_frame)
        self.optional_label.setStyleSheet("font-size: 30px; font-style: italic; background-color: cyan;")
        layout.addWidget(self.optional_label, 5, 0)

        title(self.hist_frame)

        self.x_label_label = QLabel("xlabel:", self.hist_frame)
        self.x_label_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: cyan;")
        layout.addWidget(self.x_label_label, 7, 0)

        self.x_label = QLineEdit(self.hist_frame)
        layout.addWidget(self.x_label, 7, 2)

        self.y_label_label = QLabel("ylabel:", self.hist_frame)
        self.y_label_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: cyan;")
        layout.addWidget(self.y_label_label, 8, 0)

        self.y_label = QLineEdit(self.hist_frame)
        layout.addWidget(self.y_label, 8, 2)

        self.submit = QPushButton("Submit", self.hist_frame)
        layout.addWidget(self.submit, 9, 9)

class Scatter:
    def __init__(self, window):
        self.window = window
        self.scatter_frame = QFrame(self.window)
        self.scatter_frame.setStyleSheet("background-color: cyan; height: 400px;")
        layout = QGridLayout(self.scatter_frame)
        self.scatter_frame.setLayout(layout)

        required_part(self.scatter_frame, "scatter")

        self.optional_label = QLabel("Optional", self.scatter_frame)
        self.optional_label.setStyleSheet("font-size: 30px; font-style: italic; background-color: cyan;")
        layout.addWidget(self.optional_label, 5, 0)

        title(self.scatter_frame)

        self.x_label_label = QLabel("xlabel:", self.scatter_frame)
        self.x_label_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: cyan;")
        layout.addWidget(self.x_label_label, 7, 0)

        self.x_label = QLineEdit(self.scatter_frame)
        layout.addWidget(self.x_label, 7, 2)

        self.y_label_label = QLabel("ylabel:", self.scatter_frame)
        self.y_label_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: cyan;")
        layout.addWidget(self.y_label_label, 8, 0)

        self.y_label = QLineEdit(self.scatter_frame)
        layout.addWidget(self.y_label, 8, 2)

        self.submit = QPushButton("Submit", self.scatter_frame)
        layout.addWidget(self.submit, 9, 9)

class Bar:
    def __init__(self, window):
        self.window = window
        self.bar_frame = QFrame(self.window)
        self.bar_frame.setStyleSheet("background-color: cyan; height: 400px;")
        layout = QGridLayout(self.bar_frame)
        self.bar_frame.setLayout(layout)

        required_part(self.bar_frame, "bar")

        self.values_label = QLabel("Values:", self.bar_frame)
        self.values_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: cyan;")
        layout.addWidget(self.values_label, 3, 0)

        self.values = QLineEdit(self.bar_frame)
        layout.addWidget(self.values, 3, 2)

        self.category_label = QLabel("Categories:", self.bar_frame)
        self.category_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: cyan;")
        layout.addWidget(self.category_label, 4, 0)

        self.category = QLineEdit(self.bar_frame)
        layout.addWidget(self.category, 4, 3)

        self.optional_label = QLabel("Optional", self.bar_frame)
        self.optional_label.setStyleSheet("font-size: 30px; font-style: italic; background-color: cyan;")
        layout.addWidget(self.optional_label, 5, 0)

        title(self.bar_frame)

        self.submit = QPushButton("Submit", self.bar_frame)
        layout.addWidget(self.submit, 7, 9)

class Pie:
    def __init__(self, window):
        self.window = window
        self.pie_frame = QFrame(self.window)
        self.pie_frame.setStyleSheet("background-color: cyan; height: 400px;")
        layout = QGridLayout(self.pie_frame)
        self.pie_frame.setLayout(layout)

        required_part(self.pie_frame, "pie")

        self.optional_label = QLabel("Optional", self.pie_frame)
        self.optional_label.setStyleSheet("font-size: 30px; font-style: italic; background-color: cyan;")
        layout.addWidget(self.optional_label, 5, 0)

        title(self.pie_frame)

        self.submit = QPushButton("Submit", self.pie_frame)
        layout.addWidget(self.submit, 7, 9)