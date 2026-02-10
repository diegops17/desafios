altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))
area = altura * largura
tinta = 2
litros_tinta = area / tinta

print(f'Uma parede de {altura}m X {largura}m possui {area}m². Precisa {litros_tinta} l para pinta-la')