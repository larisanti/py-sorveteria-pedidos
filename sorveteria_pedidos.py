print('Bem-vindo à Loja de Gelados da Larissa de Santi')
print('------------------Cardápio------------------')
print('--------------------------------------------')
print('---| Tamanho | Cupuaçu (CP) | Açaí (AC) |---')
print('---|    P    |   R$ 9.00    | R$ 11.00  |---')
print('---|    M    |   R$ 14.00   | R$ 16.00  |---')
print('---|    G    |   R$ 18.00   | R$ 20.00  |---')
print('--------------------------------------------')

# Criar variável para valor total do pedido
valor_total = 0

# Criar loop para sabor e tamanho
while True:
    # Implementar input do sabor
    while True:
      sabor = input('Entre com o sabor desejado (CP/AC): ').upper()
      if (sabor != 'CP' and sabor != 'AC'): # Se sabor diferente
        print('Sabor inválido. Tente novamente.')
        continue # Volta no loop 1
      break # Sai do loop 1

    # Implementar input do tamanho
    while True:
      tamanho = input('Entre com o tamanho desejado (P/M/G): ').upper()
      if (tamanho != 'P' and tamanho != 'M' and tamanho != 'G'): # Se tamanho diferente
        print('Tamanho inválido. Tente novamente.')
        continue # Volta no loop 2
      break # Sai do loop 2

    # Implementar acumulador utilizando modelo aninhado
    if sabor == 'CP': # Condições para Cupuaçu
      if tamanho == 'P':
        valor = 9
      elif tamanho == 'M':
        valor = 14
      elif tamanho == 'G':
        valor = 18
      print(f'Você pediu um Cupuaçu no tamanho {tamanho}: R$ {valor:.2f}')
    elif sabor == 'AC': # Condições para Açaí
      if tamanho == 'P':
        valor = 11
      elif tamanho == 'M':
        valor = 16
      elif tamanho == 'G':
        valor = 20
      print(f'Você pediu um Açaí no tamanho {tamanho}: R$ {valor:.2f}')

    valor_total += valor # Adicionar o valor do item ao total

    # Perguntar se deseja mais alguma coisa
    adicionar_item = input('Deseja adicionar mais alguma coisa? (S/N): ').upper()
    if adicionar_item != 'S':
      break

# Encerrar o programa e executar o print do acumulador
print(f'O valor total a ser pago: R$ {valor_total:.2f}')