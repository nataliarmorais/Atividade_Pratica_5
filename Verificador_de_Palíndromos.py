import re

# Função para verificar se um texto é um palíndromo
def verificar_palindromo():
    # Solicita ao usuário uma palavra ou frase
    frase = input("Digite uma palavra ou frase: ")

    # Remove espaços, pontuação e coloca tudo em minúsculo
    frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()

    # Verifica se a frase é um palíndromo
    if frase_limpa == frase_limpa[::-1]:
        print("Sim, é um palíndromo!")
    else:
        print("Não, não é um palíndromo!")

# Chama a função
verificar_palindromo()