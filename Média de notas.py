N1 = float(input())
N2 = float(input())
media = (N1 + N2) / 2
if media == 10:
    resultado = "Aprovado com Distinção"
elif media >= 7:
    resultado = "Aprovado"
elif media < 7:
    resultado = "Reprovado"
print("Média:", round(media, 1))
print(resultado)
