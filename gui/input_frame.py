
import tkinter as tk
from tkinter import ttk

from gui.input_table import inputTable

class inputFrame(tk.Frame):

    def __init__(self, master, **options):
        super().__init__(master, **options)
        # self.rows_var = tk.IntVar()
        # self.columns_var = tk.IntVar()
        self.rows_box = ttk.Spinbox(self, from_=1, to=5, command=self.refresh_size)
        self.rows_box.insert(0, 5)
        self.columns_box = ttk.Spinbox(self, from_=1, to=5, command=self.refresh_size)
        self.columns_box.insert(0, 5)
        self.rows_label = tk.Label(self, text="Vectors Count:")
        self.columns_label = tk.Label(self, text="Vectors Size:")
        self.table = inputTable(self, 5 ,5)

    def pack(self, **options):
        self.rows_label.grid(row=0, column=0)
        self.rows_box.grid(row=0, column=1)
        self.columns_label.grid(row=0, column=2)
        self.columns_box.grid(row=0, column=3)
        self.table.grid(row=1, column=0, columnspan=4)
        super().pack(**options)

    def grid(self, **options):
        self.rows_label.grid(row=0, column=0)
        self.rows_box.grid(row=0, column=1)
        self.columns_label.grid(row=0, column=2)
        self.columns_box.grid(row=0, column=3)
        self.table.grid(row=1, column=0, columnspan=4)
        super().grid(**options)

    def get_values(self):
        return self.table.get_values()

    def refresh_size(self):
        self.table.set_size(int(self.rows_box.get()), int(self.columns_box.get()))