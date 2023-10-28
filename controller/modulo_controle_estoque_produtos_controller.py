import inquirer
from model.modulo_controle_estoque_produtos import ModuloControleEstoqueProdutos

modulo_controle_estoque_produtos = ModuloControleEstoqueProdutos()

def run():
    while True:
        perguntas = [
            inquirer.List('opcao',
                          message='Selecione o que deseja fazer:',
                          choices=[
                              ('1 - Adicionar algo aqui', '1'),
                              ('2 - Registrar', '2'),
                              ('3 - Sair do módulo', '3')
                          ])
        ]

        respostas = inquirer.prompt(perguntas)
        opcao = respostas['opcao']

        # Aqui temos uma estrutura de decisão para cada opção do menu
        if opcao == '1':
            modulo_controle_estoque_produtos.run()

        elif opcao == '2':
            perguntas_registro = [
                inquirer.Text('nome', message='Digite o nome do produto:'),
                inquirer.Text('quantidade', message='Digite a quantidade do produto:')
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            
            nome = respostas_registro['nome']
            quantidade = respostas_registro['quantidade']
            modulo_controle_estoque_produtos.registrar(nome, quantidade)
        elif opcao == '3':
            print('Saindo do módulo de controle de estoque de produtos...')
            break