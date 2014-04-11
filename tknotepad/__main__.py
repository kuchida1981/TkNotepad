import sys
import Tkinter as tk
from mainwindow import Mainwindow

def main(argv):
    root = tk.Tk()
    mainwindow = Mainwindow(master = root)
    mainwindow.pack(expand = True, fill = tk.BOTH)
    root.mainloop()

if __name__ == '__main__':
    main(sys.argv)
