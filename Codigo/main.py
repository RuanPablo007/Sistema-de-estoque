produto = input('Qual é o seu produto? ')
preco = float(input('Qual é o preço do produto? '))
quantidade = int(input('Qual a quantidade? '))

if produto == '':
    print('PRODUTO INVALIDO')

elif preco <= 0:
    print('ERRO')

elif quantidade < 0:
    print('ERRO')

else:
    valorEstoque = preco * quantidade
    print('\n===== DADOS DO PRODUTO =====')
    print(f'O nome do seu produto é: {produto}')
    print(f'O preço do seu produto é: R${preco:.2f}')
    print(f'A quantidade é: {quantidade}')
    print(f'O valor do estoque é de: R${valorEstoque:.2f}')
    print('Cadastro válido')