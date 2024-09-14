co_gasolina = 2.2
co_alcool = 0.56
co_gas_natural = 0.14

def credito_gas(consumo):
    
    emissao = consumo * co_gasolina
    credito = emissao / 1000
    
    return credito

def credito_alcool(consumo):
    
    emissao = consumo * co_alcool
    credito = emissao / 1000
    
    return credito

def potencia_gas1(km):
    consumo = km / 10.6

    return f"Tonelada de CO2 (Gasolina 1.4) = {round(credito_gas(consumo), 3)}"

def potencia_gas2(km):
    consumo = km / 9.3

    return f"Tonelada de CO2 (Gasolina 1.5 à 2.0) = {round(credito_gas(consumo), 3)}"

def potencia_gas3(km):
    consumo = km / 7.2
    
    return f"Tonelada de CO2 (Gasolina acima de 2.0) = {round(credito_gas(consumo), 3)}"

def potencia_alcool1(km):
    consumo = km / 6.7

    return f"Tonelada de CO2 (Alcool até 1.4) = {round(credito_alcool(consumo), 3)}"

def potencia_alcool2(km):
    consumo = km / 6.1

    return f"Tonelada de CO2 (Alcool de 1.5 até 2.0) = {round(credito_alcool(consumo), 3)}"

def potencia_alcool3(km):
    consumo = km / 5.7

    return f"Tonelada de CO2 (Alcool de acima de 2.0) = {round(credito_alcool(consumo), 3)}"

def gas_natural(km):

    emissao = km * co_gas_natural
    credito = emissao / 1000

    return f"Tonelada de CO2 (Gás Natural) = {round(credito, 3)}"



print(potencia_gas1(1000))
print(potencia_gas2(1000))
print(potencia_gas3(1000))

print(potencia_alcool1(1000))
print(potencia_alcool2(1000))
print(potencia_alcool3(1000))

print(gas_natural(1000))