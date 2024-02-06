
contador = 0

while contador <= 50:
    contador += 1

    if contador == 6:
        print("Oi!")
        continue
    
    print(contador)

    if contador == 30:
        break

print("Finished!!")