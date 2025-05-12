positivo = 0
negativo = 0
numeros = []

while True:
    numeros = int(input("Digite um número inteiro e quando quiser parar digite o número '0'"))
    if numeros == 0:
        break
    elif numeros > 0:
        positivo += 1
    elif numeros < 0:
        negativo += 1
    else:
        print("Digite um valor válido!")

print(f"Quantidade de números positivos digitados foi {positivo}")
print(f"Quantidade de números negativos digitados foi {negativo}")

if positivo > negativo:
    print("Há mais números positivos")
elif negativo > positivo:
    print("Há mais números negativos")
else:
    print("A quantidade de números negativos e positivos digitados são iguais!")