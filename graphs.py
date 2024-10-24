import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class Matplotlib:
    def __init__(self, frame):
        self.frame = frame

    def init_plot(self):

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.frame)
        width_inches = self.frame.width()/96
        height_inches = self.frame.height()/96

        self.figure.set_size_inches(width_inches, height_inches)

        self.frame.layout().addWidget(self.toolbar)
        self.frame.layout().addWidget(self.canvas)

    def clear_plot(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clear_plot(item.layout())

    def create_plot(self, x, kind, title='', y_label='', x_label='', y=""):
        self.clear_plot(self.frame.layout())
        self.init_plot()
        self.ax = self.figure.add_subplot(111)

        if kind == "Plot":
            self.ax.plot(x, y)
            self.ax.set_title(title)
            self.ax.set_xlabel(x_label)
            self.ax.set_ylabel(y_label)
            self.ax.tick_params(axis='x', rotation=90)
            self.ax.grid(True)


        elif kind == "Hist":
            self.ax.hist(x, bins=5, color='skyblue', edgecolor='black')
            self.ax.set_title(title)
            self.ax.set_xlabel(x_label)
            self.ax.set_ylabel(y_label)
            self.ax.tick_params(axis='x', rotation=90)

        elif kind == "Scatter":
            self.ax.scatter(x, y, color='red', marker='o')
            self. ax.set_title(title)
            self.ax.set_xlabel(x_label)
            self.ax.set_ylabel(y_label)
            self.ax.tick_params(axis='x', rotation=90)
            self.ax.grid(True)

        elif kind == "Bar":
            self.ax.bar(y, x, color='green')
            self.ax.set_title(title)
            self.ax.set_xlabel(x_label)
            self.ax.set_ylabel(y_label)
            self. ax.tick_params(axis='x', rotation=90)

        elif kind == "Pie":
            self.ax.pie(x, labels=y, autopct='%1.1f%%', startangle=90)
            self.ax.set_title(title)
            self.ax.set_aspect('equal', adjustable='box')

        self.canvas.draw()
