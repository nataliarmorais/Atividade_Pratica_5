#Calcular idade em dias

def calcular_idade_em_dias():
    
    # Solicitar o ano do nascimento da pessoa 
    ano_nascimento = int(input("Digite o ano do seu nascimento: "))
    
    #Ano atual
    ano_atual = 2025
    
    #Calcular a idade em anos
    idade_anos = ano_atual - ano_nascimento
    
    #Converter a idade em dias (desconsiderando anos bissextos)
    idade_dias = idade_anos * 365
    
    #Exibe a idade em dias
    print(f"Sua idade em dias é : {idade_dias} dias")
    
    #Chamar a função
calcular_idade_em_dias()
    