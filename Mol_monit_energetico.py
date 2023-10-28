import csv
import requests
import json

class Moduloenergetico:
    def __init__(self, api_key):
        self.api_key = api_key

    def obter(self, url):
        try:
            response = requests.get(url)
            data = response.json()
            inc_solar = data['outputs']['avg_dni']['monthly']

            with open('incidencia_solar.csv', 'w', newline='') as arquivo_csv:
                escritor = csv.writer(arquivo_csv)
                escritor.writerow(['chave', 'valor'])
                for chave, valor in inc_solar.items():
                    escritor.writerow([chave, valor])

            with open('incidencia_solar.csv', 'r') as arquivo:
                leitor = csv.reader(arquivo)
                for linha in leitor:
                    print(linha)

        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
        except json.JSONDecodeError as e:
            print(f"Erro ao decodificar resposta JSON: {e}")

# Chave da API
API_KEY = 'h1sZGSoHQjEe3MaoZ3GxMPeYPfLVMjnHd8fbphfD'

url = f'https://developer.nrel.gov/api/solar/solar_resource/v1.json?api_key={API_KEY}&lat=40&lon=-105'

gerenciamento = Moduloenergetico(API_KEY)
gerenciamento.obter(url)
