'''
entrada = input("[E]ntrar ou [S]air: ")
senha_digitada = input("Senha: ")

senha_real = str(123456)

if entrada == "E" and senha_digitada == senha_real:
    print("Bem vindo!!")

else:
    print("Acesso Negado!")
'''
print(bool(0))
print(True and 0 and True)

if 0 and 1:
    print(True and 1) # não aparecerá nada -> Valor falsy/none