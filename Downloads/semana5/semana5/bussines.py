from data_access import DataAccess
from entities import User

class BussinessLogic:
    def __init__(self):
        self.data_acess = DataAccess()
    
    def process_user(self, user: User):
        user.validate()
        user_id = self.data_acess.save_user(user.name)
        user.id = user_id
        return f'Usuario {user.name} guardado con el nombre {user.id}'