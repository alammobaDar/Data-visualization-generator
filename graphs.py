import sys
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class Matplotlib:
    def __init__(self, frame):
        self.frame = frame
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.frame)

        frame.layout().addWidget(self.toolbar)
        frame.layout().addWidget(self.canvas)

    def create_plot(self, x, title, kind, y=""):
        if kind == "Plot":
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x, y)
            ax.set_title(title)
            ax.tick_params(axis='x', rotation=90)
            ax.grid(True)
            self.canvas.draw()

        elif kind == "Hist":
            plt.figure()
            plt.hist(x, bins=5, color='skyblue', edgecolor='black')
            plt.title('Histogram')
            plt.xlabel('Values')
            plt.ylabel('Frequency')
            plt.xticks(rotation=90)
            plt.show()

        elif kind == "Scatter":
            plt.figure()
            plt.scatter(x, y, color='red', marker='o')
            plt.title('Scatter Plot')
            plt.xlabel('X Axis')
            plt.ylabel('Y Axis')
            plt.grid(True)
            plt.show()

        elif kind == "Bar":
            plt.figure()
            plt.bar(y, x, color='green')
            plt.title('Bar Plot')
            plt.xlabel('Categories')
            plt.ylabel('Values')
            plt.xticks(rotation=90)
            plt.show()

        elif kind == "Pie":
            plt.figure()
            plt.pie(x, labels=y, autopct='%1.1f%%', startangle=90)
            plt.title('Pie Chart')
            plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.
            plt.show()

    def get_figure(self):
        return self.canvas

    def get_toolbar(self):
        return self.toolbar

