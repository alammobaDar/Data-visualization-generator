from tkinter import Tk, Label, Button
import tkinter as tk



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
        self.upload_button = Button(self.upload_frame, text="upload")
        self.upload_button.pack()



        def upload():
            self.window.tk


if __name__ == "__main__":
    window = Tk()
    ui = UI(window)
    window.mainloop()