import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMainWindow, QFileDialog, \
    QFrame, QScrollBar, QTableWidget, QTableWidgetItem, QWidget, QHeaderView
import pandas as pd


def upload():
    file_name, _ = QFileDialog.getOpenFileName(None, "Open file", "",
                                               "CSV files (*.csv);;Excel files (*.xlsx, *.xls)")

    df = None
    if file_name:
        if file_name.endswith(".xlsx") or file_name.endswith(".xls"):
            df = pd.read_excel(file_name)
        elif file_name.endswith(".csv"):
            df = pd.read_csv(file_name)

    return df


def show_df(df, frame):
    # Remove existing widgets from the frame if necessary
    for widget in frame.findChildren(QWidget):
        widget.deleteLater()

    columns = list(df.columns)
    num_rows = df.shape[0]

    # Create a QTableWidget
    table = QTableWidget(frame)
    table.setRowCount(num_rows)
    table.setColumnCount(len(columns))
    table.setHorizontalHeaderLabels(columns)

    # Insert DataFrame values into the table
    for i in range(num_rows):
        for j in range(len(columns)):
            table.setItem(i, j, QTableWidgetItem(str(df.iloc[i, j])))

    # Set stretch and scrollbar
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    scroll_bar = QScrollBar()
    table.setHorizontalScrollBar(scroll_bar)

    layout = QVBoxLayout(frame)
    layout.addWidget(table)

    frame.setLayout(layout)