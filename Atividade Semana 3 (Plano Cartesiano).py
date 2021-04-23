# Atividade para encontrar o valor de x e y dentro de quandrante no plano cartesiano. #
# ___________________________________________________________________________________ #

x = float(input('Digite o valor de X: '))
y = float(input('Digite o valor de Y: '))
if x == y == 0:
    print('O valor se encontra na ORIGEM')
elif x > 0 and y > 0:
    print('O valor se encontra no 1° Quadrante ')
elif y > 0 and x < 0:
    print('O valor se encontra no 2° Quadrante ')
elif y < 0 and x < 0:
    print('O valor se encontra no 3° Quadrante ')
elif y < 0 and x < 0:
    print('O valor se encontra no 4° Quadrante ')
elif y == 0 and x > 0 or x < 0:
    print('Esse é o Eixo X')
elif x == 0 and y > 0 or y < 0:
    print('Esse é o eixo Y')