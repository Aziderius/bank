import re
from os import system
from random import randint
import phonenumbers
from classes_bank import *


#Función para validar contraseña usando Regular expresions.
def validar_contrasenia(contrasenia):
    if not re.search(r'[a-z]', contrasenia):
        return False
    
    if not re.search(r'[A-Z]', contrasenia):
        return False
    
    if not re.search(r'[0-9]', contrasenia):
        return False
    
    if not re.search(r'[!"#$%&/()=?¡¿\-.,]', contrasenia):
        return False
    
    if len(contrasenia) < 6:
        return False
    
    return True

#Funcion para validar correo electrónico usando regular expresions.
def validar_correo(email):
    if re.match(r'^[a-zA-Z0-9._%+-]+@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$', email):
        return True
    

#Funcion para validar telefono usando libreria Phonenumber    
def validar_telefono(numero_telefono):
    numero_telefono = "+52" + numero_telefono  # Agregamos la lada directamente
    try:
        parsed_numero = phonenumbers.parse(numero_telefono, None)

        if phonenumbers.is_valid_number(parsed_numero):    
            return phonenumbers.format_number(parsed_numero, phonenumbers.PhoneNumberFormat.E164)  # Retornamos el número válido
        
    except phonenumbers.phonenumberutil.NumberParseException:
        print("Número de celular inválido. Inténtelo nuevamente.")


#Funcion para validar nombre/nombres del usuario
def validar_nombre(nombre_cliente):
    nombres = nombre_cliente.split()

    if all(nombre.isalpha() for nombre in nombres):
        return nombres


#Funcion para validar que solo se coloque 1 apellido y que no contenga numeros ni simbolos
def validar_apellido(nombre):
    if nombre.isalpha():
        return nombre


#funcion para crear cliente
def crear_cliente():
    print("Siga las instrucciones correctamente para registrarse.\n")
    while True:
        nombre_cliente = input("Coloque su(s) nombre(s): ").upper()
        if validar_nombre(nombre_cliente):
            break
        print("Los nombres solo deben contener letras.")

    while True:
        apellido1 = input("Ingrese su apellido paterno: ").upper()
        if validar_apellido(apellido1):
            break    
        print("Favor de colocar tu apellido paterno correctamente")

    while True:
        apellido2 = input("Ingrese su apellido materno: ").upper()
        if validar_apellido(apellido2):
            break
        print("Favor de colocar tu apellido materno correctamente")

    apellido_cliente = apellido1 + " " + apellido2

    while True:
        email_cl = input("Ingrese su email: ")
        if validar_correo(email_cl):
            break
        print("Ingrese un correo electrónico válido.")

    while True:
        num_celular = input("Ingrese un número de celular: ")
        if validar_telefono(num_celular):
            break
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
        if validar_contrasenia(passwd):
            break
        print("\nPor favor, ingresa una contraseña válida.\n")

    numero_cuenta = randint(1000000000,9999999999)

    cliente = Cliente(nombre_cliente, apellido_cliente, email_cl, num_celular, passwd, numero_cuenta)
    return cliente

#funcion del menu inicial del programa
def inicio():
    system("cls")
    print("*" * 50)
    print(" Bienvenido a nuestro sistema bancario offline. ")
    print("*" * 50)

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


def volver_inicio():
    eleccion_regresar = "x"

    while eleccion_regresar.lower() != "s":
        eleccion_regresar = input("\n Presiona s para salir: ")