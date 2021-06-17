
import tkinter as tk

class inputVector(tk.Frame):
    def __init__(self, master, size, **options):
        super().__init__(master, **options)
        self.master = master
        self.size = size
        self.cells = []
        for i in range(size):
            self.cells.append(tk.Entry(self))
            self.cells[i].insert(0, '0')

    def pack(self, **options):
        for c in self.cells:
            c.pack(side=tk.LEFT)
        super().pack(**options)

    def grid(self, **options):
        for c in self.cells:
            c.pack(side=tk.LEFT)
        super().grid(**options)

    def get_values(self):
        values = []
        for c in self.cells:
            values.append(int(c.get()))
        return values

    def set_size(self, size):
        if self.size < size:
            for i in range(self.size, size):
                self.cells.append(tk.Entry(self))
                self.cells[i].insert(0, '0')
                self.cells[i].pack(side=tk.LEFT)

        if self.size > size:
            while len(self.cells) > size:
                self.cells[-1].destroy()
                self.cells.pop()
        
        self.size = size


class inputTable(tk.Frame):

    def __init__(self, master, rows, columns, **options):
        super().__init__(master, **options)
        self.vectors = []
        self.titles = []
        self.rows = rows
        self.columns = columns
        for i in range(rows):
            self.vectors.append(inputVector(self, columns))
            self.titles.append(tk.Label(self,  text=f"vector {i+1}:"))


    def pack(self, **options):
        for i in range(self.rows):
            self.titles[i].grid(row=i, column=0)
            self.vectors[i].grid(row=i, column=1)
        super().pack(**options)

    def grid(self, **options):
        for i in range(self.rows):
            self.titles[i].grid(row=i, column=0)
            self.vectors[i].grid(row=i, column=1)
        super().grid(**options)

    def get_values(self):
        values = []
        for v in self.vectors:
            values.append(v.get_values())
        return values

    def set_size(self, rows, columns):
        if self.rows < rows:
            for i in range(self.rows, rows):
                self.vectors.append(inputVector(self, self.columns))
                self.titles.append(tk.Label(self,  text=f"vector {i+1}:"))
                self.titles[i].grid(row=i, column=0)
                self.vectors[i].grid(row=i, column=1)
        
        if self.rows > rows:
            while len(self.vectors) > rows:
                self.vectors[-1].destroy()
                self.titles[-1].destroy()
                self.vectors.pop()
                self.titles.pop()

        self.rows = rows

        if self.columns != columns:
            for v in self.vectors:
                v.set_size(columns) 

        self.columns = columns

        
