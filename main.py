from Cliente import Cliente
from Entrega import Entrega

cliente1 = Cliente("Cleber", "085645864598", "cleber@lemos.com")
cliente2 = Cliente("Paulo", "01111111118", "paulo@lemos.com")

pacote1 = Entrega("27-10-21", "Secreto", "Rua A, Centro, Salvador", cliente1)
pacote2 = Entrega("30-10-21", "Bicicleta", "Rua A, Centro, Salvador", cliente2)

print(pacote2.cliente.getNome())