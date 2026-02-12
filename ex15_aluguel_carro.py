km_percorrido = float(input('Informe quantos km percorreu: '))
quant_dias_alugado = int(input('Informe a quantidade de dias alugados: '))

custo_dia = 60
custo_km_rodado = 0.15

total_pagar = ((km_percorrido * custo_km_rodado) + (quant_dias_alugado * custo_dia))

print(f'Total pagar pelo aluguel do carro R$ {total_pagar:.2f} reais.')