import random
import string

print("---Gerador de Senhas---")

# Definir o conjunto de caracteres para a senha
CHARS = string.ascii_letters + string.digits + "!@#$%¨&*().,?"

def gerar_senhas(tamanho, quantidade):
    """Função para gerar senhas"""
    senhas = []
    for _ in range(quantidade):
        senha = ''.join(random.choice(CHARS) for _ in range(tamanho))
        senhas.append(senha)
    return senhas

# Solicitar o tamanho da senha e a quantidade de senhas ao usuário
while True:
    try:
        tamanho_senha = int(input("Tamanho da senha (mínimo de 6 caracteres): "))
        if tamanho_senha < 6:
            print("O tamanho da senha deve ser pelo menos 6 caracteres.")
            continue
        quantidade_senhas = int(input("Deseja gerar quantas senhas? (mínimo de 1 e máximo de 5): "))
        if quantidade_senhas < 1 or quantidade_senhas > 5:
            print("A quantidade de senhas deve ser entre 1 e 5.")
            continue
        break
    except ValueError:
        print("Por favor, insira um número válido.")

print("Gerando senhas...")

# Gerar e exibir as senhas
senhas_geradas = gerar_senhas(tamanho_senha, quantidade_senhas)
for senha in senhas_geradas:
    print(senha)
