# Atividade para criar um programa que simula uma calculadora simples.

N1_op_N2 = input('Digite seu cálculo,ex(2 * 2): ').split()
N1, opera, N2 = int(N1_op_N2[0]), N1_op_N2[1], int(N1_op_N2[2])
so = N1 + N2
su = N1 - N2
m = N1 * N2
d = N1 / N2

if opera == '+':
    print('{} + {} = {:.1f}'.format(N1, N2, so))

elif opera == '-':
    print('{} - {} = {:.1f}'.format(N1, N2, su))

elif opera == '*':
    print('{} * {} = {:.1f}'.format(N1, N2, m))

elif opera == '/':
    print('{} / {} = {:.1f}'.format(N1, N2, d))
