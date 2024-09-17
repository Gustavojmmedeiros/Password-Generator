import random

print("---Gerador de senhas---")

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHYJKLMNOPQRSTUVWXYZ!@#$%&*().,?0123456789"

try: 
    length = int(input("Tamanho da senha (mínimo de 6 caracteres): "))
except EOFError:
    length = 6

try:
    quantity = int(input("Deseja gerar quantas senhas? (mínimo de 1 e máximo de 5): "))
except EOFError:
    quantity = 1

print("Gerando senhas...")


def generate_password(length, quantity):
    passwords_list = []

    for _ in range(quantity):
        password = ''.join(random.choice(CHARS) for _ in range(length))
        passwords_list.append(password)
    return passwords_list


passwords = generate_password(length, quantity)

for password in passwords:
    print(password)
