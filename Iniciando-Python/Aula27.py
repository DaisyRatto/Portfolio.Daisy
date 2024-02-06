lista = ["Bolo", "Brigadeiro", "Coxinha"]
itemx = lista.count("Bolo")

nomes = [

    ["Billy", "Jack", "Max"],

    ["Mamis", "Diogo", "Vó Nira", "Daisy"],

    ["Débora", "Lucas", "Lolis", ],
]

# print(nomes[1][1])
# print(nomes[2][3][2])
# print(nomes[0][0])

for sala in nomes:
    print(f"Sala {sala}: ")

    for aluno in sala:
        print(aluno)
