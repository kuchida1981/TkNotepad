from Tkinter import *
from ttk import *

from ScrolledText import ScrolledText

class Mainwindow(Frame):

    def __init__(self, master = None, cnf = {}, **kw):
        Frame.__init__(self, master, *cnf, **kw)

        self.setup_menus()
        self.setup_widgets()

    def setup_menus(self):
        menubar = Menu(self.master)
        self.master.configure(menu = menubar)
        menu_file = Menu(menubar, tearoff = False)
        menubar.add_cascade(label = 'File', underline = 0, menu = menu_file)
        menu_file.add_command(label = 'New', command = self.cmd_new)
        menu_file.add_command(label = 'Open', command = self.cmd_open)
        menu_file.add_command(label = 'Save', command = self.cmd_save)
        menu_file.add_command(label = 'Save As', command = self.cmd_save_as)
        menu_file.add_command(label = 'Close', command = self.cmd_close)
        menu_file.add_command(label = 'Quit', command = self.cmd_quit)

    def setup_widgets(self):
        ScrolledText(self).pack(expand = True, fill = BOTH)

    def cmd_new(self):
        pass

    def cmd_open(self):
        pass

    def cmd_save(self):
        pass

    def cmd_save_as(self):
        pass

    def cmd_close(self):
        pass

    def cmd_quit(self):
        pass

