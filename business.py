# from data_access import DataAccess
# from entities import User

# class BusinessLogic:
#     def __init__(self):
#         self.data_access = DataAccess()
    
#     def process_user(self,user:User):
#         user.validate()
#         user_id = self.data_access.save_user(user.name)
#         user.id = user_id

#         return f"Usuario {user.name} guardado con ID {user.id}"
    
#     def get_all_users(self):
#         return self.data_access.get_all_users()
    
#     def update_user(self, user: User):
#         user.validate()
#         self.data_access.update_user(user.id, user.name)
#         return f"Usuario {user.name}, actualizado correctamente"
   
#     def deleteUser(self, userId):
#         self.data_access.deleteUser(userId)
#         return f"Usuario {userId}, eliminado correctamente"
        
