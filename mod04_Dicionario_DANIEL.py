'''





'''

prato_dia = {

    'segunda-feira': 'ovo',
    'terça-feira': 'macarrao alho e oleo',
    'quarta-feira': 'frango parmegiana',
    'quinta-feira': 'peixe frito ',
    'sexta-feira': 'carne de panela',
    'sabado': 'lasanha',
    'Domingo': 'arroz com feijao e bife a cavalo'
  }

dia_escolhido = input('Digite o dia da semana para saber o prato do dia: \n').lower() 


if dia_escolhido in prato_dia:
    comida = prato_dia[dia_escolhido]
    print(f'O prato do dia para {dia_escolhido} é: {comida}')
else:
    print('Dia inválido. Por favor, digite um dia da semana válido.')


print('💥  ' * 20)
