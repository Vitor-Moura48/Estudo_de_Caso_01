import inquirer
from model.modulo_controle_estoque_produtos import ModuloControleEstoqueProdutos

modulo_controle_estoque_produtos = ModuloControleEstoqueProdutos()

def run():
    while True:
        perguntas = [
            inquirer.List('opcao',
                          message='Selecione o que deseja fazer',
                          choices=[
                              ('1 - Listar estoque', '1'),
                              ('2 - Registrar', '2'),
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
            modulo_controle_estoque_produtos.listar_estoque()

        elif opcao == '2':
            perguntas_registro = [
                inquirer.List('nome', message='Digite o nome do produto', choices=['gasolina', 'alcool', 'diesel', 'energia_solar']),
                inquirer.Text('quantidade', message='Digite a quantidade do produto'),
                inquirer.List('compra_venda', message='Escolha uma ação', choices=['Compra', 'Venda']),
            ]
            respostas_registro = inquirer.prompt(perguntas_registro)
            
            nome = respostas_registro['nome']
            try:
                quantidade = float(respostas_registro['quantidade'])
                compra_venda = respostas_registro['compra_venda'] == "Compra"

                modulo_controle_estoque_produtos.registrar(nome, quantidade, compra_venda)
            except ValueError:
                print("Preencha os valores corretamente! \n")
            
        elif opcao == '3':
            print('Saindo do módulo de controle de estoque de produtos...')
            break