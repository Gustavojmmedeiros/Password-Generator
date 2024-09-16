import random

print("---Gerador de senhas---")

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHYJKLMNOPQRSTUVWXYZ!@#$%¨&*().,?0123456789"

length = int(input("Tamanho da senha (mínimo de 6 caracteres): "))

quantity = int(input("Deseja gerar quantas senhas? (mínimo de 1 e máximo de 5): "))

print("Gerando senhas...")

def gerar_senha(l, q):
    for _ in range(q):
        passwords = ''

        for _ in range(l):
            passwords += random.choice(CHARS)
        
        print(passwords)

senha = gerar_senha(length, quantity)
