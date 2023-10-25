class ModuloControle:
    def __init__(self):
        self.produtos = {
            "gasolina": 0,
            "alcool": 0,
            "diesel": 0,
            "energia_solar": 0
        }
    
    # registrar a quantidade de produtos recebidos dos fornecedores
    def registrar(self, nome_produto, quantidade, compra):

        # se for um reabastecimento, adiciona o valor
        if compra:
            self.produtos[nome_produto] += quantidade
        # se não, é uma venda, reduz a quantidade do produto
        else:
            self.produtos[nome_produto] -= quantidade
    
    # emitir alertas quando os níveis de estoque atigem um limite mínimo
    def emitir_alerta(self, nome_produto):
        print(f"{nome_produto}: Nível de estoque baixo!")
    
    # atualizar automaticamente o estoque após cada venda ou serviço prestado
    def update(self, vendas):

        # confere se houve alguma venda naquele 'loop'
        if vendas != {}:
            
            # percorre as informações de cada produto vendido
            for produto, quantidade in vendas.items():

                # registra a venda
                self.registrar(produto, quantidade, False)

                # confere se o estoque chegou em um nível mínimo
                if self.produtos[produto] < 5:
                    self.emitir_alerta(produto)
        

controle_de_estoque = ModuloControle()


controle_de_estoque.registrar("gasolina", 9, True)


controle_de_estoque.update({"gasolina": 2})
controle_de_estoque.update({"gasolina": 2})
controle_de_estoque.update({"gasolina": 1})