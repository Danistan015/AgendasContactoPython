from tkinter import *

raiz=Tk()
raiz.title("Juan presente pues a un parcerito")
#raiz.resizable(True,False)
#raiz.iconbitmap(#va la imagen)
#raiz.geometry("650x300")
raiz.config(bg="pink")
miFrame=Frame()
miFrame.pack(side="center")
miFrame.config(bg="blue")
miFrame.config(width="650",height="350")
raiz.mainloop()