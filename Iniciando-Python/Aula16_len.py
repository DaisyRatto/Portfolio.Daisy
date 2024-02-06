variavel = "Maçã faz bem à saúde"
print(len(variavel))


numero = input(
    "Digite um número que eu irei dobrá-lo.: "
)

try:
    numero_flutuante = float(numero)
    print(f"Seu número x 2 é {numero_flutuante * 2}")
except:
    print("Isto não é um numero")


if numero.isdigit():
    numero_float = float(numero)
    print(f"O número {numero} 2x é {numero_float * 2}")
else:
    print("ERRO!")

