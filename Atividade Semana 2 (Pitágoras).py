# Criar programa para calcular un triângulo retângulo usando o teorema de pitágoras.
# Solicitar ao usuário o cateto opst, cateto adj, e o ângulo.
# Calcule a hipotenusa. hipo = (Copst ** 2 + Cadj ** 2) ** (1/2)
# Calcule a área. area = (Copst * Cadj)/2
# Calcule o perímetro do triangulo. PdoT = hipo + Copst + Cadj
# Descubra o angulo alfa.
# Descubra o angulo de beta
# Revelar o sen, cos, tang de alfa. respectivamente = SenoA, CosA, TanA.
# Revelar o sen, cos, tabg de beta. respectivamente = SenoB, CosB, TanB.

import math

Copst = float(input('Digite o valor do cateto adjacente: '))
Cadj = float(input('Digite o valor do cateto oposto: '))
hipo = math.hypot(Cadj, Copst)
area = (Cadj * Copst) / 2
PdoT = (hipo + Cadj + Copst)
alfa = math.asin(Copst / hipo) * (180 / math.pi)
beta = ((math.radians(90)) - (- alfa))
SenoA = math.sin(math.radians(alfa))
CosA = math.cos(math.radians(alfa))
TanA = math.tan(math.radians(alfa))
SenoB = math.sin(math.radians(beta))
CosB = math.cos(math.radians(beta))
TanB = math.tan(math.radians(beta))
print('O valor da hipotenusa é', hipo)
print('O valor da área é', area)
print('O valor do perímetro do triângulo é', PdoT)
print('O ângulo alfa é', math.floor(alfa))
print('O ângulo beta é', math.floor(beta))
print('O valor do seno do ângulo alfa é', SenoA)
print('O valor do cosseno do ângulo alfa é', CosA)
print('O valor da tangente do ângulo alfa é', TanA)
print('O valor de seno do ângulo beta é', SenoB)
print('O valor de cosseno do ângulo beta é', CosB)
print('O valor da tangente do ângulo beta é', TanB)
