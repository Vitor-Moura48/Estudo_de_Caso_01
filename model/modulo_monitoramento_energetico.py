import csv
import requests
import json

class ModuloMonitoramentoEnergetico:
    def __init__(self):
        self.arquivo_economia = "data/economia.csv"
        self.arquivo_producao_energia = "data/producao_energia.csv"
        url = f'https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key={API_KEY}&lat=40&lon=-105'

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
            producao = incidencia * area_placa_solar * eficiencia_placa_solar *30 # 30 é a quantidade de dias no mês
            producao_energia_solar[mes] = producao
        return producao_energia_solar
    
    def economia_solar_e_convencional(self, producao_energia_solar, fonte_convencional_energia):
        gasto_fontes = fonte_convencional_energia * 0.76 #taxa por KWH = 0.76
        tabela_custo = {}

        for mes, producao in producao_energia_solar.items():
            custo = producao * 0.76
            tabela_custo[mes] = custo - gasto_fontes

        #Salvando isso em um arquivo.csv
        with open(self.arquivo_economia, 'w', newline='') as arquivo_csv:
            print(' |mês|   |custo|')
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['mes', 'custo'])
            for mes, custo in tabela_custo.items():
                escritor.writerow([mes, custo])
                print([mes, custo])

    def salvar_em_arquivo_csv(self, producao_solar):
        with open(self.arquivo_producao_energia, 'w', newline='') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerow(['Mes', 'Producao Solar (kWh)'])
            for mes, producao in producao_solar.items():
                producao_solar_mes = producao_solar[mes]
                escritor.writerow([mes, f"{producao:.2f}"])

    def verificar_producao(self, producao_solar):
        for mes, producao in producao_solar.items():
            if producao < 15000:  # Limiar para baixa produção 
                print(f"ALERTA: Baixa produção de energia no mês {mes} ({producao:.2f} kWh)")

    def detectar_falha(self, producao_solar):
        if None in producao_solar.values():
            print("ALERTA: Falha na obtenção dos dados de produção de energia.")

# Chave da API
API_KEY = 'h1sZGSoHQjEe3MaoZ3GxMPeYPfLVMjnHd8fbphfD'

url = f'https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key={API_KEY}&lat=40&lon=-105'

