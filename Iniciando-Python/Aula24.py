for i in range(10):
    if i == 2:
        print("Epa!")
        continue

    if i == 8:
        print("Não tem mais nada por aqui")
        break
    for j in range(0, 3):
        print(i, j)
else: 
    print("vamos ver se chega até aqui")