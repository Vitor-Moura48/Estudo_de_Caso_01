import datetime

#Tela inicial:

def run():
  print('Olá Seja bem vindo ao Caixa\nEcoPosto')
  a = 'nao'
  while a == 'sim':
    selecao_inicio = int(input('Escolha: \n1 -- Acesso \n2 -- Cadastro Funcionário'))
    if selecao_inicio == 1:
      print( '-- Tela de login --' )
    if selecao_inicio == 2:
      print(' -- Tela de cadastro --')
    else:
      print('Ops, Algo de errado não está certo\n')
      a = str(input('Quer tentar de novo?\n*5'))

  #Acesso -- Tela de login --
  login_caixa = str(input('Digite o login:\n'))
  senha_caixa = str(input('Digite a senha:\n'))

  #Cadastro -- Tela de Cadastro --


  #Exibir lista de abastecimentos - pagos e com pendencias:
  print('Lista de abastecimentos\n')
  print('|Hora:    Bomba:      Frentista:      Tipo:       Quant.:       Situação:      |')



  #Registro do abastecimento
  #OBS: no momento só teremos uma bomba para abastecer
  tipo_combustivel = ('',0)
  situacao = 'Em aberto' #essa variavel é para saber se foi pago ou não

  frentista = ['João', 'Maria', 'José']

  while True:
    novo_abastecimento = str(input('Novo abastecimento?'))
    if novo_abastecimento == 'sim':

      #loop para exibir todos os frentistas
      print('Qual o frentista?/')
      for i in range(len(frentista)):
        print(i,' -- ',frentista[i] , '\n2')
        selecao_frentista = input()

      #Exibis todos os tipos de combustiveis:
      print('Qual o tipo do combustivel:/n')
      Tipo_combustivel = int(input('1 -- Alcool \n2 -- Gasolina \n3 -- Diesel\n'))


      if Tipo_combustivel == 1:
      #Alcool
        tipo_combustivel = ('Alcool', 4.5)
        selecao_combustivel = 0
      
      if Tipo_combustivel == 2:
      #Gasolina
        tipo_combustivel = ('Gasolina', 5.9)
        selecao_combustivel = 0
      
      if Tipo_combustivel == 3:
      #Diesel
        tipo_combustivel = ('Diesel', 4.8)
        selecao_combustivel = 0

      #Abastecendo o veículo
      abastecendo = int(input('Deseja colocar qual valor ou quantos litros?'))
      
      #agora preciso tratar esse dado para verificar se
      #o cliente vai dizer em litros ou em reais 
      # ...
      #e fazer loop para a pessoa tentar de novo

    print('|Hora:    Bomba:      Frentista:      Tipo:       Quant.:       Valor:     Situação:      |')
    print('| ---',    'Bomba 01',      selecao_frentista,      tipo_combustivel[0],       'Quant.:',       tipo_combustivel[1],     situacao,      '|')

    break
