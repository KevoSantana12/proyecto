# import pyodbc

# class DataAccess:
#     def __init__(self):
#         self.connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=app_flask;UID=sa;PWD=123456'

#     def save_user(self,name):
#         try:
#             with pyodbc.connect(self.connection_string) as conn:
#                 cursor = conn.cursor()
#                 cursor.execute("INSERT INTO usuarios (nombre) OUTPUT INSERTED.id values(?)",(name,))
#                 user_id = cursor.fetchone()[0]
#                 conn.commit()
#             return user_id
#         except Exception as e:
#             raise RuntimeError(f"Error al guardar Usuario: {e}")

#     def get_all_users(self):
#         try:
#             with pyodbc.connect(self.connection_string) as conn:
#                 cursor = conn.cursor()
#                 cursor.execute("SELECT id, nombre FROM usuarios")  
#                 rows = cursor.fetchall()
#                 users = []
#                 for row in rows:
#                     users.append({"id": row[0], "name": row[1]})  
#             return users
#         except Exception as err:
#             raise RuntimeError(f"Error al obtener los usuario: {err}")
        
#     def update_user(self, id, nombre):
#         try:
#             with pyodbc.connect(self.connection_string) as conn:
#                 cursor = conn.cursor()
#                 cursor.execute("UPDATE usuarios SET nombre = ? WHERE id = ?", (nombre, id))
#                 cursor.commit()
#         except Exception as err:
#             raise RuntimeError(f"Error al actualizar usuario: {err}")
        
#     def deleteUser(self, id):
#         try:
#             with pyodbc.connect(self.connection_string) as conn:
#                 cursor = conn.cursor()
#                 cursor.execute("DELETE usuarios WHERE id = ?", (id))
#                 cursor.commit()
#         except Exception as err:
#             raise RuntimeError(f"Error al borrar usuario usuario: {err}")
       