"""
Este código simula el registro y manejo de cuentas bancarias a traves de un menu de opciones.
"""

import re
from os import system
from random import randint
import phonenumbers

#Base de datos local para almacenar clientes registrados al banco
clientes_registrados = []

#OOP del cliente con sus funciones
class Persona:
    def __init__(self, nombre, apellido, email, num_cel, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.num_cel = num_cel
        self.password = password

class Cliente(Persona):
    def __init__(self, nombre, apellido, email, num_cel, password, num_cuenta):
        super().__init__(nombre, apellido, email, num_cel, password)
        self.num_cuenta = num_cuenta

    def __str__(self):
        return f"\nCliente: {self.nombre} {self.apellido}\nEmail: {self.email}\nNum. Tel: {self.num_cel}\nNum. de cuenta: {self.num_cuenta}\n"
    
    #función para iniciar sesión con @staticmethod
        

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


#funcion para crear cliente
def crear_cliente():
    print("Siga las instrucciones correctamente para registrarse.\n")
    while True:
        nombre_cliente = input("Coloque su(s) nombre(s): ").upper()
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

    cliente = Cliente(nombre_cliente, apellido_cliente, email_cl, num_celular, passwd, numero_cuenta)
    return cliente


#funcion del menu inicial del programa
def inicio():
    system("cls")
    print("*" * 46)
    print(" Bienvenido a nuestro sistema bancario offline")
    print("*" * 46)

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
        print("\nNuestro menu de usuarios se encuentra en mantenimiento\nFavor de volver mas tarde.")
        volver_inicio()
        #verificar que la lista de clientes registrados no esté en 0
        #función para volver al inicio en caso de que lo esté
        
        #si ya existe un cliente registrado
        #ingresar numero de telefono y contraseña
        #función para verificar inicio de sesión
        #si encuentra los datos del cliente registrado, printear sus datos en inicio
        #función para el menú del cliente
        #función para salir del menu

    elif menu == 3:
        print("Gracias por su preferencia.")
        print("--------------------------")
        finalizar_programa = True
