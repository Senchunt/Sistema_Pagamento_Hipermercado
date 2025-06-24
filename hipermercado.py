print('--- Hipermercado Tabajara ---')
carne = input('Digite qual o tipo de carne (F)ile duplo | (A)lcatra | (P)icanha: ')
kg_carne = float(input('Digite quantos quilos deseja levar: '))
pagamento = input('Digite a forma de pagamento (D)inheiro (P)ix ou (C)artão')


## Cálculo Filé Duplo
preco_file5 = kg_carne * 4.90
preco_file6 = kg_carne * 5.80
desconto_file = preco_file5 * 0.05

if carne == 'F':
    if kg_carne <= 5 and kg_carne > 0:
        print(f'Tipo: Filé Duplo')
        print(f'Total: {kg_carne:.0f}kg')
        print(f'Preço Total: R$ {preco_file5:.2f}')
        if pagamento == 'D':
            print(f'Pagamento: Dinheiro')
            print(f'Total final: R$ {preco_file5:.2f} reais')
        elif pagamento == 'P':
            print(f'Pagamento: Pix')
            print(f'Total final: R$ {preco_file5:.2f} reais')
        elif pagamento == 'C':
            print(f'Pagamento: Cartão Tabajara')
            print(f'Desconto 5%: com valor final: R$ {preco_file5 - desconto_file:.2f}')
    if kg_carne > 5 and kg_carne <= 200:
        print(f'Tipo: Filé Duplo')
        print(f'Total: {kg_carne:.0f}kg')
        print(f'Preço Total: R$ {preco_file6:.2f}')
        if pagamento == 'D':
            print(f'Pagamento: Dinheiro')
            print(f'Total final: R$ {preco_file6:.2f} reais')
        elif pagamento == 'P':
            print(f'Pagamento: Pix')
            print(f'Total final: R$ {preco_file6:.2f} reais')
        elif pagamento == 'C':
            print(f'Pagamento: Cartão Tabajara')
            print(f'Desconto 5%: com valor final: R$ {preco_file6 - desconto_file:.2f}')
    else:
        print('Digite um valor válido.')

## Cálculo Alcatra
preco_alcatra5 = kg_carne * 5.90
preco_alcatra6 = kg_carne * 6.80
desconto_alcatra = preco_alcatra5 * 0.05

if carne == 'A':
    if kg_carne <= 5 and kg_carne > 0:
        print(f'Tipo: Alcatra')
        print(f'Total: {kg_carne:.0f}kg')
        print(f'Preço Total: R$ {preco_alcatra5:.2f}')
        if pagamento == 'D':
            print(f'Pagamento: Dinheiro')
            print(f'Total final: R$ {preco_alcatra5:.2f} reais')
        elif pagamento == 'P':
            print(f'Pagamento: Pix')
            print(f'Total final: R$ {preco_alcatra5:.2f} reais')
        elif pagamento == 'C':
            print(f'Pagamento: Cartão Tabajara')
            print(f'Desconto 5%: com valor final: R$ {preco_alcatra5 - desconto_alcatra:.2f}')
    if kg_carne > 5 and kg_carne <= 200:
        print(f'Tipo: Alcatra')
        print(f'Total: {kg_carne:.0f}kg')
        print(f'Preço Total: R$ {preco_alcatra6:.2f}')
        if pagamento == 'D':
            print(f'Pagamento: Dinheiro')
            print(f'Total final: R$ {preco_alcatra6:.2f} reais')
        elif pagamento == 'P':
            print(f'Pagamento: Pix')
            print(f'Total final: R$ {preco_alcatra6:.2f} reais')
        elif pagamento == 'C':
            print(f'Pagamento: Cartão Tabajara')
            print(f'Desconto 5%: com valor final: R$ {preco_alcatra6 - desconto_alcatra:.2f}')
    else:
        print('Valor inválido! Redigite os valores.')

## Cálculo Picanha
preco_picanha5 = kg_carne * 70.90
preco_picanha6 = kg_carne * 80.80
desconto_picanha = preco_picanha5 * 0.05

if carne == 'P':
    if kg_carne <= 5 and kg_carne > 0:
        print(f'Tipo: Picanha')
        print(f'Total: {kg_carne:.0f}kg')
        print(f'Preço Total: R$ {preco_picanha5:.2f}')
        if pagamento == 'D':
            print(f'Pagamento: Dinheiro')
            print(f'Total final: R$ {preco_picanha5:.2f} reais')
        elif pagamento == 'P':
            print(f'Pagamento: Pix')
            print(f'Total final: R$ {preco_picanha5:.2f} reais')
        elif pagamento == 'C':
            print(f'Pagamento: Cartão Tabajara')
            print(f'Desconto 5%: com valor final: R$ {preco_picanha5 - desconto_picanha:.2f}')
    if kg_carne > 5 and kg_carne <= 200:
        print(f'Tipo: Picanha')
        print(f'Total: {kg_carne:.0f}kg')
        print(f'Preço Total: R$ {preco_picanha6:.2f}')
        if pagamento == 'D':
            print(f'Pagamento: Dinheiro')
            print(f'Total final: R$ {preco_picanha6:.2f} reais')
        elif pagamento == 'P':
            print(f'Pagamento: Pix')
            print(f'Total final: R$ {preco_picanha6:.2f} reais')
        elif pagamento == 'C':
            print(f'Pagamento: Cartão Tabajara')
            print(f'Desconto 5%: com valor final: R$ {preco_picanha6 - desconto_picanha:.2f}')
    else:
        print('Valor inválido! Redigite os valores.')
