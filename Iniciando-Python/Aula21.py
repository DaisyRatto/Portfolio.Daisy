string = "Só um teste."
nova_letra = " "
i = 0
while i < len(string):
    letra = string[i]
    nova_letra += letra
    i += 1 

else:
    print("Else no while pode")
print(nova_letra)