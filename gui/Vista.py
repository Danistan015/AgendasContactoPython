from tkinter import *
from tkinter import ttk

class Vista(Frame):
    
    def __init__(self, master, menu):
        super().__init__(master, width=890, height=360)
        self.master = master
        self.menu = menu
        self.center(self.menu)  
        self.pack(fill=BOTH, expand=True)
        self.create_widgets()
        
    def center(self, win):
     
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def fCancelar(self):
        self.master.withdraw()  
        self.ventana_anterior.deiconify()
        

    def fNuevo(self):
        pass

    def fGuardar(self):
        pass

    def fModificar(self):
        pass

    def fEliminar(self):
        pass

        

    def create_widgets(self):
        frame1 = Frame(self, bg="#9370DB")
        frame1.place(x=0,y=0,width=110, height=559)
        self.btnGuardar=Button(frame1,text="Guardar", command=self.fNuevo, bg="magenta", fg="white")
        self.btnGuardar.place(x=6,y=50,width=80, height=30 )
        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="magenta", fg="white")
        self.btnModificar.place(x=6,y=90,width=80, height=30)
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="magenta", fg="white")
        self.btnEliminar.place(x=6,y=130,width=80, height=30)
        self.btnBuscar=Button(frame1,text="Buscar", command=self.fGuardar, bg="magenta", fg="white")
        self.btnBuscar.place(x=6,y=170,width=80, height=30)
        self.btnVolver=Button(frame1,text="Volver", command=self.fCancelar, bg="red", fg="white")
        self.btnVolver.place(x=6,y=300,width=80, height=30)
        

        frame2 = Frame(self, bg="#d8bfd8")
        frame2.place(x=95, y=0, width=160, height=559)

        lbl1 = Label(frame2, text="Nombre: ")
        lbl1.place(x=4, y=10)
        self.txtNombre = Entry(frame2)
        self.txtNombre.place(x=4, y=40, width=150, height=20)

        lbl2 = Label(frame2, text=" Apellido: ")
        lbl2.place(x=4, y=70)
        self.txtApellido = Entry(frame2)
        self.txtApellido.place(x=4, y=100, width=150, height=20)

        lbl3 = Label(frame2, text="Telefono: ")
        lbl3.place(x=4, y=130)
        self.txtTelefono = Entry(frame2)
        self.txtTelefono.place(x=4, y=160, width=150, height=20)

        lbl4 = Label(frame2, text=" Correo: ")
        lbl4.place(x=4, y=190)
        self.txtCorreo = Entry(frame2)
        self.txtCorreo.place(x=4, y=220, width=150, height=20)

        lbl5 = Label(frame2, text=" Direccion: ")
        lbl5.place(x=4, y=250)
        self.txtDireccion = Entry(frame2)
        self.txtDireccion.place(x=4, y=280, width=150, height=20)

        

        self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4","col5"))
        self.grid.place(x=247,y=0,width=620, height=459)
        self.grid.column("#0",width=50)
        self.grid.column("col1",width=60, anchor=CENTER)
        self.grid.column("col2",width=90, anchor=CENTER)
        self.grid.column("col3",width=90, anchor=CENTER)
        self.grid.column("col4",width=90, anchor=CENTER)
        self.grid.column("col5",width=100, anchor=CENTER)
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Apellido", anchor=CENTER)
        self.grid.heading("col3", text="Telefono", anchor=CENTER)
        self.grid.heading("col4", text="Correo", anchor=CENTER)
        self.grid.heading("col5", text="Direccion", anchor=CENTER)


