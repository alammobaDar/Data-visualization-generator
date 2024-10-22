import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from PyQt5 import sip
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class Matplotlib:
    def __init__(self, frame):
        self.frame = frame
        self.init_plot()


    def init_plot(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.frame)

        self.frame.layout().addWidget(self.toolbar)
        self.frame.layout().addWidget(self.canvas)

    def clear_plot(self):
        self.frame.layout().count()

    def create_plot(self, x, title, kind, y=""):
        self.figure.clear()
        self.ax = self.figure.add_subplot(111)

        if kind == "Plot":
            self.ax.plot(x, y)
            self.ax.set_title(title)
            self.ax.tick_params(axis='x', rotation=90)
            self.ax.grid(True)


        elif kind == "Hist":
            self.ax.hist(x, bins=5, color='skyblue', edgecolor='black')
            self.ax.set_title('Histogram')
            self.ax.set_xlabel('Values')
            self.ax.set_ylabel('Frequency')
            self.ax.tick_params(axis='x', rotation=90)

        elif kind == "Scatter":
            self.ax.scatter(x, y, color='red', marker='o')
            self. ax.set_title('Scatter Plot')
            self.ax.set_xlabel('X Axis')
            self.ax.set_ylabel('Y Axis')
            self. ax.grid(True)

        elif kind == "Bar":
            self.ax.bar(y, x, color='green')
            self.ax.set_title('Bar Plot')
            self.ax.set_xlabel('Categories')
            self. ax.set_ylabel('Values')
            self. ax.tick_params(axis='x', rotation=90)

        elif kind == "Pie":
            self.figure.clear()
            self.ax.pie(x, labels=y, autopct='%1.1f%%', startangle=90)
            self.ax.set_title('Pie Chart')
            self.ax.set_aspect('equal', adjustable='box')

        self.canvas.draw()
