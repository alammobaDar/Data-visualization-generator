import tkinter as tk
from tkinter import Tk, Entry


class Plot:

    def __init__(self, window):
        self.window = window

        self.x = Entry(window, text="X-axis array")
        self.x.grid(row= 1, column=1, columnspan=6, sticky='nsew')
