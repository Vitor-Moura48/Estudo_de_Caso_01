import inquirer
from colorama import init, Fore, Style

# Inicialize o colorama
init()

# Defina as cores que você deseja usar
cor_titulo = Fore.GREEN
cor_pergunta = Fore.WHITE
cor_resposta = Fore.MAGENTA

# Imprima o título com a cor personalizada
print(f'{cor_titulo}╔══════════════════════════════════════════════════════════╗')
print(f'║                                                          ║')
print(f'║          🌿 Sistema de Informação EcoEnergy 🌿           ║')
print(f'║                                            v1.0.0        ║')
print(f'║                                                          ║')
print(f'╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n')

# Crie uma pergunta com a cor personalizada
pergunta = [
    inquirer.List('opcao',
                  message=f'Selecione o módulo que deseja acessar',
                  choices=[
                      (f'{cor_pergunta}1 - Módulo de Controle de Estoque de Produtos{Style.RESET_ALL}', '1'),
                      (f'{cor_pergunta}2 - Módulo de Gerenciamento de Serviços Automotivos{Style.RESET_ALL}', '2'),
                      (f'{cor_pergunta}3 - Módulo de Gestão de Mercearia{Style.RESET_ALL}', '3'),
                      (f'{cor_pergunta}4 - Módulo de Monitoramento Energético{Style.RESET_ALL}', '4'),
                      (f'{cor_pergunta}5 - Módulo de Loja de Conveniência{Style.RESET_ALL}', '5')
                  ])
]

# Faça a pergunta e obtenha as respostas
respostas = inquirer.prompt(pergunta)
opcao = respostas['opcao']

# Imprima a resposta com a cor personalizada
print(f'{cor_titulo}=>{Style.RESET_ALL} Você selecionou o môdulo: {cor_titulo}{opcao}{Style.RESET_ALL}\n')