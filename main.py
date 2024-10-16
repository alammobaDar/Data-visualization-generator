from tkinter import Tk, Label, Button, filedialog, ttk, Scrollbar
import tkinter as tk
from tkinter.constants import VERTICAL, HORIZONTAL
from tkinter.ttk import Combobox
import pandas as pd

from modes import kind_of_plots


class UI:

    def __init__(self, window):
        self.window = window
        self.window.title("Matplotlib Generator")
        self.window.geometry("1200x700")

        # Configure grid layout to allow expansion
        self.window.grid_columnconfigure(0)  # For dashboard
        self.window.grid_columnconfigure(1, weight=2)  # For main_section
        self.window.grid_rowconfigure(1, weight=1)  # For both dashboard and main_section

        #Division of the whole window
        self.title_bar = tk.Frame(self.window, bg="green", height=100, width=1200)
        self.title_bar.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.dashboard = tk.Frame(self.window, bg="cyan", height=600, width=450)
        self.dashboard.grid(row=1, column=0, sticky="ns")

        self.main_section = tk.Frame(self.window, bg="red", height=600, width=750)
        self.main_section.grid(row=1, column=1, sticky='nsew')

        #Header
        self._title = Label(self.title_bar, text="Data Visualization Tool", font=("Courier", 25, "bold"), bg="green")
        self._title.pack()

        # Frame to hold label and button, centered
        self.upload_frame = tk.Frame(self.main_section, bg="red")  # Wrapper frame for centering
        self.upload_frame.pack(expand=True)  # Make the frame fill available space

        self.upload_label = Label(self.upload_frame, text="Please upload your Excel file or CSV file", bg="red")
        self.upload_label.pack(pady=10)
        self.upload_button = Button(self.upload_frame, text="upload", command=self.load_and_display_data)
        self.upload_button.pack()

        #combo box for the type of plot that the user will going to use.

        for i in range(10):
            self.dashboard.columnconfigure(i, weight=1)

        self.select_label = Label(self.dashboard, text="Please choose what kind of plot you want to use", bg="cyan")
        self.select_label.grid(row=0, column=0, columnspan=7, sticky='nsew', pady=10)

        self.selected_plot = tk.StringVar()

        self.select_plot = Combobox(self.dashboard, textvariable=self.selected_plot)
        self.select_plot['values'] = [
            "Plot",
            "Hist",
            "Scatter",
            "Bar",
            "Pie"
        ]
        self.select_plot['state'] = 'readonly'
        self.select_plot.grid(row=1, column=0,columnspan=10, sticky='nsew', padx=100)
        self.select_plot.bind("<<ComboboxSelected>>", self.on_combo_box)

        self.pl = kind_of_plots

        #creating instances of plots.
        self.plot_instance = self.pl.Plot(self.dashboard)
        self.hist_instance = self.pl.Hist(self.dashboard)
        self.bar_instance = self.pl.Bar(self.dashboard)
        self.pie_instance = self.pl.Pie(self.dashboard)
        self.scatter_instance = self.pl.Scatter(self.dashboard)

        #then forgets it
        self.erase_frame()

    def erase_frame(self):
        self.plot_instance.plot_frame.destroy()
        self.hist_instance.hist_frame.destroy()
        self.scatter_instance.scatter_frame.destroy()
        self.bar_instance.bar_frame.destroy()
        self.pie_instance.pie_frame.destroy()

    def on_combo_box(self, event):
        selected_value = self.select_plot.get()
        self.erase_frame()
        if selected_value == "Plot":
            self.plot_instance = self.pl.Plot(self.dashboard)
        elif selected_value == "Hist":
            self.hist_instance = self.pl.Hist(self.dashboard)
        elif selected_value == "Scatter":
            self.scatter_instance = self.pl.Scatter(self.dashboard)
        elif selected_value == "Bar":
            self.bar_instance = self.pl.Bar(self.dashboard)
        elif selected_value == "Pie":
            self.pie_instance = self.pl.Pie(self.dashboard)

    def upload(self):
        filetypes =[
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

    def show_df(self, df):

        self.data_frame = tk.Frame(self.main_section, height=300, width=730, bg="pink")
        self.data_frame.pack()

        columns = list(df.columns)

        tree = ttk.Treeview(self.data_frame, columns=columns, show='headings')
        for col in df.columns:
            tree.heading(col, text=col)
        for _, rows in df.iterrows():
            tree.insert("", "end", values=list(rows))

        tree.pack()

        horizontal_scrollbar = Scrollbar(self.data_frame, orient=HORIZONTAL, command=tree.xview)
        tree.configure(xscrollcommand=horizontal_scrollbar.set)
        horizontal_scrollbar.pack(anchor='s', fill=tk.X, expand=True)

    def load_and_display_data(self):
        df = self.upload()
        if df is not None:
            self.upload_frame.destroy()
            self.show_df(df)



if __name__ == "__main__":
    window = Tk()
    ui = UI(window)
    window.mainloop()