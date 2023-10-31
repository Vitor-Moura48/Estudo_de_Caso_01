class ModuloRelatorio:
    def __init__(self):
        pass
    
    def gerar_relatorio_vendas(self):
      vendas_diarias = [1500, 1700, 1800, 1600, 1750]
      vendas_semanais = sum(vendas_diarias)
      vendas_mensais = vendas_semanais * 4
      return {
          "vendas_diarias": vendas_diarias,
          "vendas_semanais": vendas_semanais,
          "vendas_mensais": vendas_mensais,
      }

    # Função para gerar relatórios de desempenho de serviços automotivos
    def gerar_relatorio_desempenho_servicos(self):
        tempos_execucao = [30, 45, 60, 35, 40]
        satisfacao_clientes = [4, 5, 4, 5, 3]
        tempo_medio_execucao = sum(tempos_execucao) / len(tempos_execucao)
        media_satisfacao = sum(satisfacao_clientes) / len(satisfacao_clientes)
        return {
            "tempos_execucao": tempos_execucao,
            "satisfacao_clientes": satisfacao_clientes,
            "tempo_medio_execucao": tempo_medio_execucao,
            "media_satisfacao": media_satisfacao,
        }

    # Função para gerar relatórios de eficiência energética
    def gerar_relatorio_eficiencia_energetica(self):
        economia_energia_solar = 2000  # Valor fictício em kWh
        return {
            "economia_energia_solar": economia_energia_solar,
        }