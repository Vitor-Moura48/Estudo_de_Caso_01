import csv

class ModuloGerenciamento:
    def __init__(self):
        self.mecanicos = [['Anderson'],['roberto'],['junior']]  
        self.carregar_dados()  

    def carregar_dados(self):
        try:
            with open('arquivo.csv' ,'r', newline='') as arquivo_csv:
                leitor = csv.reader(arquivo_csv)
        except FileNotFoundError:
            print('Arquivo não encontrado')

    def salvar_dados(self):
        with open('arquivo.csv', 'w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerows(self.mecanicos)

    def agendar(self, nome, horas):
        # o mecânico existe:
        for mec in self.mecanicos:
            if mec[0] == nome:
                # Cria uma nova lista contendo as horas
                horas_lista = [horas]
                mec.extend(horas_lista)
                break
        else:
            # Se o mecânico não existe
            novo_mecanico = [nome, horas]
            self.mecanicos.append(novo_mecanico)
        self.salvar_dados()  
    
    def feito_ou_desmarcar(self, nome, horas,servico):
            if servico:
                print("Serviço feito!")
            else:
                print('Serviço desmarcado')
            for mec in self.mecanicos:
                if mec[0] == nome:
                    # Verifica se as horas de trabalho existem na lista do mecânico
                    if horas in mec[1:]:
                        mec.remove(horas)
                    break
            self.salvar_dados()  

gerenciamento = ModuloGerenciamento()

