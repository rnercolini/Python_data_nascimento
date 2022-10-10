from datetime import date
print('\033[0;31m*_*_' * 13, '\033[m')
print('\033[31mDigite a data do seu nascimento\033[m')
dia = int(input('Dia = '))
mes = int(input('Mês = '))
ano = int(input('Ano = '))
idade = date.today().year - ano
print('Você nasceu no dia\033[34m', dia, '\033[mde\033[34m', mes, '\033[mde\033[34m', ano,'\033[m. Correto?')
print('Você tem\033[34m', idade, '\033[m.')
print('\033[31m*_*_' * 13, '\033[m')


      
