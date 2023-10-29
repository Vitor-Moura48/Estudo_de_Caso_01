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

            df.to_csv(self.arquivo_csv, index=False, sep=';', header=None)
    
    # registrar a quantidade de produtos recebidos dos fornecedores
    def registrar(self, nome_produto, quantidade, compra):

        estoque = pd.read_csv(self.arquivo_csv)

        # se for um reabastecimento, adiciona o valor
        if compra:
            estoque[nome_produto] += quantidade  

        # se não, é uma venda, reduz a quantidade do produto
        else:
            estoque[nome_produto] -= quantidade
        
        # confere se o estoque chegou em um nível mínimo
        for produto in estoque.columns:
            if estoque[produto][0] < 5:
                self.emitir_alerta(produto)

        estoque.to_csv(self.arquivo_csv, index=False)
    
    # emitir alertas quando os níveis de estoque atigem um limite mínimo
    def emitir_alerta(self, nome_produto):
        print(f"{nome_produto}: Nível de estoque baixo!")
    
    def listar_estoque(self):
        estoque = pd.read_csv(self.arquivo_csv)
    
        for produto in estoque.columns:
            print(f"{produto}: {estoque[produto][0]}")
        print()

