# Programa para inserir cidade, temperatura e escala.
cidade = input('Digite sua cidade: ').strip()
temperatura = float(input('Digite a temperatura da sua cidade: '))
escala = input('Digite a escala.ex(K,C OU F): ')

if escala == 'F':
    C = (temperatura - 32) * (5 / 9)
elif escala == 'K':
    C = (temperatura - 273.15)
else:
    C = temperatura
if C < 17:
    temperatura = 'fria'
elif C < 30:
    temperatura = 'ambiente'
else:
    temperatura = 'quente'
print('{} está {} e medindo {:.1f}°C'.format(cidade, temperatura, C))
