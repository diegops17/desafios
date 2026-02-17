cidade = str(input('Informe o nome da cidade: ')).strip().upper()

cidade_splitada = cidade.split()

if cidade_splitada[0] == 'SANTO':
    print(f'{cidade} começa com {cidade_splitada[0]}')
else:
    print(f'{cidade} não começa com SANTO')
