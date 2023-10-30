import csv

class ModuloGerenciamentoAutomotivo:
    def __init__(self):
        self.arquivo_mecanico = "data/mecanicos.csv"
        self.arquivo_registros = "data/registros.csv"
        self.arquivo_mecanico = 'data/medias_por_clientes.csv'
        self.mecanicos = [['Anderson'],['Roberto'],['Fernando']]
        self.registro = []
        self.media = []
        self.carregar_dados()  

    def carregar_dados(self):
        # verificação se existe o arquivo dos mecânicos:
        try:
            with open(self.arquivo_mecanico ,'r', newline='') as arquivo_csv:
                leitor = csv.reader(arquivo_csv)
        except FileNotFoundError:
            print('Arquivo não encontrado')

    def salvar_dados(self):
        # cria os dados dos mecânicos e os horários:
        with open(self.arquivo_mecanico, 'w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Mecanico', 'Horas marcadas'])
            escritor.writerows(self.mecanicos)

    def salvar_dados2(self):
        # cria os dados do registro:
        with open(self.arquivo_registros, 'w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Mecanico','Cliente','Modelo do Carro','Modelo do carro', 'Pecas', 'Tempo', 'Dia', 'Satifascao do cliente',])
            escritor.writerows(self.registro)

    def agendar(self, nome, horas):
        # Verifica se o mecânico existe:
        mec_existente = None
        for mec in self.mecanicos:
            if mec[0] == nome:
                mec_existente = mec
                break

        if mec_existente:
            # Verifica se o horário já existe no mecânico:
            if horas in mec_existente[1:]:
                print("Horário indisponível")
            else:
                # Se o horário não existe, adicione-o ao mecânico existente
                mec_existente.append(horas)
                print(f"Horário agendado com sucesso para {nome} às {horas}.")
        else:
            # Se o mecânico não existe, crie um novo mecânico com as horas
            novo_mecanico = [nome, horas]
            self.mecanicos.append(novo_mecanico)
            print(f"Novo mecânico {nome} criado com horário às {horas}.")
        
        self.salvar_dados()

    
    def feito_ou_desmarcar(self, nome, horas,servico):
            if servico == 'Feito':
                print("Serviço feito!")
                
                cliente_nome = input("Nome do cliente*: ")
                modelo = input("Modelo do carro*: ")
                registro = input('Registro detalhado*: ')
                pecas = input("Peças utilizadas*: ")

                tempo = float(input("Tempo de execução: "))
                dia = int(input("Dia do serviço: "))
                satisfacao = int(input("Nível de satisfação (0 a 5): "))

                while not (0 <= satisfacao <= 5):
                    print("O nível de satisfação deve estar entre 0 e 5.")
                    satisfacao = int(input("Nível de satisfação (0 a 5): "))
                
                detalhado = [nome,cliente_nome,modelo,registro,pecas,tempo,dia,satisfacao]
                
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
            with open(self.arquivo_registros ,'r', newline='') as arquivo_csv:
                leitor = csv.reader(arquivo_csv)
                next(leitor)
                tempo = 0
                satisfacao = 0
                quant_mecanicos = 0
                for linha in leitor:
                    tempo += float(linha[5])
                    satisfacao += float(linha[7])
                    
                    quant_mecanicos += 1
                    
                media_tempo = tempo/quant_mecanicos
                media_satisfacao = satisfacao/quant_mecanicos

                lista = [media_tempo,media_satisfacao]    
                
                self.media.append(lista)
                with open(self.arquivo_media_cliente, 'w', newline='') as arquivo_csv3:
                    escritor = csv.writer(arquivo_csv3)
                    escritor.writerow(['Media-Execucao','Media-Satisfacao'])
                    escritor.writerows(self.media)

        except FileNotFoundError:
            print('Arquivo não encontrado')   
    
    def historico(self, cliente, veiculo):
        try:
            with open(self.arquivo_registros, 'r', newline='') as arquivo_csv:
                leitor = csv.reader(arquivo_csv)
                for linha in leitor:
                    if linha[1] == cliente and linha[2] == veiculo:
                        print(f"Nome: {linha[1]}\nModelo do Carro: {linha[2]}\nRegistro detalhado: {linha[3]}\nPeças: {linha[4]}\nTempo: {linha[5]}\nDia: {linha[6]}\nSatisfação do Cliente: {linha[7]}")
        except FileNotFoundError:
            print("Arquivo não encontrado")


