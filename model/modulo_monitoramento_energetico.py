import csv
import requests
import json

class ModuloMonitoramentoEnergetico:
    def __init__(self, api_key):
        self.api_key = api_key

    def obter_incidencia_solar(self, url):
        try:
            response = requests.get(url)
            data = response.json()
            inc_solar = data['outputs']['avg_dni']['monthly']
            return inc_solar

        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar resposta JSON: {e}")
            return None

    def calcular_producao_energia_solar(self, incidencia_solar, area_placa_solar, eficiencia_placa_solar):
        producao_energia_solar = {}
        for mes, incidencia in incidencia_solar.items():
            producao = incidencia * area_placa_solar * eficiencia_placa_solar
            producao_energia_solar[mes] = producao
        return producao_energia_solar

    def salvar_em_arquivo_csv(self, producao_solar):
        with open('producao_energia.csv', 'w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Mês', 'Produção Solar (kWh)'])
            for mes, producao in producao_solar.items():
                producao_solar_mes = producao_solar[mes]
                escritor.writerow([mes, f"{producao:.2f}"])

    def verificar_producao(self, producao_solar):
        for mes, producao in producao_solar.items():
            if producao < 520:  # Limiar para baixa produção 
                print(f"ALERTA: Baixa produção de energia no mês {mes} ({producao:.2f} kWh)")

    def detectar_falha(self, producao_solar):
        if None in producao_solar.values():
            print("ALERTA: Falha na obtenção dos dados de produção de energia.")

# Chave da API
API_KEY = 'h1sZGSoHQjEe3MaoZ3GxMPeYPfLVMjnHd8fbphfD'

url = f'https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key={API_KEY}&lat=40&lon=-105'

gerenciamento = ModuloMonitoramentoEnergetico(API_KEY)
incidencia_solar = gerenciamento.obter_incidencia_solar(url)

if incidencia_solar:
    area_placa_solar = 600
    eficiencia_placa_solar = 0.15  # Eficiência da placa solar (exemplo)

    producao_energia_solar = gerenciamento.calcular_producao_energia_solar(incidencia_solar, area_placa_solar, eficiencia_placa_solar)
    
    gerenciamento.salvar_em_arquivo_csv(producao_energia_solar)
    gerenciamento.verificar_producao(producao_energia_solar)
    gerenciamento.detectar_falha(producao_energia_solar)
    
    print("Produção de Energia Solar (kWh/mês):")
    for mes, producao in producao_energia_solar.items():
        print(f"Mês {mes}: {producao:.2f} kWh")

    print("Dados salvos em 'producao_energia.csv'")
else:
    print("Não foi possível obter dados de incidência solar.")
