import inquirer
from model.modulo_monitoramento_energetico import ModuloMonitoramentoEnergetico

modulo_monitoramento_energetico = ModuloMonitoramentoEnergetico()

def run():
    while True:
        perguntas = [
            inquirer.List('opcao',
                          message='Selecione o que deseja fazer:',
                          choices=[
                              ('1 - Leituras em tempo real da energia solar', '1'),
                              ('2 - Dados econômicos da energia', '2'),
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
            modulo_monitoramento_energetico.obter_incidencia_solar
            modulo_monitoramento_energetico.calcular_producao_energia_solar
            modulo_monitoramento_energetico.verificar_producao
            modulo_monitoramento_energetico.detectar_falha
        
        elif opcao == '2':
            modulo_monitoramento_energetico.economia_solar_e_convencional

        elif opcao == '3':
            print('Saindo do módulo de monitoramento energético...')
            break