entrada = input("Quantos anos você tem? ")

int_entrada = int(entrada)
if int_entrada >= 18:
    print("Acesso liberado!")
elif int_entrada <= 17:
    print("Acesso NEGADO!")


saida = input("Oque você achou do conteúdo? Bom ou Ruim? ")

if saida == "Bom":
    print("Que bom que gostou!")
elif saida == "Ruim":
    print("Que pena, estamos trabalhando para melhorar cada vez mais!")
else:
    print("Volte sempre!!")