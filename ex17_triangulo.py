import math
cateto_oposto = int(input('Informe o cateto oposto: '))
cateto_adjacente = int(input('Informe o cateto adjacente: '))

hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotensa é {hipotenusa}')
