from tkinter import *
from menu import menu

def main():
    root = Tk()
    root.wm_title("Menu")
    app = menu(root)
    center(root)  
    root.mainloop()

def center(win):

    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

if __name__ == '__main__':
    main()
