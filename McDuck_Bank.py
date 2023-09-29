"""
Este código simula el registro y manejo de cuentas bancarias a traves de un menu de opciones.
"""

import re
from os import system
from random import randint
import phonenumbers

#Base de datos local para almacenar clientes registrados al banco
clientes_registrados = []

#OOP del cliente con sus funciones de depositar y retirar, ademas del inicio de sesión
class Persona:
    def __init__(self, nombre, apellido, email, num_cel, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.num_cel = num_cel
        self.password = password

class Cliente(Persona):
    def __init__(self, nombre, apellido, email, num_cel, password, num_cuenta, balance):
        super().__init__(nombre, apellido, email, num_cel, password)
        self.num_cuenta = num_cuenta
        self.balance = balance

    def __str__(self):
        return f"\nCliente: {self.nombre} {self.apellido}\nEmail: {self.email}\nNum. Tel: {self.num_cel}\nNum. de cuenta: {self.num_cuenta}\nBalance: ${self.balance}"
    
    def depositar(self, deposito):
        self.balance += deposito
        print("Deposito realizado")

    def retirar(self, retiro):
        if self.balance >= retiro:
            self.balance -= retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")

    @staticmethod
    def iniciar_sesion(num_cel, password):
        for cliente in clientes_registrados:
            if cliente.num_cel == num_cel and cliente.password == password:
                return cliente
            else:
                print("Datos incorrectos.")
        return None

#Función para validar contraseña usando Regular expresions.
def validar_contraseña(contraseña):
    if not re.search(r'[a-z]', contraseña):
        return False
    
    if not re.search(r'[A-Z]', contraseña):
        return False
    
    if not re.search(r'[0-9]', contraseña):
        return False
    
    if not re.search(r'[!"#$%&/()=?¡¿\-.,]', contraseña):
        return False
    
    if len(contraseña) < 6:
        return False
    
    return True

#Funcion para validar correo electrónico usando regular expresions.
def validar_correo(email):
    if re.match(r'^[a-zA-Z0-9._%+-]+@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$', email):
        return True
    else:
        return False

#Funcion para validar telefono usando libreria Phonenumber    
def validar_telefono(numero_telefono):
    numero_telefono = "+52" + numero_telefono  # Agregamos la lada directamente
    try:
        parsed_numero = phonenumbers.parse(numero_telefono, None)

        if phonenumbers.is_valid_number(parsed_numero):
            print("Número de celular válido:", phonenumbers.format_number(parsed_numero, phonenumbers.PhoneNumberFormat.E164))
            return phonenumbers.format_number(parsed_numero, phonenumbers.PhoneNumberFormat.E164)  # Retornamos el número válido
        else:
            print("Ingrese un número de celular válido (lada + número celular). Inténtelo nuevamente.")
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Número de celular inválido. Inténtelo nuevamente.")

#Funcion para validar nombre/nombres del usuario
def validar_nombre(nombre_cliente):
    nombres = nombre_cliente.split()

    if len(nombres) == 1 or len(nombres) == 2:
        if all(nombre.isalpha() for nombre in nombres):
            if len(nombres) == 1:
                primer_nombre = nombres[0] 
                return primer_nombre
            else:
                return nombres
        else:
            print("Los nombres solo deben contener letras.")
    else:
        print("Ingresa uno o dos nombres, separados por espacio.")

#Funcion para validar que solo se coloque 1 apellido y que no contenga numeros ni simbolos
def validar_apellido(nombre):
    if nombre.isalpha():
        return nombre
    else:
        print("\n-----------------Error-----------------")

#funcion para crear cliente BIM BIM BAM BAM... SUKA BLYAD EAAASYYY
def crear_cliente():
    print("Proporcionanos tus datos para registrarte...\nNo venderemos tus datos a un comerciante ruso.")
    while True:
        nombre_cliente = input("Coloque su nombre: ").upper()
        if validar_nombre(nombre_cliente):
            break
        else:
            continue

    while True:
        apellido1 = input("Ingrese su apellido paterno: ").upper()
        if validar_apellido(apellido1):
            break
        else:
            print("Favor de colocar tu apellido paterno correctamente")
    while True:
        apellido2 = input("Ingrese su apellido materno: ").upper()
        if validar_apellido(apellido2):
            break
        else:
            print("Favor de colocar tu apellido materno correctamente")
    apellido_cliente = apellido1 + " " + apellido2

    while True:
        email_cl = input("Ingrese su email: ")
        if validar_correo(email_cl):
            break
        else:
            print("Ingrese un correo electrónico válido.")

    while True:
        num_celular_cl = input("Ingrese un número de celular (lada + número celular): ")
        num_celular = validar_telefono(num_celular_cl)
        if num_celular:
            break
        else:
            print("Favor de ingresar un numero de telefono válido.")

    while True:
        print(""" La contraseña debe contener:
              Al menos Una minuscula.
              Al menos Una mayuscula
              Al menos Un número
              Al menos Un simbolo.
              Al menos 6 caracteres
              """)
        passwd = input("Ingrese su contraseña: ")
        if validar_contraseña(passwd):
            break
        else:
            print("Por favor, ingresa una contraseña válida.")

    numero_cuenta = randint(1000000000,9999999999)

    balance_cuenta = 0

    cliente = Cliente(nombre_cliente, apellido_cliente, email_cl, num_celular, passwd, numero_cuenta, balance_cuenta)
    return cliente

#funcion del menu inicial del programa
def inicio():
    system("cls")
    print("*" * 80)
    print(" Bienvenido a nuestro sistema bancario offline SUKA BLYAD, danos todo tu dinero. ")
    print("*" * 80)

    opcion = "x"
    while not opcion.isnumeric() or int(opcion) not in range(1, 4):
        print("Elige una categoría de nuestro menú de opciones ")
        print('''
              [1] - Crear cuenta
              [2] - Iniciar sesión
              [3] - Finalizar Programa
              ''')
        opcion = input("Elige un número del 1 al 3 según el menú: ")
    return int(opcion)

#Funcion del menu de la cuenta del cliente (ya iniciada la sesión)
def menu_cliente():
    print(cliente_iniciado)
    opcion_cliente = "x"
    while not opcion_cliente.isnumeric() or int(opcion_cliente) not in range(1,4):
        print("\nElige una categoría de nuestro menu de opciones ")
        print('''
                [1] - Depositar
                [2] - Retirar
                [3] - Cerrar Sesion
                ''')
        opcion_cliente = input("Elige un numero del 1 al 3 segun el menú: ")
    return int(opcion_cliente)

def volver_inicio():
    eleccion_regresar = "x"

    while eleccion_regresar.lower() != "s":
        eleccion_regresar = input("\n Presiona s para salir: ")

#Programa
finalizar_programa = False

while not finalizar_programa:
    menu = inicio()
    if menu == 1:
        mi_cliente = crear_cliente()
        # Verificar si el cliente ya está registrado
        cliente_existente = next((cliente for cliente in clientes_registrados if cliente.num_cel == mi_cliente.num_cel or cliente.email == mi_cliente.email), None)
        
        if cliente_existente:
            print("Ya existe un cliente con los datos anteriormente registrados")
        else:
            clientes_registrados.append(mi_cliente)
            print("\nSu registro ha sido exitoso!\n")
        
        volver_inicio()
    elif menu == 2:
        if len(clientes_registrados) == 0:
            print("Aun no te has registrado")
            volver_inicio()
        else:
            num_cel = ("+52" + input("Ingrese su numero de telefono: "))
            password = input("Ingrese su contraseña: ")
            cliente_iniciado = Cliente.iniciar_sesion(num_cel, password)
            if cliente_iniciado:
                print(f"\nInicio de sesión exitoso como {cliente_iniciado.nombre} {cliente_iniciado.apellido}")

                salida = False
                while not salida:
                    menu_bancario = menu_cliente()
                    if menu_bancario == 1:
                        print(f"\n¡Hola! {cliente_iniciado.nombre} {cliente_iniciado.apellido}")
                        print(f"Su balance es: {cliente_iniciado.balance}\n")
                        monto_deposito = int(input("Monto a depositar: "))
                        cliente_iniciado.depositar(monto_deposito)
                        volver_inicio()
                    elif menu_bancario == 2:
                        print(f"\n¡Hola! {cliente_iniciado.nombre} {cliente_iniciado.apellido}")
                        print(f"Su balance es: {cliente_iniciado.balance}\n")
                        monto_retiro = int(input("Monto a retirar: "))
                        cliente_iniciado.retirar(monto_retiro)
                        volver_inicio()
                    elif menu_bancario == 3:
                        salida = True
            else:
                print("Credenciales incorrectas. Intente nuevamente o cree una cuenta.")
                volver_inicio()  
    elif menu == 3:
        print("Gracias por elegir nuestro Banco... SUKA BLYAD")
        print("----------------------")
        finalizar_programa = True
