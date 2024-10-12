import tkinter as tk

class Pie:
    def __init__(self, window):
        self.window = window

        self.pie_frame = tk.Frame(self.window, height=400, bg="cyan")
        self.pie_frame.grid(row=2, column=0, columnspan=10, sticky='sew')

        for i in range(10):
            self.pie_frame.columnconfigure(i, weight=1)
        self.required_label = tk.Label(self.pie_frame, text="Required", font=("Arial", 30, "italic"), bg="cyan")
        self.required_label.grid(row=2, column=0, columnspan=10, pady=20, sticky='w')

        self.x_label = tk.Label(self.pie_frame, text="X-axis:", font=("Arial", 10, "bold"), bg='cyan')
        self.x_label.grid(row=3, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.x = tk.Entry(self.pie_frame)
        self.x.grid(row=3, column=2, columnspan=8, sticky='w')

        self.y_label = tk.Label(self.pie_frame,
                                text="Y-axis:",
                                font=("Arial", 10, "bold"),
                                bg="cyan")

        self.y_label.grid(row=4, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.y = tk.Entry(self.pie_frame)
        self.y.grid(row=4, column=2, columnspan=8, sticky='w')
