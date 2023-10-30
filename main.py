import inquirer
from colorama import init, Fore, Style

init()

# Definição de cores
cor_titulo = Fore.GREEN
cor_pergunta = Fore.WHITE
cor_resposta = Fore.MAGENTA
cor_mensagem = Fore.YELLOW
cor_mensagem_erro = Fore.RED

try:
    while True:
        print(f'{cor_titulo}╔══════════════════════════════════════════════════════════╗')
        print(f'║                                                          ║')
        print(f'║          🌿 Sistema de Informação EcoEnergy 🌿           ║')
        print(f'║                                            v1.0.0        ║')
        print(f'║                                                          ║')
        print(f'╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n')

        pergunta = [
            inquirer.List('opcao',
                        message=f'Selecione o módulo que deseja acessar',
                        choices=[
                            (f'1 - Módulo de Controle de Estoque de Produtos', '1'),
                            (f'2 - Módulo de Gerenciamento de Serviços Automotivos', '2'),
                            (f'3 - Módulo de Gestão de Mercearia', '3'),
                            (f'4 - Módulo de Monitoramento Energético', '4'),
                            (f'5 - Módulo de Loja de Conveniência', '5'),
                            (f'6 - Encerrar a Sessão no Sistema', '6')
                        ])
        ]

        respostas = inquirer.prompt(pergunta)

        # Verifique se as respostas são nulas
        if respostas is None:
            raise KeyboardInterrupt
        
        opcao = respostas['opcao']

        print(f'{cor_titulo}=>{Style.RESET_ALL} Você selecionou a opção: {cor_titulo}{opcao}{Style.RESET_ALL}\n')

        match opcao:
            case '1':
                from controller.modulo_controle_estoque_produtos_controller import run
                run()
            case '2':
                from controller.gerenciamento_automotivo_controller import run
                run()
            case '3':
                from controller.caixa_bomba import run
                run()
            case '4':
                from controller.modulo_monitoramento_energetico_controller import run
                run()
            case '5':
                print("Tese")
            case '6':
                print(f'{cor_titulo}👋 {cor_mensagem}Encerrando a sessão no sistema...{Style.RESET_ALL}')
                break
            case _:
                print(f'{cor_mensagem_erro}❌ Ocorreu um erro estranho{Style.RESET_ALL}\n')

except KeyboardInterrupt:
    print(f'{cor_mensagem_erro}❌ O Sistema foi interrompido forçadamente pelo usuário{Style.RESET_ALL}\n')