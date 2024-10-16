import tkinter as tk
from tkinter import Tk, filedialog, Scrollbar, HORIZONTAL, ttk
import pandas as pd

def upload():
    filetypes = [
        ("CSV files", "*.csv"),
        ("Excel files", "*.xlsx, *.xls")
    ]

    file_name = filedialog.askopenfilename(title="Open file", filetypes=filetypes)

    df = None
    if file_name:
        if file_name.endswith(".xlsx"):
            df = pd.read_excel(file_name)
        elif file_name.endswith(".csv"):
            df = pd.read_csv(file_name)

    return df


def show_df(df, frame):
    data_frame = tk.Frame(frame, height=300, width=730, bg="pink")
    data_frame.pack()

    columns = list(df.columns)

    tree = ttk.Treeview(data_frame, columns=columns, show='headings')
    for col in df.columns:
        tree.heading(col, text=col)
    for _, rows in df.iterrows():
        tree.insert("", "end", values=list(rows))

    tree.pack()

    horizontal_scrollbar = Scrollbar(data_frame, orient=HORIZONTAL, command=tree.xview)
    tree.configure(xscrollcommand=horizontal_scrollbar.set)
    horizontal_scrollbar.pack(anchor='s', fill=tk.X, expand=True)


