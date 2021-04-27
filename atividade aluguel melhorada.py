Valuguel = int(input())
Vtvacabo = int(input())
Vinternet = int(input())

aluguel = float(525.50 * Valuguel)
tvacabo = int(50 * Vtvacabo)
internet = int(40 * Vinternet)
valorT = (float(aluguel + tvacabo + internet))

while (Valuguel, Vtvacabo, Vinternet):
    if Valuguel <= 0:
        print('Erro: O número de semanas do aluguel deve ser positivo')
    elif Vtvacabo < 0:
        print('Erro: O número de semanas de TV a cabo não pode ser negativo')
    elif Vinternet < 0:
        print('Erro: O número de semanas de Internet não pode ser negativo')
    else:
        print('{:.2f}'.format(valorT))
    break


