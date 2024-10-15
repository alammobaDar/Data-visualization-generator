import tkinter as tk
from tkinter import Tk, Entry, Label, Frame


class Plot:

    def __init__(self, window):
        self.window = window

        self.plot_frame = Frame(self.window, height=400, bg="cyan")
        self.plot_frame.grid(row=2, column=0, columnspan=10, sticky='sew')


        for i in range(10):
            self.plot_frame.columnconfigure(i, weight=1)
        self.required_label = Label(self.plot_frame, text="Required", font=("Arial", 30, "italic"), bg="cyan")
        self.required_label.grid (row=2, column=0, columnspan=10, pady=20, sticky='w')

        self._x_label = Label(self.plot_frame, text="X-axis:", font=("Arial", 10, "bold"), bg='cyan')
        self._x_label.grid(row=3, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.x = Entry(self.plot_frame)
        self.x.grid(row= 3, column=2, columnspan=8, sticky='w')

        self._y_label = Label(self.plot_frame, text="Y-axis:", font=("Arial", 10, "bold"), bg="cyan")
        self._y_label.grid(row=4, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.y = Entry(self.plot_frame)
        self.y.grid(row=4, column=2, columnspan=8, sticky='w')

        self.optional_label = Label(self.plot_frame, text="Optional", font=("Arial", 30, "italic"), bg="cyan")
        self.optional_label.grid(row=5, column=0, columnspan=10, pady=20, sticky='w')

        self.title_label = Label(self.plot_frame, text="Title:", font=("Arial", 10, "bold"), bg="cyan")
        self.title_label.grid(row=6, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.title = Entry(self.plot_frame)
        self.title.grid(row=6, column=2, columnspan=8, sticky='w')

        self.x_label_label = Label(self.plot_frame, text="xlabel:", font=("Arial", 10, "bold"), bg="cyan")
        self.x_label_label.grid(row=7, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.x_label = Entry(self.plot_frame)
        self.x_label.grid(row=7, column=2, columnspan=8, sticky='w')

        self.y_label_label = Label(self.plot_frame, text="ylabel:", font=("Arial", 10, "bold"), bg="cyan")
        self.y_label_label.grid(row=8, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.y_label = Entry(self.plot_frame)
        self.y_label.grid(row=8, column=2, columnspan=8, sticky='w')

