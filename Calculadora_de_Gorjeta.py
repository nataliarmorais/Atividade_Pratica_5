# Calculadora de Gorjeta

conta = float(input("Digite o valor da conta:(R$): ")) # R$ 100.00

porcentagem = float(input("Digite a porcentagem da gorjeta:(%):")) # ex: 10%, 15%, 20%


# Calcule o valor da gorjeta
    
valor_gorjeta = (conta * porcentagem) / 100

 # Exiba o resultado
 
print(f"O valor da gorjeta para uma conta de R$ {conta:.2f} com uma porcentagem de {porcentagem}% é R$ {valor_gorjeta:.2f}.")




