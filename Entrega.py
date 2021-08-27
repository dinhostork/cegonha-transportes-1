class Entrega:
    def __init__(self, dataDeEntrega, descricao, endereco, cliente):
        self.dataDeEntrega = dataDeEntrega
        self.descricao = descricao
        self.endereco = endereco
        self.cliente = cliente
    
    def getCliente(self):
        return self.cliente
    
