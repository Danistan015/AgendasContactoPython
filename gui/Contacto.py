class Contacto:
    def __init__(self, nombre, apellido, telefono, correo, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
    
    @property
    def nombre(self):
        return self.nombre
    
    
    @nombre.setter 
    def nombre(self, nombre):
        self.nombre = nombre
    
    @property
    def apellido(self):
        return self.apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self.apellido = apellido
    
    @property
    def telefono(self):
        return self.telefono
    
    @telefono.setter
    def telefono(self, telefono):
        self.telefono = telefono
    
    @property
    def correo(self):
        return self.correo
    
    @correo.setter
    def correo(self, correo):
        self.correo = correo
        
    @property
    def direccion(self):
        return self.direccion
    
    @direccion.setter
    def direccion(self, direccion):
        self.direccion = direccion
    
    
    
        
    