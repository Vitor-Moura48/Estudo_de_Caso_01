from . import *
from model.gerenciamento_automotivo import ModuloGerenciamentoAutomotivo

init()
cor_mensagem_erro = Fore.RED

modulo_gerenciamento_automotivo = ModuloGerenciamentoAutomotivo()

def run():
    while True:
        perguntas = [
            inquirer.List('opcao',
                          message='Selecione o que deseja fazer',
                          choices=[
                              ('1 - Coloque algo', '1'),
                              ('2 - Coloque algo', '2'),
                              ('3 - Sair do módulo', '3')
                          ])
        ]

        respostas = inquirer.prompt(perguntas)

        # Verifique se as respostas são nulas
        if respostas is None:
            raise KeyboardInterrupt
        
        opcao = respostas['opcao']

        # Aqui temos uma estrutura de decisão para cada opção do menu
        if opcao == '1':
           # O que faz
           pass

        elif opcao == '2':
            perguntas_registro = [
                inquirer.List('pergunt1', message='Pergunta1', choices=['gasolina', 'alcool', 'diesel', 'energia_solar']),
                inquirer.Text('pergunt2', message='Pergunta que tem que digitar'),
                inquirer.List('pergunt3', message='Pergunta tem que escolher', choices=['Compra', 'Venda']),
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            
            # Como pegar os dados inseridos
            pergunt2 = respostas_registro['pergunt2']
            print(f"Sua resposta é {pergunt2}")
            
        elif opcao == '3':
            print('Saindo do módulo de gerenciamento de serviços automotivos...')
            break