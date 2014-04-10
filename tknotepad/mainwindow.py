import Tkinter as tk

class Mainwindow(tk.Frame):

    def __init__(self, master = None, cnf = {}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw)
        self.setup_menus()
        self.setup_widgets()

    def setup_menus(self):
        pass

    def setup_widgets(self):
        tk.Text(self).pack(expand = True, fill = tk.BOTH)
