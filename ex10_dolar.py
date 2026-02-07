real_carteira = float(input('Informe quanto real(is) tem R$ '))
cotacao_dolar = 5.22

dolar_pode_comprar = real_carteira / cotacao_dolar 

print(f'Com R$ {real_carteira} real(is) equivale a U$$ {dolar_pode_comprar:.2f} dólares.')