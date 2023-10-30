import modulo_relatorio_analises

def run():
    print("Escolha uma opção:")
    print("1. Relatório de Vendas")
    print("2. Relatório de Desempenho de Serviços Automotivos")
    print("3. Relatório de Eficiência Energética")
    escolha = input("Digite o número da opção desejada: ")

    if escolha == "1":
        relatorio = modulo_relatorio_analises.gerar_relatorio_vendas()
        imprimir_relatorio("Relatório de Vendas", relatorio)
    elif escolha == "2":
        relatorio = modulo_relatorio_analises.gerar_relatorio_desempenho_servicos()
        imprimir_relatorio("Relatório de Desempenho de Serviços Automotivos", relatorio)
    elif escolha == "3":
        relatorio = modulo_relatorio_analises.gerar_relatorio_eficiencia_energetica()
        imprimir_relatorio("Relatório de Eficiência Energética", relatorio)
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

# Função para imprimir relatórios
def imprimir_relatorio(titulo, relatorio):
    print("\n" + titulo)
    for chave, valor in relatorio.items():
        print(f"{chave}: {valor}")
    print("\n")

# Chame a função principal
