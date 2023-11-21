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
                              ('3 - Dados econômicos da energia ordenados', '3'),
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
            API_KEY = 'h1sZGSoHQjEe3MaoZ3GxMPeYPfLVMjnHd8fbphfD'

            url = f'https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key={API_KEY}&lat=40&lon=-105'

            
            incidencia_solar = modulo_monitoramento_energetico.obter_incidencia_solar(url)

            if incidencia_solar:
                area_placa_solar = 600 #300 placas de 2m quadrados.
                eficiencia_placa_solar = 0.15  # Eficiência da placa solar 
                fonte_convencional_energia = 15000 # Energia em KWH

                producao_energia_solar = modulo_monitoramento_energetico.calcular_producao_energia_solar(incidencia_solar, area_placa_solar, eficiencia_placa_solar)
                
                modulo_monitoramento_energetico.salvar_em_arquivo_csv(producao_energia_solar)
                modulo_monitoramento_energetico.verificar_producao(producao_energia_solar)
                modulo_monitoramento_energetico.detectar_falha(producao_energia_solar)
                
                print("Produção de Energia Solar (kWh/mês):")
                for mes, producao in producao_energia_solar.items():
                    print(f"Mês {mes}: {producao:.2f} kWh")

                print("Dados salvos em 'producao_energia.csv'")
            else:
                print("Não foi possível obter dados de incidência solar.")

        
        elif opcao == '2':
            API_KEY = 'h1sZGSoHQjEe3MaoZ3GxMPeYPfLVMjnHd8fbphfD'

            url = f'https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key={API_KEY}&lat=40&lon=-105'

            incidencia_solar = modulo_monitoramento_energetico.obter_incidencia_solar(url)

            if incidencia_solar:
                area_placa_solar = 600 #300 placas de 2m quadrados.
                eficiencia_placa_solar = 0.15  # Eficiência da placa solar 
                fonte_convencional_energia = 15000 # Energia em KWH

                producao_energia_solar = modulo_monitoramento_energetico.calcular_producao_energia_solar(incidencia_solar, area_placa_solar, eficiencia_placa_solar)

                modulo_monitoramento_energetico.economia_solar_e_convencional(producao_energia_solar, fonte_convencional_energia)

        elif opcao == '3':
            API_KEY = 'h1sZGSoHQjEe3MaoZ3GxMPeYPfLVMjnHd8fbphfD'

            url = f'https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key={API_KEY}&lat=40&lon=-105'

            incidencia_solar = modulo_monitoramento_energetico.obter_incidencia_solar(url)

            if incidencia_solar:
                area_placa_solar = 600 #300 placas de 2m quadrados.
                eficiencia_placa_solar = 0.15  # Eficiência da placa solar 
                fonte_convencional_energia = 15000 # Energia em KWH


                producao_energia_solar = modulo_monitoramento_energetico.calcular_producao_energia_solar(incidencia_solar, area_placa_solar, eficiencia_placa_solar)
                
                modulo_monitoramento_energetico.ordenado()

        elif opcao == '4':
            print('Saindo do módulo de monitoramento energético...')
            break