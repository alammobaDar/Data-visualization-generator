import sys

from PyQt5.QtCore import Qt, QFile, QTextStream
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMainWindow, QFileDialog, \
    QFrame, QScrollBar, QTableWidget, QTableWidgetItem, QWidget, QHeaderView, QAbstractScrollArea, QScrollArea
import pandas as pd

class Table:
    
    def __init__(self):
        self.file_name = None
        self.table = None
        self.tableFrame = None

    def upload(self):
        self.file_name, _ = QFileDialog.getOpenFileName(None, "Open file", "",
                                                   "CSV files (*.csv);;Excel files (*.xlsx, *.xls)")
    
        self.df = None
        if self.file_name:
            if self.file_name.endswith(".xlsx") or self.file_name.endswith(".xls"):
                self.df = pd.read_excel(self.file_name)
            elif self.file_name.endswith(".csv"):
                self.df = pd.read_csv(self.file_name)
    
        return self.df
    
    
    def show_df(self, df):
    
        self.columns = list(df.columns)
        num_rows = df.shape[0]

        self.tableFrame = QFrame()
        table_layout = QVBoxLayout(self.tableFrame)
        self.tableFrame.setContentsMargins(0,0,0,0)


        # Create a QTableWidget
        self.table = QTableWidget(self.tableFrame)
        self.table.setRowCount(num_rows)
        self.table.setColumnCount(len(self.columns))
        self.table.setHorizontalHeaderLabels(self.columns)
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table.setFixedHeight(300)
        self.table.setFixedWidth(750)
        self.table.setObjectName("table")
    
        # Insert DataFrame values into the table
        for i in range(num_rows):
            for j in range(len(self.columns)):
                self.table.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))
    
        # Set stretch and scrollbar
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        table_layout.addWidget(self.table)

    def get_value(self, x, kind, y=""):
        try:
            if kind == "Hist":
                print(self.df[x])
                print(kind)
            else:
                print(self.df[x])
                print(self.df[y])
                print(kind)
        except KeyError:
            print("there's no such column")


    def get_frame(self):
        return self.tableFrame

