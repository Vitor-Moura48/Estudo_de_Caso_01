import csv

class ModuloGerenciamento:
    def __init__(self):
        self.mecanicos = [['Anderson'],['roberto'],['junior']]
        self.registro = []
        self.media = []
        self.carregar_dados()  

    def carregar_dados(self):
        # verificação se existe o arquivo dos mecânicos:
        try:
            with open('Mecanicos.csv' ,'r', newline='') as arquivo_csv:
                leitor = csv.reader(arquivo_csv)
        except FileNotFoundError:
            print('Arquivo não encontrado')

    def salvar_dados(self):
        # cria os dados dos mecânicos e os horários:
        with open('Mecanicos.csv', 'w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Mecanico', 'Horas marcadas'])
            escritor.writerows(self.mecanicos)

    def salvar_dados2(self):
        # cria os dados do registro:
        with open('Registros.csv', 'w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Registro', 'Pecas', 'Tempo', 'Dia', 'Satifascao do cliente'])
            escritor.writerows(self.registro)

    def agendar(self, nome, horas):
        # o mecânico existe:
            mec_existente =  None
            for mec in self.mecanicos:
                if mec[0] == nome:
                    mec_existente = mec
                    break

            if mec_existente:
            # Verifica se o horário já existe no mecânico:
                if horas in mec_existente[1:]:
                    return print("Horário indisponível")
            else:
                mec_existente.append(horas)
            if mec[0] == nome:
                # Cria uma nova lista contendo as horas:
                horas_lista = [horas]
                mec.extend(horas_lista)
            
            else:
            # Se o mecânico não existe:
                return print("Mecânico inexistente na nossa lista")
            self.salvar_dados()  
    
    def feito_ou_desmarcar(self, nome, horas,servico):
            if servico:
                print("Serviço feito!")
                
                registro = input("Registro detalhado: ")
                pecas = input("Peças utilizadas: ")
                tempo = float(input("Tempo de execução: "))
                dia = int(input("Dia do serviço: "))
                cliente = int(input("Nível de satifasção: "))
                
                detalhado = [nome,registro,pecas,tempo,dia,cliente]
                
                self.registro.append(detalhado)
                self.salvar_dados2()

            else:
                print('Serviço desmarcado')
            for mec in self.mecanicos:
                if mec[0] == nome:
                    # Verifica se as horas de trabalho existem na lista do mecânico
                    if horas in mec[1:]:
                        mec.remove(horas)
                    break
            self.salvar_dados()

    def desempenho(self):
        try:
            with open('Registros.csv' ,'r', newline='') as arquivo_csv:
                leitor = csv.reader(arquivo_csv)
                next(leitor)
                tempo = 0
                satisfacao = 0
                quant_mecanicos = 0
                for linha in leitor:
                    tempo += float(linha[3])
                    satisfacao += float(linha[5])
                    
                    quant_mecanicos += 1
                    
                media_tempo = tempo/quant_mecanicos
                media_satisfacao = satisfacao/quant_mecanicos

                lista = [media_tempo,media_satisfacao]    
                
                self.media.append(lista)
                with open('Medias_por_clientes.csv', 'w', newline='') as arquivo_csv3:
                    escritor = csv.writer(arquivo_csv3)
                    escritor.writerow(['Media-Execucao','Media-Satisfacao'])
                    escritor.writerows(self.media)

        except FileNotFoundError:
            print('Arquivo não encontrado')   
    
gerenciamento = ModuloGerenciamento()

gerenciamento.agendar('Anderson','9')
gerenciamento.agendar('Anderson','10')
gerenciamento.agendar('roberto','10')
gerenciamento.agendar('roberto','12')
gerenciamento.agendar('junior','12')
gerenciamento.agendar('junior','13')
gerenciamento.feito_ou_desmarcar('Anderson','10',True)
gerenciamento.feito_ou_desmarcar('roberto','12',True)
gerenciamento.feito_ou_desmarcar('junior','13',True)
gerenciamento.desempenho()
