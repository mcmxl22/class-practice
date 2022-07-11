import tkinter as tk
from time import strftime

root = tk.Tk()


class StartWindow:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=80, height=30)
        self.canvas.place(x=0, y=0)
        self.clock = Clock(master=self, x=50, y=25, text="Time")


class Clock:
    def __init__(self, master, x, y, text=""):
        self.master = master
        self.clock = self.master.canvas.create_text(x, y, text=text)
        self.set_time()

    def set_time(self):
        self.master.canvas.itemconfig(self.clock, text=strftime("%H:%M:%S"))
        self.master.root.after(10, self.set_time)


st = StartWindow(root)
root.mainloop()
