''''
entrada = input("[E]ntrar ou [S]air: ")
senha_digitada = input("Senha: ")
senha_real = str(123456)

if (entrada == "E" or entrada == "e") and senha_digitada == senha_real:
    print("Bem vindo!!")

else:
    print("Acesso Negado!")
'''
senha = input("Senha: ") or "Sem senha"
print(senha)