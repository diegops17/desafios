email = str(input('Informe o seu e-mail completo: ')).strip().lower()

inicio = email.find('@')
fim = email.find('.', inicio)

dominio = email[inicio + 1: fim]

print(f'Dominio do e-mail informado: {dominio}')