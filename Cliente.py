class Cliente:
    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.email = email
        self.cpf = cpf
    
    def getNome(self):
        return self.nome

    