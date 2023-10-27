from Sistemas.imports import *
from Telas.Tela_Estoque import TelaEstoque

# criar instância da classe TelaEstoque
janela = tk.Tk()
tela_estoque = TelaEstoque()

# Configurar janela principal
janela.title("Tela de Estoque")
janela.geometry("800x600")

# Adicionar instância da classe TelaEstoque à janela principal
tela_estoque.pack(fill="both", expand=True)

# Iniciar o loop principal do Tkinter
janela.mainloop()