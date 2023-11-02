import mysql.connector

class Contacto:
    
    def __init__(self, nombre, apellido, telefono, correo, direccion):
        self._nombre = nombre
        self._apellido = apellido
        self._telefono = telefono
        self._correo = correo
        self._direccion = direccion

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter 
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo
        
    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    def __str__(self):
        datos = self.consulta_contacto()        
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux
        
    def consulta_contacto(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM contacto")
        datos = cur.fetchall()
        cur.close()    
        return datos
    
    def buscar_contacto(self, nombre, apellido, telefono):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM contacto WHERE nombre = '{}' OR apellido = '{}' OR telefono = '{}'".format(nombre, apellido, telefono)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos

    def guardar_contacto(self, nombre, apellido, telefono, correo, direccion):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO contacto (nombre, apellido, telefono, correo, direccion) 
        VALUES('{}', '{}', '{}', '{}', '{}')'''.format(nombre, apellido, telefono, correo, direccion)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def eliminar_contacto(self, Id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM contacto WHERE id = {}'''.format(Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modificar_contacto(self, Id, nombre, apellido, telefono, correo, direccion):
        cur = self.cnn.cursor()
        sql = '''UPDATE contacto SET nombre='{}', apellido='{}', telefono='{}',
        correo='{}', direccion='{}' WHERE id={}'''.format(nombre, apellido, telefono, correo, direccion, Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n  

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="", database="db_python")
