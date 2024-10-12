import tkinter as tk
from tkinter import Tk, Entry, Label, Frame


class Plot:

    def __init__(self, window):
        self.window = window

        self.plot_frame = Frame(self.window, height=400)
        self.plot_frame.grid(row=2, column=0, columnspan=10, sticky='sew')


        for i in range(10):
            self.plot_frame.columnconfigure(i, weight=1)
        self.required_label = Label(self.plot_frame, text="Required", font=("Arial", 30, "italic"), bg="cyan")
        self.required_label.grid (row=2, column=0, columnspan=10, pady=20, sticky='w')
        self.x_label = Label(self.plot_frame, text="X-axis array")
        self.x_label.grid(row=3, column=0, columnspan=7, sticky='w', padx=5, pady=10)


        self.x = Entry(self.plot_frame)
        self.x.grid(row= 3, column=4, columnspan=9, sticky='nsew')
