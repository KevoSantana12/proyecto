import pyodbc

class DataAccess:
    def __init__(self):
        self.connection_string = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=app_flask;UID=sa;PWD=123456'

    def save_user(self, name):
        try:
            with pyodbc.connect(self.connection_string) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO usuarios (nombre) OUTPUT INSERTED.id VALUES(?)",(name,))
                user_id = cursor.fetchone()[0]
                conn.commit()
            return user_id
        except Exception as e:
            raise RuntimeError(f'Error al guardar usuario: {e}')