bill = float(input("Qual foi o valor total da conta?\n $"))

tip = float(input("Que porcentagem de gorjeta você gostaria de pagar?\n %"))

group = int(input("Quantas pessoas para dividir a conta?\n "))

print(f"Each one of you should pay: ${'{:.2f}'.format(bill / group + (bill * ((tip / 100) / group)))}")