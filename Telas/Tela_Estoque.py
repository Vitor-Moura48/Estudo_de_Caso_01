from Sistemas.imports import *
from Sistemas.Modulo_Controle_de_Estoques_de_Produtos import controle_de_estoque

class TelaEstoque(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)

        self.configure(bg='white')

        label_fundobranco = Label(self, width=45, height=30, background='#242323', relief=RAISED)
        label_fundobranco.place(x=230, y=80)
       
        # Produto:
        label_produto = Label(self, width=10, height=2, text='Produto:', font=("Arial", 10), bg='#242323', fg='#888a89')
        label_produto.place(x=240, y=160)

        entrada_produto = Entry(self, width=14, font=("Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_produto.place(x=260, y=190)

        self.entrada_produto = entrada_produto

        # Quantidade:
        label_quantidade = Label(self, width=10, height=2, text='Quantidade:', font=("Arial", 10), bg='#242323', fg='#888a89')
        label_quantidade.place(x=250, y=240)

        entrada_quantidade = Entry(self, width=14, font=("Arial", 25), bg='#636262', highlightthickness=0.5, relief='solid')
        entrada_quantidade.place(x=260, y=270)

        self.entrada_quantidade = entrada_quantidade

        # Botão de confirmar:
        botao_confirmar = Button(self, text='confirmar', width=23, command=lambda: self.confirmar_compra(), height=2, font=("Arial", 15), bg='#02bae8', fg='white', relief=RAISED, overrelief=RAISED)
        botao_confirmar.place(x=260, y=400)
    
    def limpar_campos(self):
        self.entrada_produto.delete(0, END)
        self.entrada_quantidade.delete(0, END)

    def confirmar_compra(self):
        produto = self.entrada_produto.get()
        quantidade = self.entrada_quantidade.get()

        if quantidade.isdigit():
            quantidade = int(quantidade)

            estoque = pandas.read_csv("Sistemas/estoque.csv")
        
            if quantidade > 0 and produto in estoque.iloc[0]:
                controle_de_estoque.update({produto: quantidade})

            else:
                messagebox.showinfo("Atenção!", "Preencha os campos corretamente", icon="warning")

        else:
            messagebox.showinfo("Atenção!", "Preencha os campos corretamente", icon="warning")
        
        self.limpar_campos()