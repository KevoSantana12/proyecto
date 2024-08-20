from data_access.data_access import userCRUD
from data_access.data_access import EmpleadoCRUD
from entities.entities import User

class User_logica:
    def __init__(self):
        self.data_access = userCRUD()
        self.empleado_data_access = EmpleadoCRUD()
        
    def crear_user(self, user:User):
        self.data_access.insertar_user(user=user)
    
    def get_user(self, id) -> User:
        return self.data_access.obtener_user_por_id(id=id)
    
    def update_user(self, userEditado: User, id:int):
        user = self.get_user(id)
        user.nombre = userEditado.nombre
        user.apellido = userEditado.apellido
        user.compania = userEditado.compania
        user.telefono = userEditado.telefono
        user.email = userEditado.email
        self.data_access.actualizar_user(user=user)
   
    def deleteUser(self, id):
        self.empleado_data_access.eliminar_empleados_por_usuario(id)
        self.data_access.eliminar_user(id)

    def login(self, email, contrasena) -> User:
        return self.data_access.login(email=email, contrasena=contrasena)
