from io import StringIO
from PyQt5.QtCore import Qt, QFile, QTextStream
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QFileDialog, \
    QFrame, QTableWidget, QTableWidgetItem, QWidget, QAbstractScrollArea
import pandas as pd
from graphs import Matplotlib

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

    def get_value(self, x, kind, frame, y_label="", x_label="", title="", y=""):

        mt = Matplotlib(frame)
        if kind == "Hist":
            mt.create_plot(x=self.df[x], title=title, kind=kind, y_label=y_label, x_label= x_label)
        else:
            mt.create_plot(x= self.df[x], y= self.df[y], title=title, kind=kind, x_label=x_label, y_label=y_label)


    def get_frame(self):
        return self.tableFrame

    def get_another_window(self):
        self.info = info_window(self.df)
        self.info.show()


class info_window(QWidget):

    def __init__(self, df):
        super().__init__()
        layout = QHBoxLayout()
        self.setWindowTitle("Information")
        self.setObjectName("central_widget")

        info_frame = QFrame(self)
        info_layout = QVBoxLayout(info_frame)
        info_frame.setProperty("class", "info_frame")
        layout.addWidget(info_frame)

        median_frame = QFrame(self)
        median_layout = QVBoxLayout(median_frame)
        median_frame.setProperty("class", "info_frame")
        layout.addWidget(median_frame)

        mean_frame = QFrame(self)
        mean_layout = QVBoxLayout(mean_frame)
        mean_frame.setProperty("class", "info_frame")
        layout.addWidget(mean_frame)

        buffer = StringIO()

        df.info(buf=buffer)
        info_str = buffer.getvalue()

        info_title = QLabel("Information")
        info_layout.addWidget(info_title)
        info_title.setProperty("class", "title")

        info_label = QLabel(info_str)
        info_layout.addWidget(info_label)
        info_label.setProperty("class", "font_color")

        num_columns = df.select_dtypes(include=['int64', 'float64'])
        median_values = num_columns.median()
        median_str = median_values.to_string()
        mean_values = num_columns.mean()
        mean_str = mean_values.to_string()

        median_title = QLabel("Median")
        median_layout.addWidget(median_title, alignment=Qt.AlignTop)
        median_title.setProperty("class", "title")

        median_label = QLabel(median_str)
        median_layout.addWidget(median_label, alignment=Qt.AlignTop)
        median_label.setProperty("class", "font_color")

        mean_title = QLabel("Mean")
        mean_layout.addWidget(mean_title, alignment=Qt.AlignTop)
        mean_title.setProperty("class", "title")

        mean_label = QLabel(mean_str)
        mean_layout.addWidget(mean_label, alignment=Qt.AlignTop )
        mean_label.setProperty("class", "font_color")

        self.setLayout(layout)

        self.load_stylesheet()
    def load_stylesheet(self):
        file = QFile("src/styles/styles.qss")
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
