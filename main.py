from tkinter import Tk
import tkinter as tk



class UI:

    def __init__(self, window):
        self.window = window
        self.window.title("Matplotlib Generator")
        self.window.geometry("1200x700")

        self.title_bar = tk.Frame(self.window, bg="green", height=100, width=1200)
        self.title_bar.grid(row=0, column=0, columnspan=2, sticky="ew")

        self.dashboard = tk.Frame(self.window, bg="cyan", height=600, width=450)
        self.dashboard.grid(row=1, column=0, sticky="ns")

        self.main_section = tk.Frame(self.window, bg="red", height=600, width=750)
        self.main_section.grid(row=1, column=1, sticky='nsew')

if __name__ == "__main__":
    window = Tk()
    ui = UI(window)
    window.mainloop()