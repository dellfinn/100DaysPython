conta = float(input("Qual foi o valor total da conta?\n R$"))

porcetagem = float(input("Que porcentagem de gorjeta você gostaria de pagar?\n %"))

grupo = int(input("Quantas pessoas para dividir a conta?\n "))

print(f"Cada um de vocês deve pagar:{'{:.2f}'.format(conta / grupo + (conta * ((porcetagem / 100) / grupo)))}")