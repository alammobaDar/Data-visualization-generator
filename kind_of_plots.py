import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QWidget, \
    QGridLayout, QMainWindow, QSizePolicy

x = None
y = None
_title = None



def title(frame):
    optional_label = QLabel("Optional", frame)
    optional_label.setStyleSheet("font-size: 30px; font-style: italic; background-color: white;")
    frame.layout().addWidget(optional_label, 5, 0)

    global _title
    title_label = QLabel("Title:", frame)
    title_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: white;")
    frame.layout().addWidget(title_label, 6, 0)

    _title = QLineEdit(frame)
    _title.setFixedSize(100,30)
    _title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
    frame.layout().addWidget(_title, 6, 2)

def required_part(frame, type_):
    global x, y

    required_label = QLabel("Required", frame)
    required_label.setStyleSheet("font-size: 30px; font-style: italic; background-color: white;")
    frame.layout().addWidget(required_label, 2, 0)



    if type_ != "bar":
        x_label = QLabel("X-axis:", frame)
        x_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: white;")
        frame.layout().addWidget(x_label, 3, 0)

        x = QLineEdit(frame)
        x.setFixedSize(100,30)
        x.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        frame.layout().addWidget(x, 3, 2)

    if type_ != "hist" and type_ != "bar":
        y_label = QLabel("Y-axis:", frame)
        y_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: white;")
        frame.layout().addWidget(y_label, 4, 0)

        y = QLineEdit(frame)
        y.setFixedSize(100, 30)
        y.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        frame.layout().addWidget(y, 4, 2)

class Plot:
    def __init__(self, window):
        self.window = window
        self.plot_frame = QFrame(self.window)
        self.plot_frame.setStyleSheet("background-color: white; padding: 0px; margin: 0px")
        layout = QGridLayout(self.plot_frame)
        self.plot_frame.setLayout(layout)

        required_part(self.plot_frame, "plot")

        title(self.plot_frame)

        self.x_label_label = QLabel("xlabel:", self.plot_frame)
        self.x_label_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: white;")
        layout.addWidget(self.x_label_label, 7, 0)

        self.x_label = QLineEdit(self.plot_frame)
        self.x_label.setFixedSize(100, 30)
        self.x_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.x_label, 7, 2)

        self.y_label_label = QLabel("ylabel:", self.plot_frame)
        self.y_label_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: white;")
        layout.addWidget(self.y_label_label, 8, 0)

        self.y_label = QLineEdit(self.plot_frame)
        self.y_label.setFixedSize(100, 30)
        self.y_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.y_label, 8, 2)

        self.submit = QPushButton("Submit", self.plot_frame)
        self.submit.setFixedSize(100, 30)
        self.submit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.submit, 9, 9)

    def get_frame(self):
        return self.plot_frame


class Hist:
    def __init__(self, window):
        self.window = window
        self.hist_frame = QFrame(self.window)
        self.hist_frame.setStyleSheet("background-color: white; padding: 0px; margin: 0px")
        layout = QGridLayout(self.hist_frame)
        self.hist_frame.setLayout(layout)

        required_part(self.hist_frame, "hist")

        title(self.hist_frame)

        self.x_label_label = QLabel("xlabel:", self.hist_frame)
        self.x_label_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: white;")
        layout.addWidget(self.x_label_label, 7, 0)

        self.x_label = QLineEdit(self.hist_frame)
        self.x_label.setFixedSize(100, 30)
        self.x_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.x_label, 7, 2)

        self.y_label_label = QLabel("ylabel:", self.hist_frame)
        self.y_label_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: white;")
        layout.addWidget(self.y_label_label, 8, 0)

        self.y_label = QLineEdit(self.hist_frame)
        self.y_label.setFixedSize(100, 30)
        self.y_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.y_label, 8, 2)

        self.submit = QPushButton("Submit", self.hist_frame)
        self.submit.setFixedSize(100, 30)
        self.submit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.submit, 9, 9)

    def get_frame(self):
        return self.hist_frame

class Scatter:
    def __init__(self, window):
        self.window = window
        self.scatter_frame = QFrame(self.window)
        self.scatter_frame.setStyleSheet("background-color: white; padding: 0px; margin: 0px")
        layout = QGridLayout(self.scatter_frame)
        self.scatter_frame.setLayout(layout)

        required_part(self.scatter_frame, "scatter")

        title(self.scatter_frame)

        self.x_label_label = QLabel("xlabel:", self.scatter_frame)
        self.x_label_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: white;")
        layout.addWidget(self.x_label_label, 7, 0)

        self.x_label = QLineEdit(self.scatter_frame)
        self.x_label.setFixedSize(100, 30)
        self.x_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.x_label, 7, 2)

        self.y_label_label = QLabel("ylabel:", self.scatter_frame)
        self.y_label_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: white;")
        layout.addWidget(self.y_label_label, 8, 0)

        self.y_label = QLineEdit(self.scatter_frame)
        self.y_label.setFixedSize(100, 30)
        self.y_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.y_label, 8, 2)

        self.submit = QPushButton("Submit", self.scatter_frame)
        self.submit.setFixedSize(100, 30)
        self.submit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.submit, 9, 9)

    def get_frame(self):
        return self.scatter_frame

class Bar:
    def __init__(self, window):
        self.window = window
        self.bar_frame = QFrame(self.window)
        self.bar_frame.setStyleSheet("background-color: white; padding: 0px; margin: 0px")
        layout = QGridLayout(self.bar_frame)
        self.bar_frame.setLayout(layout)

        required_part(self.bar_frame, "bar")

        self.values_label = QLabel("Values:", self.bar_frame)
        self.values_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: white;")
        layout.addWidget(self.values_label, 3, 0)

        self.values = QLineEdit(self.bar_frame)
        self.values.setFixedSize(100, 30)
        self.values.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.values, 3, 2)

        self.category_label = QLabel("Categories:", self.bar_frame)
        self.category_label.setStyleSheet("font-size: 10px; font-weight: bold; background-color: white;")
        layout.addWidget(self.category_label, 4, 0)

        self.category = QLineEdit(self.bar_frame)
        self.category.setFixedSize(100, 30)
        self.category.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.category, 4, 2)

        title(self.bar_frame)

        self.submit = QPushButton("Submit", self.bar_frame)
        self.submit.setFixedSize(100, 30)
        self.submit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.submit, 7, 9)

    def get_frame(self):
        return self.bar_frame

class Pie:
    def __init__(self, window):
        self.window = window
        self.pie_frame = QFrame(self.window)
        self.pie_frame.setStyleSheet("background-color: white; padding: 0px; margin: 0px")
        layout = QGridLayout(self.pie_frame)
        self.pie_frame.setLayout(layout)

        required_part(self.pie_frame, "pie")

        title(self.pie_frame)

        self.submit = QPushButton("Submit", self.pie_frame)
        self.submit.setFixedSize(100, 30)
        self.submit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.submit, 7, 9)

    def get_frame(self):
        return self.pie_frame