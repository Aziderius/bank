from functions_bank import *


#Funcion del menu de la cuenta del cliente (ya iniciada la sesión)
def menu_cliente():
    print(cliente_iniciado)
    opcion_cliente = "x"
    while not opcion_cliente.isnumeric() or int(opcion_cliente) not in range(1,3):
        print("\nElige una categoría de nuestro menu de opciones ")
        print('''
                [1] - Ver datos de la cuenta
                [2] - Cerrar Sesion
                ''')
        opcion_cliente = input("Elige el número 1 o 2 segun el menú: ")
    return int(opcion_cliente)


#Programa
finalizar_programa = False

while not finalizar_programa:
    menu = inicio()
    if menu == 1:
        mi_cliente = crear_cliente()
        # Verificar si el cliente ya está registrado
        cliente_existente = verificar_existencia_cliente(mi_cliente)
        if cliente_existente:
            print("Ya existe un cliente con los datos anteriormente registrados")
        else:
            insertar_cliente(mi_cliente)
            print("\nSu registro ha sido exitoso!\n")
        
        volver_inicio()
        
    elif menu == 2:
        num_cel = input("Ingrese su numero de telefono: ")
        password = input("Ingrese su contraseña: ")
        cliente_iniciado = Cliente.iniciar_sesion(num_cel, password)
        if cliente_iniciado:
            print(f"\nInicio de sesión exitoso como {cliente_iniciado.nombre} {cliente_iniciado.apellido}")

            salida = False
            while not salida:
                menu_bancario = menu_cliente()
                if menu_bancario == 1:
                    print(f"\n¡Hola! {cliente_iniciado.nombre} {cliente_iniciado.apellido}")
                    print(cliente_iniciado)   
                    volver_inicio()
                elif menu_bancario == 2:
                    salida = True   
        else:
            print("Credenciales incorrectas. Intente nuevamente o cree una cuenta.")
            volver_inicio()
        
    elif menu == 3:
        print("Gracias por elegir nuestro Banco")
        print("--------------------------------")
        finalizar_programa = True
        cerrar_conexion()
