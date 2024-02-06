frase = "O Python é uma linguagem de programação" \
    " multiparadigma." \
    " Python foi criado pelo Holandês Guido van Rossum.".lower()

i = 0
qtd_x_letra_apareceu = 0
letra_mais_apareceu = " "
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == " ":
        i += 1
        continue

    qtd_x_letra_apareceu_atual = frase.count(letra_atual)

    if qtd_x_letra_apareceu < qtd_x_letra_apareceu_atual:
        qtd_x_letra_apareceu = qtd_x_letra_apareceu_atual
        letra_mais_apareceu = letra_atual

    i += 1

print(
    "A letra que apareceu mais vezes foi "
    f"'{letra_mais_apareceu}' "
    f"ela apareceu {qtd_x_letra_apareceu}x"

)