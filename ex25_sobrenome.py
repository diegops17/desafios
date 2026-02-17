nome_completo = str(input('Informe o seu nome completo: ')).strip().upper()

if 'SILVA' in nome_completo:
    print(f'{nome_completo} tem SILVA no nome')
else:
    print(f'{nome_completo} não tem SILVA no nome')