class User:
    def __init__(self, id = None, nombre = None, apellido = None, compania = None, telefono = None, email = None, contrasena = None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasena = contrasena
        self.compania = compania
        self.telefono = telefono