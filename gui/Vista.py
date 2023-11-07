from tkinter import *
from tkinter import ttk
from Contacto import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import errorcode

def validate_name_input(new_value):
    return all(c.isalpha() or c.isspace() for c in new_value)

def validate_phone_input(new_value):
    return all(c.isdigit() for c in new_value)

class Vista(Frame):
    
    contacto= Contacto()
    
    def __init__(self, master, menu): 
        super().__init__(master,width=590,height=360) 
        self.master = master 
        self.menu = menu
        self.center(self.menu) 
        self.pack(fill=BOTH, expand=True) 
        self.create_widgets() 
        self.llenaDatos() 
        self. id=-1 
        
    def center(self, win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def fVolver(self):
        self.master.withdraw()  
        self.ventana_anterior.deiconify()
        
    
    def fBuscar(self):
        nombre = self.txtNombre.get()
        telefono = self.txtTelefono.get()
        apellido = self.txtApellido.get()

        if nombre == '' and telefono == '' and apellido == '':
            messagebox.showwarning("Buscar", 'Debes ingresar al menos un valor.')
        else:
            # Llama a la función buscar_contacto con los valores ingresados
            resultado = self.contacto.buscar_contacto(nombre, apellido, telefono)

            if resultado:
                self.limpiaGrid()
                for row in resultado:
                    self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
            else:
                messagebox.showinfo("Buscar", "No se encontraron contactos")

            


    def llenaDatos(self):
        datos = self.contacto.consulta_contacto()       
        for row in datos:            
            self.grid.insert("",END,text=row[0], values=(row[1],row[2], row[3],row[4],row[5]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set( self.grid.get_children()[0] )
            
            
            
        
    def limpiarCajas(self):
        self.txtNombre.delete(0,END)
        self.txtApellido.delete(0,END)
        self.txtTelefono.delete(0,END)
        self.txtCorreo.delete(0,END)
        self.txtDireccion.delete(0,END)
        
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
                

    def fGuardar(self): 
        try:
            if self.id == -1:       
                self.contacto.guardar_contacto(self.txtNombre.get(), self.txtApellido.get(), self.txtTelefono.get(), self.txtCorreo.get(), self.txtDireccion.get())            
                messagebox.showinfo("Guardar", 'Elemento insertado correctamente.')
            else:
                self.contacto.modificar_contacto(self.id, self.txtNombre.get(), self.txtApellido.get(), self.txtTelefono.get(), self.txtCorreo.get(), self.txtDireccion.get())
                messagebox.showinfo("Modificar", 'Elemento modificado correctamente.')
            self.id = -1
            self.limpiaGrid()
            self.llenaDatos() 
            self.limpiarCajas() 
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DUP_ENTRY:
                messagebox.showerror("Error", "El número de teléfono ya existe en la base de datos. Por favor, utilice un número de teléfono diferente.")
            else:
                messagebox.showerror("Error", "Se produjo un error en la base de datos: {}".format(err))




    def fCargarDatos(self):        
        selected = self.grid.focus()                               
        clave = self.grid.item(selected, 'text')        
        if clave == '':
            messagebox.showwarning("Modificar", 'Debes seleccionar un elemento.')            
        else:            
            self.id = clave                         
            valores = self.grid.item(selected, 'values')
            self.limpiarCajas()            
            self.txtNombre.insert(0, valores[0])
            self.txtApellido.insert(0, valores[1])
            self.txtTelefono.insert(0, valores[2])
            self.txtCorreo.insert(0, valores[3])
            self.txtDireccion.insert(0, valores[4])
            self.txtNombre.focus() 


                                            
    def fEliminar(self):
        selected = self.grid.focus()                               
        clave = self.grid.item(selected,'text')        
        if clave == '':
            messagebox.showwarning("Eliminar", 'Debes seleccionar un elemento.')            
        else:                           
            valores = self.grid.item(selected,'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n" + data)            
            if r == messagebox.YES:
                n = self.contacto.eliminar_contacto(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado correctamente.')
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showwarning("Eliminar", 'No fue posible eliminar el elemento.')

    def fCargarTabla(self):
        self.limpiaGrid()  
        self.llenaDatos()
    def fLimpiar(self):
        self.limpiarCajas()  
        self.txtNombre.focus() 
        

    def create_widgets(self):
        frame1 = Frame(self, bg="#9370DB")
        frame1.place(x=0,y=0,width=150, height=559)
        self.btnGuardar=Button(frame1,text="Guardar", command=self.fGuardar, bg="magenta", fg="white")
        self.btnGuardar.place(x=6,y=50,width=80, height=30 )
        self.btnCargarDatos=Button(frame1,text="Cargar Datos", command=self.fCargarDatos, bg="magenta", fg="white")
        self.btnCargarDatos.place(x=6,y=90,width=80, height=30)
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="magenta", fg="white")
        self.btnEliminar.place(x=6,y=130,width=80, height=30)
        self.btnBuscar=Button(frame1,text="Buscar", command=self.fBuscar, bg="magenta", fg="white")
        self.btnBuscar.place(x=6,y=170,width=80, height=30)
        self.btnCargarTabla=Button(frame1,text="Cargar Tabla", command=self.fCargarTabla, bg="magenta", fg="white")
        self.btnCargarTabla.place(x=6,y=210,width=80, height=30)
        self.btnLimpiar=Button(frame1,text="Limpiar texto", command=self.fLimpiar, bg="magenta", fg="white")
        self.btnLimpiar.place(x=6,y=250,width=80, height=30)
        
    
    
        self.btnVolver=Button(frame1,text="Volver", command=self.fVolver, bg="red", fg="white")
        self.btnVolver.place(x=6,y=300,width=80, height=30)
        

        frame2 = Frame(self, bg="#d8bfd8")
        frame2.place(x=95, y=0, width=160, height=559)

        lbl1 = Label(frame2, text="Nombre: ")
        lbl1.place(x=4, y=10)
        self.txtNombre = Entry(frame2, validate="key")
        self.txtNombre['validatecommand'] = (self.txtNombre.register(validate_name_input), '%P')
        self.txtNombre.place(x=4, y=40, width=140, height=20)

        lbl2 = Label(frame2, text=" Apellido: ")
        lbl2.place(x=4, y=70)
        self.txtApellido = Entry(frame2, validate="key")
        self.txtApellido['validatecommand'] = (self.txtApellido.register(validate_name_input), '%P')
        self.txtApellido.place(x=4, y=100, width=140, height=20)

        lbl3 = Label(frame2, text="Telefono: ")
        lbl3.place(x=4, y=130)
        self.txtTelefono = Entry(frame2, validate="key")
        self.txtTelefono['validatecommand'] = (self.txtTelefono.register(validate_phone_input), '%P')
        self.txtTelefono.place(x=4, y=160, width=140, height=20)
        
        lbl4 = Label(frame2, text=" Correo: ")
        lbl4.place(x=4, y=190)
        self.txtCorreo = Entry(frame2)
        self.txtCorreo.place(x=4, y=220, width=140, height=20)

        lbl5 = Label(frame2, text=" Direccion: ")
        lbl5.place(x=4, y=250)
        self.txtDireccion = Entry(frame2)
        self.txtDireccion.place(x=4, y=280, width=140, height=20)

        

        self.grid = ttk.Treeview(self, columns=("col1","col2","col3","col4","col5"))
        self.grid.place(x=247,y=0,width=650, height=459)
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


