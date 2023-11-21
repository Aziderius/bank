#Base de datos local para almacenar clientes registrados al banco
clientes_registrados = []

#OOP del cliente con sus funciones de depositar y retirar, ademas del inicio de sesión
class Cliente:
    def __init__(self, nombre, apellido, email, num_cel, password, num_cuenta):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.num_cel = num_cel
        self.password = password
        self.num_cuenta = num_cuenta

    def __str__(self):
        return f"\nCliente: {self.nombre} {self.apellido}\nEmail: {self.email}\nNum. Tel: {self.num_cel}\nNum. de cuenta: {self.num_cuenta}\n"
    

    @staticmethod
    def iniciar_sesion(num_cel, password):
        for cliente in clientes_registrados:
            if cliente.num_cel == num_cel and cliente.password == password:
                return cliente
            
        print("Datos incorrectos.")
        return None