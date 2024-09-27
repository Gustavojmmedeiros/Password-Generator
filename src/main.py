import random

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHYJKLMNOPQRSTUVWXYZ!@#$%&*().,?0123456789"


def length_input(length=None):
    if length is not None:
        if length < 6:
            raise ValueError
        return length

    while True:
        try:
            length = int(input("\nTamanho da senha (mínimo de 6 caracteres): "))
            if length < 6:
                raise ValueError
            else:
                return length
        except ValueError:
            if length <= 0:
                print("Tamanho da senha não pode ser menor ou igual a zero.")
            elif length < 6:
                print("Senha deve ter no mínimo 6 caracteres.")
                

def quantity_input(quantity=None):
    if quantity is not None:
        if quantity <= 0:
            raise ValueError
        elif quantity > 5:
            raise ValueError
        return quantity

    while True:
        try:
            quantity = int(input("\nDeseja gerar quantas senhas? (mínimo de 1 e máximo de 5): "))
            if quantity <= 0:
                raise ValueError
            elif quantity > 5:
                raise ValueError
            else:
                return quantity
        except ValueError:
            if quantity <= 0:
                print("Valor não pode ser zero nem pode ser negativo.")
            elif quantity > 5:
                print(f"Você solicitou {quantity} senhas, mas o máximo senhas geradas por vez é 5.")


def generate_password(length, quantity):
    passwords_list = []
    print(f"\nGerando {quantity} senhas...\n")

    for _ in range(quantity):
        password = ''.join(random.choice(CHARS) for _ in range(length))
        passwords_list.append(password)

    return passwords_list


if __name__ == "__main__":
    user_length = length_input()
    user_quantity = quantity_input()
    passwords = generate_password(user_length, user_quantity)

    for password in passwords:
        print(password + "\n")
