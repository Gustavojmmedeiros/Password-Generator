import random

print("---Gerador de senhas---")

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHYJKLMNOPQRSTUVWXYZ!@#$%&*().,?0123456789"


def length_input():
    while True:
        try: 
            length = int(input("Tamanho da senha (mínimo de 6 caracteres): "))

            if length <= 0:
                raise ValueError
            elif 0 < length < 6:
                print("Senha deve ter no mínimo 6 caracteres")
            else:
                return length

        except EOFError:
            return 6

        except ValueError:
            print("Tamanho da senha deve ser um número inteiro e não pode ser menor ou igual a zero.")


def quantity_input():
    while True:
        try:
            quantity = int(input("Deseja gerar quantas senhas? (mínimo de 1 e máximo de 5): "))
            
            if quantity < 1:
                raise ValueError
            elif quantity > 5:
                print(f"Você solicitou {quantity} senhas, mas o máximo senhas geradas por vez é 5.")
            else:
                return quantity
        
        except EOFError:
            return 1
        
        except ValueError:
            print("Quantidade de senhas deve ser um número inteiro e não pode ser menor ou igual a zero")


def generate_password(length, quantity):
    passwords_list = []

    print(f"Gerando {quantity} senhas...")

    for _ in range(quantity):
        password = ''.join(random.choice(CHARS) for _ in range(length))
        passwords_list.append(password)

    return passwords_list


user_length = length_input()
user_quantity = quantity_input()

passwords = generate_password(user_length, user_quantity)

for password in passwords:
    print(password)
