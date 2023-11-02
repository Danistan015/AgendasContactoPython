from tkinter import *
from Vista import Vista

class menu(Frame):
    
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.boton = Button(self.frame, text='Gestionar contactos', width=30, height=2, command=self.menu, bg="magenta",fg="white")
        self.boton.pack()
        self.frame.pack(pady=50, padx=50)  

    def menu(self):
        self.menu = Toplevel(self.master)
        self.menu.geometry("900x400") 
        self.menu.title("Contactos") 
        self.center(self.menu)  
        self.app = Vista(self.menu, self.master)  
        
    def center(self, win):
     
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
