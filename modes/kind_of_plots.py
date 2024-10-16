import tkinter as tk
from tkinter import Tk, Entry, Label, Frame

def title(frame):
    title_label = Label(frame, text="Title:", font=("Arial", 10, "bold"), bg="cyan")
    title_label.grid(row=6, column=0, columnspan=7, sticky='w', padx=5, pady=5)
    _title = Entry(frame)
    _title.grid(row=6, column=2, columnspan=8, sticky='w')


def required_part(frame, type):
    for i in range(10):
        frame.columnconfigure(i, weight=1)
    required_label = Label(frame, text="Required", font=("Arial", 30, "italic"), bg="cyan")
    required_label.grid(row=2, column=0, columnspan=10, pady=20, sticky='w')
    if type == "bar":
        pass
    else:
        _x_label = Label(frame, text="X-axis:", font=("Arial", 10, "bold"), bg='cyan')
        _x_label.grid(row=3, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        x = Entry(frame)
        x.grid(row=3, column=2, columnspan=8, sticky='w')

    if type == "hist" or type == "bar":
        pass
    else:
        _y_label = Label(frame, text="Y-axis:", font=("Arial", 10, "bold"), bg="cyan")
        _y_label.grid(row=4, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        y = Entry(frame)
        y.grid(row=4, column=2, columnspan=8, sticky='w')

class Plot:

    def __init__(self, window):
        self.window = window

        self.plot_frame = Frame(self.window, height=400, bg="cyan")
        self.plot_frame.grid(row=2, column=0, columnspan=10, sticky='sew')

        required_part(self.plot_frame, "plot")

        self.optional_label = Label(self.plot_frame, text="Optional", font=("Arial", 30, "italic"), bg="cyan")
        self.optional_label.grid(row=5, column=0, columnspan=10, pady=20, sticky='w')

        title(self.plot_frame)

        self.x_label_label = Label(self.plot_frame, text="xlabel:", font=("Arial", 10, "bold"), bg="cyan")
        self.x_label_label.grid(row=7, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.x_label = Entry(self.plot_frame)
        self.x_label.grid(row=7, column=2, columnspan=8, sticky='w')

        self.y_label_label = Label(self.plot_frame, text="ylabel:", font=("Arial", 10, "bold"), bg="cyan")
        self.y_label_label.grid(row=8, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.y_label = Entry(self.plot_frame)
        self.y_label.grid(row=8, column=2, columnspan=8, sticky='w')

        self.submit = tk.Button(self.plot_frame, text="submit")
        self.submit.grid(row=9, column=9, pady=20)


class Hist:

    def __init__(self, window):
        self.window = window

        self.hist_frame = tk.Frame(self.window, height=400, bg="cyan")
        self.hist_frame.grid(row=2, column=0, columnspan=10, sticky='sew')

        required_part(self.hist_frame, "hist")

        self.optional_label = tk.Label(self.hist_frame, text="Optional", font=("Arial", 30, "italic"), bg="cyan")
        self.optional_label.grid(row=5, column=0, columnspan=10, pady=20, sticky='w')

        title(self.hist_frame)

        self.x_label_label = tk.Label(self.hist_frame, text="xlabel:", font=("Arial", 10, "bold"), bg="cyan")
        self.x_label_label.grid(row=7, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.x_label = tk.Entry(self.hist_frame)
        self.x_label.grid(row=7, column=2, columnspan=8, sticky='w')

        self.y_label_label = tk.Label(self.hist_frame, text="ylabel:", font=("Arial", 10, "bold"), bg="cyan")
        self.y_label_label.grid(row=8, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.y_label = tk.Entry(self.hist_frame)
        self.y_label.grid(row=8, column=2, columnspan=8, sticky='w')

        self.submit = tk.Button(self.hist_frame, text="submit")
        self.submit.grid(row=9, column=9, pady=20)

class Scatter:

    def __init__(self, window):
        self.window = window

        self.scatter_frame = tk.Frame(self.window, height=400, bg="cyan")
        self.scatter_frame.grid(row=2, column=0, columnspan=10, sticky='sew')

        required_part(self.scatter_frame, "scatter")

        self.optional_label = tk.Label(self.scatter_frame, text="Optional", font=("Arial", 30, "italic"), bg="cyan")
        self.optional_label.grid(row=5, column=0, columnspan=10, pady=20, sticky='w')

        title(self.scatter_frame)

        self.x_label_label = tk.Label(self.scatter_frame, text="xlabel:", font=("Arial", 10, "bold"), bg="cyan")
        self.x_label_label.grid(row=7, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.x_label = tk.Entry(self.scatter_frame)
        self.x_label.grid(row=7, column=2, columnspan=8, sticky='w')

        self.y_label_label = tk.Label(self.scatter_frame, text="ylabel:", font=("Arial", 10, "bold"), bg="cyan")
        self.y_label_label.grid(row=8, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.y_label = tk.Entry(self.scatter_frame)
        self.y_label.grid(row=8, column=2, columnspan=8, sticky='w')

        self.submit = tk.Button(self.scatter_frame, text="submit")
        self.submit.grid(row=9, column=9, pady=20)

class Bar:
    def __init__(self, window):
        self.window = window

        self.bar_frame = tk.Frame(self.window, height=400, bg="cyan")
        self.bar_frame.grid(row=2, column=0, columnspan=10, sticky='sew')

        required_part(self.bar_frame, "bar")

        self.values_label = tk.Label(self.bar_frame, text="Values:", font=("Arial", 10, "bold"), bg='cyan')
        self.values_label.grid(row=3, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.values = tk.Entry(self.bar_frame)
        self.values.grid(row=3, column=2, columnspan=8, sticky='w')

        self.category_label = tk.Label(self.bar_frame, text="Categories:", font=("Arial", 10, "bold"), bg="cyan")
        self.category_label.grid(row=4, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.category = tk.Entry(self.bar_frame)
        self.category.grid(row=4, column=3, columnspan=8, sticky='w')

        self.optional_label = tk.Label(self.bar_frame, text="Optional", font=("Arial", 30, "italic"), bg="cyan")
        self.optional_label.grid(row=5, column=0, columnspan=10, pady=20, sticky='w')

        title(self.bar_frame)

        self.submit = tk.Button(self.bar_frame, text="submit")
        self.submit.grid(row=7, column=9, pady=20)

class Pie:
    def __init__(self, window):
        self.window = window

        self.pie_frame = tk.Frame(self.window, height=400, bg="cyan")
        self.pie_frame.grid(row=2, column=0, columnspan=10, sticky='sew')

        required_part(self.pie_frame, "pie")

        self.optional_label = tk.Label(self.pie_frame, text="Optional", font=("Arial", 30, "italic"), bg="cyan")
        self.optional_label.grid(row=5, column=0, columnspan=10, pady=20, sticky='w')

        title(self.pie_frame)

        self.submit = tk.Button(self.pie_frame, text="submit")
        self.submit.grid(row=7, column=9, pady=20)