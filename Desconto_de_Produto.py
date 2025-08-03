# Calculadora de Desconto

def calcular_desconto():
    # Solicita o preço do produto e o percentual de desconto ao usuário
    preco_original = float(input("Digite o preço original do produto (R$): "))
    desconto_percentual = float(input("Digite o percentual do produto (em%): "))
    
    # Calcula o valor do desconto e o preço final
    desconto = (preco_original * desconto_percentual) / 100
    preco_final = preco_original - desconto
    
    # Exibe o valor do desconto e o preço final com o desconto aplicado
    print(f"O valor do desconto é: R$ {desconto:.2f}")
    print(f"O preço final com desconto é: R$ {preco_final:.2f}")

# Chama a função fora da definição para execução
calcular_desconto()
