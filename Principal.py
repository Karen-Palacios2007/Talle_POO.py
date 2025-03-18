from Cliente import Cliente
from Saludo import Saludo

objCliente=Cliente()
objSaludo=Saludo()

objCliente.tomar_datos()
aux_mensaje=objSaludo.hacer_saludo_formal()
objCliente.hacer_saludo(aux_mensaje)