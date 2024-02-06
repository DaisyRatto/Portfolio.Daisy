'''
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

lista_1 = [74, 85, 96]
lista_2 = [25, 24, 23]
# lista_original = lista_1 + lista_2

lista_1.append("lululuu")
lista_1.append("Ola")
lista_1.pop()
lista_1.insert(1, "patê de frango")
del lista_2[-2]

lista_original = lista_1 + lista_2

print(lista_original)