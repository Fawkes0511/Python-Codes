sexo = input('').strip()
altura = float(input(''))
peso = float(input(''))
h = altura
imc_M = (peso * h  - 58) / 2
imc_F = (peso * h  - 44.7) / 2
if sexo == 'M':
    if imc_M < 18.5:
     print("abaixo do peso")
    elif 18.5 <= imc_M < 24.9:
     print("peso ideal")
    elif imc_M > 25.0:
     print("acima do peso")
if sexo == 'F':
    if imc_F < 18.5:
     print("abaixo do peso")
    elif 18.5 <= imc_F < 24.9:
     print("peso ideal")
    elif imc_F > 25.0:
     print("acima do peso")
