# Atividade de um código para calcular o IMC de uma pessoa.  #
# __________________________________________________________ #

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
IMC = peso / (altura ** 2)
if IMC < 17:
    print("Muito abaixo do peso")
elif 17 <= IMC <= 18.49:
    print("Abaixo do peso")
elif 18.5 < IMC <= 24.99:
    print("peso normal")
elif 25 < IMC <= 29.99:
    print('Acima do peso')
elif 30 < IMC <= 34.99:
    print('Obesidade I')
elif 35 < IMC <= 39.99:
    print('Obesidade II')
elif IMC > 40:
    print('Obesidade III')
