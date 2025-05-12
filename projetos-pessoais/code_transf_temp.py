temp = int(input("Digite a temperatura atual que deseja converter: "))
tip = int(input("Essa temperatura está em graus Celsius ou Farenheit, digite '1' para Celsius e '2' para Farenheit! "))

if tip == 1:
 tempf = (9 * temp) / 5 + 32
 print(f"Sua temperatura convertida em Farenheit é: {tempf}")

elif tip == 2:
 tempf = 5 * (temp - 32) / 9
 print(f"Sua temperatura convertida em Celsius é: {tempf}")

else:
    print("Insira um número válido!")