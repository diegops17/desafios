metros = float(input('Informe os metros: '))
decimetro = metros * 10
centimetro = metros * 100
milimetro = metros * 1000
km = metros / 1000
milhas = metros / 1.609,34

print(f'{metros}m equivale a {decimetro} dm')
print(f'{metros}m equivale a {centimetro} cm')
print(f'{metros}m equivale a {milimetro} mm')
print(f'{metros}m equivale a {km} km')
print(f'{metros}m equivale a {milhas} mi')