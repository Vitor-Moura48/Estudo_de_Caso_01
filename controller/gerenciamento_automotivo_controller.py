from . import *
from model.gerenciamento_automotivo import ModuloGerenciamentoAutomotivo

cor_mensagem_erro = Fore.RED

modulo_gerenciamento_automotivo = ModuloGerenciamentoAutomotivo()

def run():
    while True:
        perguntas = [
            inquirer.List('opcao',
                          message='Selecione o que deseja fazer',
                          choices=[
                              ('1 - Agendar o horário', '1'),
                              ('2 - Finalizar serviço ou desmarcar' , '2'),
                              ('3 - Acessar seu histórico', '3'),
                              ('4 - Sair do módulo', '4')
                          ])
        ]

        respostas = inquirer.prompt(perguntas)

        # Verifique se as respostas são nulas
        if respostas is None:
            raise KeyboardInterrupt
        
        opcao = respostas['opcao']

        # Aqui temos uma estrutura de decisão para cada opção do menu
        if opcao == '1':
            perguntas_agendamento = [
                inquirer.List('nome_mecanico', 
                    message='Escolha um mecânico:',
                    choices=['Anderson', 'Roberto', 'Fernando']
                ),
                inquirer.Text('horas', message='Digite a hora para agendar'),
            ]

            respostas_agendamento = inquirer.prompt(perguntas_agendamento)

            nome_mecanico = respostas_agendamento['nome_mecanico']
            horas = respostas_agendamento['horas']

            modulo_gerenciamento_automotivo.agendar(nome_mecanico, horas)
 
        
        elif opcao == '2':
            perguntas_feito_desmarcar = [
                inquirer.List('nome_mecanico', 
                    message='Escolha um mecânico',
                    choices=['Anderson', 'Roberto', 'Fernando']
                ),
                inquirer.Text('horas', message='Digite a hora que foi agendado'),
                inquirer.List('feito_desmarcar', 
                    message='Escolha uma opção',
                    choices=['Feito', 'Desmarcar']
                )
            ]

            respostas = inquirer.prompt(perguntas_feito_desmarcar)
            
            nome_mecanico = respostas['nome_mecanico']
            horas = respostas['horas']
            resposta = respostas['feito_desmarcar']

            modulo_gerenciamento_automotivo.feito_ou_desmarcar(nome_mecanico,horas,resposta)
            modulo_gerenciamento_automotivo.ordenado()
            modulo_gerenciamento_automotivo.desempenho()

        elif opcao == '3':
            perguntas_historico = [inquirer.Text('cliente', 
                                        message='Nome do cliente'),
                                        inquirer.Text('carro', 
                                        message='Modelo do carro')
                                         ]

            respostas = inquirer.prompt(perguntas_historico)

            cliente = respostas['cliente']
            carro = respostas['carro'] 
            
            modulo_gerenciamento_automotivo.historico(cliente,carro)    
        elif opcao == '4':
            print('Saindo do módulo de gerenciamento de serviços automotivos...')
            break