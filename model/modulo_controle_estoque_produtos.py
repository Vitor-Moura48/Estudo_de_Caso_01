from . import *

class ModuloControleEstoqueProdutos:
    
    def __init__(self):
        self.arquivo_csv = "data/estoque.csv"
        
        if not os.path.exists(self.arquivo_csv):

            estoque = {
                "gasolina": 0,
                "alcool": 0,
                "diesel": 0,
                "energia_solar": 0
            }
            df = pd.DataFrame([estoque])

            df.to_csv(self.arquivo_csv, index=False, sep=';')
    
    # registrar a quantidade de produtos recebidos dos fornecedores
    def registrar(self, nome_produto, quantidade, compra):

        estoque = pd.read_csv(self.arquivo_csv)

        # se for um reabastecimento, adiciona o valor
        if compra:
            estoque[nome_produto] += quantidade  

        # se não, é uma venda, reduz a quantidade do produto
        else:
            estoque[nome_produto] -= quantidade
        
        estoque.to_csv(self.arquivo_csv, index=False)
    
    # emitir alertas quando os níveis de estoque atigem um limite mínimo
    def emitir_alerta(self, nome_produto):
        #print(f"{nome_produto}: Nível de estoque baixo!")
        print(f"{nome_produto}: Nível de estoque baixo!")
    
    # atualizar automaticamente o estoque após cada venda ou serviço prestado
    def update(self, vendas):

        estoque = pd.read_csv(self.arquivo_csv)

        # confere se houve alguma venda naquele 'loop'
        if vendas != {}:
            
            # percorre as informações de cada produto vendido
            for produto, quantidade in vendas.items():

                # registra a venda
                self.registrar(produto, quantidade, False)

                # confere se o estoque chegou em um nível mínimo
                if estoque[produto][0] < 5:
                    self.emitir_alerta(produto)
        

'''
controle_de_estoque.registrar("gasolina", 9, True)
controle_de_estoque.update({"gasolina": 2})
controle_de_estoque.registrar("diesel", 4, True)
controle_de_estoque.update({"gasolina": 3})
controle_de_estoque.update({"gasolina": 1})
'''