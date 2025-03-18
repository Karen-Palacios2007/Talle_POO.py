#crear clase
class Cliente:
    def __init__(self):
        self.nomb_cliente=""
        self.apell_cliente=""

    #Se crean metodos Get y Set para atributos

    def get_nombre(self):
        return self.nomb_cliente
    def get_apellido(self):
        return self.apell_cliente
    def set_nombre(self,dato_nombre):
        self.nomb_cliente=dato_nombre
    def set_apell(self,dato_apellido):
        self.apell_cliente=dato_apellido
    
    #Se crean metodos normales de la clase
    def tomar_datos(self):
        self.nomb_cliente=input("Digite el nombre de cliente: ")
        self.apell_cliente=input("Digite el Apellido de cliente: ")
        
    def procesar_datos(self):
        aux=self.nomb_cliente+ " " +self.apell_cliente
    def mostrar_datos(self):
        print(f"Nombre cliente: {self.nomb_cliente} - Apellido cliente: {self.apell_cliente}")
    def hacer_saludo(self,dato_saludo):
        print(f"{dato_saludo} : {self.nomb_cliente} {self.apell_cliente}")

#el contructor no retorna