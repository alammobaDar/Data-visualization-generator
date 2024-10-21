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

    def create_plot(self, x, title, kind, y=""):
        if kind == "Plot":
            self.figure.clear()
            plt.figure()
            plt.plot(x, y)
            plt.title(title)
            plt.xticks(rotation=90)
            plt.grid(True)
            plt.show()

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



