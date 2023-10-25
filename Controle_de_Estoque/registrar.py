class Registro:
    def __init__(self):
        self.produtos = {}
    
    def registrar(self, nome_produto, quantidade):
        if nome_produto in self.produtos:
            self.produtos[nome_produto] += quantidade
        else:
            self.produtos[nome_produto] = quantidade
    
        print(self.produtos)

registro = Registro()
for i in range(3):
    registro.registrar("macarão", 5)