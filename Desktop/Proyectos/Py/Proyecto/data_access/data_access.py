import pymysql
from entities.entities import User

def obtener_conexion():
    return pymysql.connect(host='localhost',
                                user='root',
                                password='Temach2022NM',
                                db='db_planilla_plus')

class userCRUD:
    def insertar_user(self, user:User):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("INSERT INTO user(nombre, apellido, correo, telefono, compania, contrasena) VALUES (%s, %s,%s,%s, %s, %s)",
                       (user.nombre, user.apellido, user.email, user.telefono, user.compania,user.contrasena,))
        conexion.commit()
        conexion.close()

    def eliminar_user(self, id):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("DELETE FROM user WHERE id = %s", (id,))
        conexion.commit()
        conexion.close()


    def obtener_user_por_id(self, id) -> User:
        conexion = obtener_conexion()
        user = None
        with conexion.cursor() as cursor:
            cursor.execute(
                "SELECT id, nombre, apellido, correo, telefono, compania, contrasena FROM user WHERE id = %s", (id,))
            user = cursor.fetchone()
        conexion.close()
        return user


    def actualizar_user(self, user:User):
        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("UPDATE user SET nombre = %s, apellido = %s, correo = %s, telefono = %s, compania = %s ,contrasena = %s WHERE id = %s",
                        (user.nombre, user.apellido, user.email, user.telefono, user.compania, user.contrasena))
        conexion.commit()
        conexion.close()


    def login(self, email, contrasena) -> User:
        try:
            conexion = obtener_conexion()
            with conexion.cursor() as cursor:
                sql = """
                SELECT id, nombre, apellido, correo, contrasena, compania, telefono
                FROM user
                WHERE correo = %s AND contrasena = %s
                """
                cursor.execute(sql, (email, contrasena))
                resultado = cursor.fetchone()
                if resultado:
                    user = User(
                    id=resultado[0],
                    nombre=resultado[1],
                    apellido=resultado[2],
                    email=resultado[3],
                    contrasena=resultado[4],
                    compania=resultado[5],
                    telefono=resultado[6])
                    return user
                else:
                    print("No se encontró un usuario con el correo y contraseña proporcionados.")
                    return None
        except pymysql.MySQLError as e:
            print(f"Error al obtener el usuario: {e}")
        finally:
            conexion.close()    