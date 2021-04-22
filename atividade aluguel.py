Valuguel = int(input())
Vtvacabo = int(input())
Vinternet = int(input())

aluguel = float(525.50 * Valuguel)
tvacabo = int(50 * Vtvacabo)
internet = int(40 * Vinternet)
valorT = (float(aluguel + tvacabo + internet))

print('{:.2f}'.format(valorT))
