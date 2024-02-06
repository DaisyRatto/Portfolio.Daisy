filhos = ["Diogo", "Débora", "Daisy"]
filho1, filho2, filho3 = filhos
indice = filho1, filho2, filho3

for indice, nomes in enumerate(filhos):
    indice += 1
    print(indice, nomes)

for pergunta in filhos:

    pergunta_1 = input("Qual dos filhos acima é o mais gordo? ")

    if pergunta_1 == filho3:
        print(f"Muito bem, você acertou. {filho3=} é a mais gorda dos filhos")
    else:
        print("Você errou! ")
        continue
