import psycopg2
from decouple import config

# Configuración de las variables de entorno
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST')
DB_PORT = config('DB_PORT')
DB_NAME = config('DB_NAME')

# Conexión a la base de datos utilizando las variables de entorno
connection = psycopg2.connect(
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME
)

#Base de datos local para almacenar clientes registrados al banco
def insertar_cliente(cliente):
    with connection.cursor() as cursor:
        cursor.execute('''
                INSERT INTO clientes_bank (nombre, apellido, email, num_cel, pass, num_cuenta)
                VALUES (%s, %s, %s, %s, %s, %s)
                ''', (cliente.nombre, cliente.apellido, cliente.email, cliente.num_cel, cliente.password, cliente.num_cuenta))
    connection.commit()

#función para verificar si hay clientes registrados con los mismos datos
def verificar_existencia_cliente(cliente):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT * FROM clientes_bank WHERE num_cel = %s OR email = %s
        ''', (cliente.num_cel, cliente.email))
        cliente_existente = cursor.fetchone()

    return cliente_existente is not None

#función para cerrar conexión con la base de datos
def cerrar_conexion():
    connection.close()