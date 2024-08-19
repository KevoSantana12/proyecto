from data_access.data_access import userCRUD
from entities.entities import User

class BusinessLogic:
    def __init__(self):
        self.data_access = userCRUD()
    
    def crear_user(self, user:User):
        self.data_access.insertar_user(user=user)
    
    def get_user(self, id) -> User:
        return self.data_access.obtener_user_por_id(id=id)
    
    def update_user(self, user: User):
        self.data_access.actualizar_user(user=user)
   
    def deleteUser(self, id):
        self.data_access.eliminar_user(id)

    def login(self, email, contrasena) -> User:
        return self.data_access.login(email=email, contrasena=contrasena)
