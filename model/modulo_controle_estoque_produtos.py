import pandas as pd
import os
from colorama import init, Fore, Style
import csv

init()
cor_mensagem_erro = Fore.RED
cor_estoque = Fore.GREEN

class ModuloControleEstoqueProdutos:
    
    def __init__(self):
        self.arquivo_csv = "data/estoque.csv"
        
        if not os.path.exists(self.arquivo_csv):

            estoque = {
                "gasolina": 2,
                "alcool": 1,
                "diesel": 4,
                "energia_solar": 3
            }
            df = pd.DataFrame([estoque])

            df.to_csv(self.arquivo_csv, index=False)

    def ordenar(self):
        estoque = pd.read_csv(self.arquivo_csv)
        ordenado = []
        for produto in estoque.columns:    
            ordenado.insert(0, produto)

            if len(ordenado) != 1:
                index = 0
                
                while estoque[produto][0] > estoque[ordenado[index + 1]][0]:
                    aux = ordenado[index]
                    ordenado[index]= ordenado[index + 1]
                    ordenado[index + 1] = aux
                    if index < len(ordenado) - 2:
                        index += 1
                    else:
                        break

        novo = pd.DataFrame({'inicializar':[0]})
        for produto in ordenado:
            novo[produto] = estoque[produto][0]  
        novo = novo.drop('inicializar', axis=1)

        novo.to_csv(self.arquivo_csv, index=False)

    # registrar a quantidade de produtos recebidos dos fornecedores
    def registrar(self, nome_produto, quantidade, compra):

        estoque = pd.read_csv(self.arquivo_csv)

        # se for um reabastecimento, adiciona o valor
        if compra:
            estoque[nome_produto] += quantidade  

        # se não, é uma venda, reduz a quantidade do produto
        else:
            if estoque[nome_produto][0] >= quantidade:
                estoque[nome_produto] -= quantidade
            else:
                print(f"{cor_mensagem_erro} Não é possível fazer a venda! Estoque indisponível {Style.RESET_ALL}\n")
        
        # confere se o estoque chegou em um nível mínimo
        for produto in estoque.columns:
            if estoque[produto][0] < 5:
                self.emitir_alerta(produto)

        estoque.to_csv(self.arquivo_csv, index=False)

    # emitir alertas quando os níveis de estoque atigem um limite mínimo
    def emitir_alerta(self, nome_produto):
        print(f"{cor_mensagem_erro}{nome_produto}: Nível de estoque baixo!{Style.RESET_ALL}")
    
    def listar_estoque(self):
        
        self.ordenar()
        estoque = pd.read_csv(self.arquivo_csv)
        for produto in estoque.columns:
            print(f"{cor_estoque}{produto}: {estoque[produto][0]}{Style.RESET_ALL}")
        print()
