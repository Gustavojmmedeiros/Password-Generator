import random

print("---Gerador de senhas---")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHYJKLMNOPQRSTUVWXYZ!@#$%¨&*().,?0123456789"

length = int(input("Tamanho da senha (mínimo de 6 caracteres): "))

quantity = int(input("Deseja gerar quantas senhas? (mínimo de 1 e máximo de 5): "))

print("Gerando senhas...")

for pwd in range(quantity):
    passwords = ''

    for i in range(length):
        passwords += random.choice(chars)
    
    print(passwords)