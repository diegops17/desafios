preco_produto = float(input('Informe o preço do produto R$ '))
percetentual_desconto = 5 
preco_reajustado = preco_produto - ((preco_produto * percetentual_desconto) / 100)

print(f'O produto com 5% fica R$ {preco_reajustado:.2f} reais.')