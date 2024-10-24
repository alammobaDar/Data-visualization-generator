import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QFrame, QWidget, \
    QGridLayout, QMainWindow, QSizePolicy

class All_Plots:

    def __init__(self, frame, type_):
        self.required_part(frame, type_)
        self.title(frame)
        self.submit_button(frame)

    def title(self, frame):
        optional_label = QLabel("Optional", frame)
        optional_label.setProperty("class", "title")
        frame.layout().addWidget(optional_label, 5, 0, 1, 10)

        title_label = QLabel("Title:", frame)
        title_label.setProperty("class", "font_color")
        frame.layout().addWidget(title_label, 6, 0)

        self._title = QLineEdit(frame)
        self._title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        frame.layout().addWidget(self._title, 6, 2)

    def required_part(self, frame, type_):

        required_label = QLabel("Required", frame)
        required_label.setProperty("class", "title")
        frame.layout().addWidget(required_label, 2, 0, 1, 10)

        if type_ != "bar":
            x_axis_label = QLabel("X-axis:", frame)
            x_axis_label.setProperty("class", "font_color")
            frame.layout().addWidget(x_axis_label, 3, 0)

            self.x = QLineEdit(frame)
            self.x.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            frame.layout().addWidget(self.x, 3, 2)

        if type_ != "hist" and type_ != "bar":
            y_label = QLabel("Y-axis:", frame)
            y_label.setProperty("class", "font_color")
            frame.layout().addWidget(y_label, 4, 0)

            self.y = QLineEdit(frame)
            self.y.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            frame.layout().addWidget(self.y, 4, 2)

    def labels(self, frame):
        self.x_label_label = QLabel("X-label:", frame)
        self.x_label_label.setProperty("class", "font_color")
        frame.layout().addWidget(self.x_label_label, 7, 0)

        self.x_label = QLineEdit(frame)
        self.x_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        frame.layout().addWidget(self.x_label, 7, 2)

        self.y_label_label = QLabel("Y-label:", frame)
        self.y_label_label.setProperty("class", "font_color")
        frame.layout().addWidget(self.y_label_label, 8, 0)

        self.y_label = QLineEdit(frame)
        self.y_label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        frame.layout().addWidget(self.y_label, 8, 2)

    def submit_button(self, frame):
        self.submit = QPushButton("Submit", frame)
        self.submit.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        frame.layout().addWidget(self.submit, 9, 9)


class Plot(All_Plots):

    def __init__(self, window):

        self.window = window
        self.plot_frame = QFrame(self.window)
        self.plot_frame.setProperty("class", "frame")
        layout = QGridLayout(self.plot_frame)
        self.plot_frame.setLayout(layout)

        super().__init__(self.plot_frame, "plot")
        self.labels(self.plot_frame)

        self.x.textEdited.connect(self.text_changed)
        self.y.textEdited.connect(self.text_changed)
        self._title.textEdited.connect(self.text_changed)
        self.x_label.textEdited.connect(self.text_changed)
        self.y_label.textEdited.connect(self.text_changed)

    def text_changed(self):
        self.x_value = self.x.text()
        self.y_value = self.y.text()
        self.title_value = self._title.text()
        self.y_label_value = self.y_label.text()
        self.x_label_value = self.x_label.text()

    def get_frame(self):
        return self.plot_frame

class Hist(All_Plots):
    def __init__(self, window):
        self.window = window
        self.hist_frame = QFrame(self.window)
        self.hist_frame.setProperty("class", "frame")
        layout = QGridLayout(self.hist_frame)
        self.hist_frame.setLayout(layout)

        super().__init__(self.hist_frame, "hist")
        self.labels(self.hist_frame)

        self.x.textEdited.connect(self.text_changed)
        self._title.textEdited.connect(self.text_changed)
        self.x_label.textEdited.connect(self.text_changed)
        self.y_label.textEdited.connect(self.text_changed)

    def text_changed(self):
        self.x_value = self.x.text()
        self.title_value = self._title.text()
        self.y_label_value = self.y_label.text()
        self.x_label_value = self.x_label.text()

    def get_frame(self):
        return self.hist_frame

class Scatter(All_Plots):
    def __init__(self, window):
        self.window = window
        self.scatter_frame = QFrame(self.window)
        self.scatter_frame.setProperty("class", "frame")
        layout = QGridLayout(self.scatter_frame)
        self.scatter_frame.setLayout(layout)

        super().__init__(self.scatter_frame, "scatter")

        self.labels(self.scatter_frame)

        self.x.textEdited.connect(self.text_changed)
        self.y.textEdited.connect(self.text_changed)
        self._title.textEdited.connect(self.text_changed)
        self.x_label.textEdited.connect(self.text_changed)
        self.y_label.textEdited.connect(self.text_changed)

    def text_changed(self):
        self.x_value = self.x.text()
        self.y_value = self.y.text()
        self.title_value = self._title.text()
        self.y_label_value = self.y_label.text()
        self.x_label_value = self.x_label.text()

    def get_frame(self):
        return self.scatter_frame

class Bar(All_Plots):
    def __init__(self, window):

        self.window = window
        self.bar_frame = QFrame(self.window)
        self.bar_frame.setProperty("class", "frame")
        layout = QGridLayout(self.bar_frame)
        self.bar_frame.setLayout(layout)

        super().__init__(self.bar_frame, "bar")

        self.values_label = QLabel("Values:", self.bar_frame)
        self.values_label.setProperty("class", "font_color")
        layout.addWidget(self.values_label, 3, 0)

        self.values = QLineEdit(self.bar_frame)
        self.values.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.values, 3, 2)

        self.category_label = QLabel("Categories:", self.bar_frame)
        self.category_label.setProperty("class", "font_color")
        layout.addWidget(self.category_label, 4, 0)

        self.category = QLineEdit(self.bar_frame)
        self.category.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.addWidget(self.category, 4, 2)



        self.values.textEdited.connect(self.text_changed)
        self.category.textEdited.connect(self.text_changed)
        self._title.textEdited.connect(self.text_changed)
        self.x_label.textEdited.connect(self.text_changed)
        self.y_label.textEdited.connect(self.text_changed)

    def text_changed(self):
        self.values_value = self.values.text()
        self.category_value = self.category.text()
        self.title_value = self._title.text()
        self.y_label_value = self.y_label.text()
        self.x_label_value = self.x_label.text()

    def get_frame(self):
        return self.bar_frame

class Pie(All_Plots):
    def __init__(self, window):

        self.window = window
        self.pie_frame = QFrame(self.window)
        self.pie_frame.setProperty("class", "frame")
        layout = QGridLayout(self.pie_frame)
        self.pie_frame.setLayout(layout)

        super().__init__(self.pie_frame, "pie")

        self.x.textEdited.connect(self.text_changed)
        self.y.textEdited.connect(self.text_changed)
        self._title.textEdited.connect(self.text_changed)

    def text_changed(self):
        self.x_value = self.x.text()
        self.y_value = self.y.text()
        self.title_value = self._title.text()

    def get_frame(self):
        return self.pie_frame