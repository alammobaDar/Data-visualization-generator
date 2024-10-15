import tkinter as tk

class Bar:
    def __init__(self, window):
        self.window = window

        self.bar_frame = tk.Frame(self.window, height=400, bg="cyan")
        self.bar_frame.grid(row=2, column=0, columnspan=10, sticky='sew')

        for i in range(10):
            self.bar_frame.columnconfigure(i, weight=1)
        self.required_label = tk.Label(self.bar_frame, text="Required", font=("Arial", 30, "italic"), bg="cyan")
        self.required_label.grid(row=2, column=0, columnspan=10, pady=20, sticky='w')

        self.values_label = tk.Label(self.bar_frame, text="Values:", font=("Arial", 10, "bold"), bg='cyan')
        self.values_label.grid(row=3, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.values = tk.Entry(self.bar_frame)
        self.values.grid(row=3, column=2, columnspan=8, sticky='w')

        self.category_label = tk.Label(self.bar_frame, text="Categories:", font=("Arial", 10, "bold"), bg="cyan")
        self.category_label.grid(row=4, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.category = tk.Entry(self.bar_frame)
        self.category.grid(row=4, column=2, columnspan=8, sticky='w')

        self.optional_label = tk.Label(self.bar_frame, text="Optional", font=("Arial", 30, "italic"), bg="cyan")
        self.optional_label.grid(row=5, column=0, columnspan=10, pady=20, sticky='w')

        self.title_label = tk.Label(self.bar_frame, text="Title:", font=("Arial", 10, "bold"), bg="cyan")
        self.title_label.grid(row=6, column=0, columnspan=7, sticky='w', padx=5, pady=5)
        self.title = tk.Entry(self.bar_frame)
        self.title.grid(row=6, column=2, columnspan=8, sticky='w')