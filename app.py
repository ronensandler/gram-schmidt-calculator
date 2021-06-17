
import tkinter as tk
from tkinter import ttk

from gui.input_frame import inputFrame

class App:

    instance = None

    def __init__(self, gs_func):
        self.root = tk.Tk()
        self.input_frame = inputFrame(self.root)
        self.submit_btn = tk.Button(self.root, text="Calculate Grahm Schmidt", command=self.calculate_gs)
        self.output_text = tk.Text(self.root)
        self.gs_func = gs_func

    @staticmethod
    def start(gs_func):
        App.instance = App(gs_func)

        app = App.instance
        app.build_window()
        app.root.resizable(width=False, height=False)
        app.root.mainloop()

    @staticmethod
    def close():
        app = App.instance
        app.root.destroy()


    def build_window(self):
        self.input_frame.pack()
        self.submit_btn.pack()
        self.output_text.pack()

    @staticmethod
    def calculate_gs():
        app = App.instance
        input = app.input_frame.get_values()
        app.output_text.delete(1.0, tk.END)
        app.output_text.insert(1.0, app.gs_func(input))

