from textwrap import dedent
from math import ceil

# Função para calcular o valor monetário
def valor_da_tonelada(co):
    
    media_valor_credito = 70.10 # Média dos últimos 12 meses na bolsa de valores
    valor = co * media_valor_credito

    return valor

# Função de compensação das Árvores
def arvores(co):
    absorcao_co2 = 0.36485 # Cálculo baseado do site IDESAM
    arvore = co / absorcao_co2

    return arvore

#Função Menu

def menu():
    print ("\n","Menu da Calculadora".center(40, "="))
    menu = ("""
    Bem vindo a calculadora de carbono!!!
    =============================

    [v] - Veículo
    [e] - Energia
    [s] - Sair

    =============================
    Escolha a operação:""")

    return input(dedent(menu))

#Função Cálculo de emissão veículos

def calc_veiculo(CO_ALCOOL, CO_DIESEL, CO_GAS_NATURAL, CO_GASOLINA, opcao_veiculo):

    while True:


        #Gasolina 1.4
        if (opcao_veiculo == "g1"):
            km = int (input ("Digite sua kilometragem mensal: "))

            consumo = km / 10.6
            emissao = consumo * CO_GASOLINA
            credito = emissao / 1000
            anual = credito * 12

            print (f'''Resultado:
            Toneladas de CO2 por mês: {round(credito, 3)}
            Toneladas de CO2 por ano: {round(anual, 3)}
            Árvores à replantar: {ceil(arvores(anual))}
            Valor monetário do Crédito de Carbono: R${round(valor_da_tonelada(anual),2)}''')

        #Gasolina 1.5
        elif (opcao_veiculo == "g2"):
            km = int (input ("Digite sua kilometragem mensal: "))

            consumo = km / 9.3
            emissao = consumo * CO_GASOLINA
            credito = emissao / 1000
            anual = credito * 12

            print (f'''Resultado:
            Toneladas de CO2 por mês: {round(credito, 3)}
            Toneladas de CO2 por ano: {round(anual, 3)}
            Árvores à replantar: {ceil(arvores(anual))}
            Valor monetário do Crédito de Carbono: R${round(valor_da_tonelada(anual),2)}''')


        #Gasolina 2.0
        elif (opcao_veiculo == "g3"):
            km = int (input ("Digite sua kilometragem mensal: "))

            consumo = km / 7.2
            emissao = consumo * CO_GASOLINA
            credito = emissao / 1000
            anual = credito * 12

            print (f'''Resultado:
            Toneladas de CO2 por mês: {round(credito, 3)}
            Toneladas de CO2 por ano: {round(anual, 3)}
            Árvores à replantar: {ceil(arvores(anual))}
            Valor monetário do Crédito de Carbono: R${round(valor_da_tonelada(anual),2)}''')


        #Álcool 1.4
        elif (opcao_veiculo == "a1"):
            km = int (input ("Digite sua kilometragem mensal: "))

            consumo = km / 6.7
            emissao = consumo * CO_ALCOOL
            credito = emissao / 1000
            anual = credito * 12

            print (f'''Resultado:
            Toneladas de CO2 por mês: {round(credito, 3)}
            Toneladas de CO2 por ano: {round(anual, 3)}
            Árvores à replantar: {ceil(arvores(anual))}
            Valor monetário do Crédito de Carbono: R${round(valor_da_tonelada(anual),2)}''')


        #Álcool 1.5
        elif (opcao_veiculo == "a2"):
            km = int (input ("Digite sua kilometragem mensal: "))

            consumo = km / 6.1
            emissao = consumo * CO_ALCOOL
            credito = emissao / 1000
            anual = credito * 12

            print (f'''Resultado:
            Toneladas de CO2 por mês: {round(credito, 3)}
            Toneladas de CO2 por ano: {round(anual, 3)}
            Árvores à replantar: {ceil(arvores(anual))}
            Valor monetário do Crédito de Carbono: R${round(valor_da_tonelada(anual),2)}''')


        #Álcool 2.0
        elif (opcao_veiculo == "a3"):
            km = int (input ("Digite sua kilometragem mensal: "))

            consumo = km / 5.7
            emissao = consumo * CO_ALCOOL
            credito = emissao / 1000
            anual = credito * 12

            print (f'''Resultado:
            Toneladas de CO2 por mês: {round(credito, 3)}
            Toneladas de CO2 por ano: {round(anual, 3)}
            Árvores à replantar: {ceil(arvores(anual))}
            Valor monetário do Crédito de Carbono: R${round(valor_da_tonelada(anual),2)}''')


        #Gás Natural
        elif (opcao_veiculo == "gn"):
            km = int (input ("Digite sua kilometragem mensal: "))

            emissao = km * CO_GAS_NATURAL
            credito = emissao / 1000
            anual = credito * 12

            print (f'''Resultado:
            Toneladas de CO2 por mês: {round(credito, 3)}
            Toneladas de CO2 por ano: {round(anual, 3)}
            Árvores à replantar: {ceil(arvores(anual))}
            Valor monetário do Crédito de Carbono: R${round(valor_da_tonelada(anual),2)}''')

 
        elif (opcao_veiculo == "mp"):
            print ("\nRetornando ao Menu\n")
            break

        else:
            print ("@@@ Opção Inválida! @@@")

        opcao_veiculo = input("Digite novamente a opção: ")


#Função Cálculo de emissão de carbono por energia

def calc_energia (CO_ENERGIA, opcao_energia):

    while (True):


        #Energia por KWH / Mês
        if (opcao_energia == "ek"):
            kwh = int (input ("Digite seu uso de Kilowhatts mensal: "))

            emissao = kwh * CO_ENERGIA
            credito = emissao / 1000
            anual = credito * 12

            print (f'''Resultado:
            Toneladas de CO2 por mês: {round(credito, 3)}
            Toneladas de CO2 por ano: {round(anual, 3)}
            Árvores à replantar: {ceil(arvores(anual))}
            Valor monetário do Crédito de Carbono: R${round(valor_da_tonelada(anual),2)}''')


        #Energia por conta
        elif (opcao_energia == "ec"):
            reais = float (input ("Digite o valor da conta de luz desse mês: "))

            conversao = reais / 0.37
            emissao = conversao * CO_ENERGIA
            credito = emissao / 1000
            anual = credito * 12

            print (f'''Resultado:
            Toneladas de CO2 por mês: {round(credito, 3)}
            Toneladas de CO2 por ano: {round(anual, 3)}
            Árvores à replantar: {ceil(arvores(anual))}
            Valor monetário do Crédito de Carbono: R${round(valor_da_tonelada(anual),2)}''')


        elif (opcao_energia == "mp"):
            print ("\nRetornando ao Menu\n")
            break

        else:
            print ("@@@ Opção Inválida! @@@")

        opcao_energia = input("Digite novamente a opção: ")

#Função principal

def main():
    #Valores constantes de emissão de carbono por tipo de combustível

    CO_GASOLINA = float (2.2)
    CO_ALCOOL = float (0.56)
    CO_GAS_NATURAL = float (0.14)
    CO_DIESEL = float (2.8)

    #Valores constantes de emissão de carbono para energia

    CO_ENERGIA = float (0.051)

    opcao = menu()

    while (True):

        if (opcao == "v"):
            print ("\n","Menu de tipo de veículos".center(40, "="))
            menu_veiculos = ("""
            Selecione o tipo de combustível do veículo!!!
            =============================

            [g1] - Gasolina até 1.4
            [g2] - Gasolina 1.5 à 2.0
            [g3] - Gasolina acima de 2.0
            [a1] - Álcool até 1.4
            [a2] - Álcool 1.5 até 2.0
            [a3] - Álcool acima de 2.0
            [gn] - Gás Natural
            [mp] - Voltar ao menu principal

            =============================
            Escolha a operação:""")


            opcao_veiculo = input (dedent (menu_veiculos))

            calc_veiculo(CO_ALCOOL, CO_DIESEL, CO_GAS_NATURAL, CO_GASOLINA, opcao_veiculo = opcao_veiculo)


        elif (opcao == "e"):
            print ("\n","Menu de tipo de energia".center(40, "="))
            menu_energia = ("""
            Selecione o tipo de energia!!!
            =============================

            [ek] - Energia por Kilowhatts
            [ec] - energia por conta de luz
            [mp] - Voltar ao menu principal

            =============================
            Escolha a operação:""")


            opcao_energia = input (dedent (menu_energia))

            calc_energia(CO_ENERGIA, opcao_energia = opcao_energia)

        elif (opcao == "s"):
            print ("\nCálculo finalizado")
            break

        else:
            print ("\n@@@ Opção inválida, por favor coloque uma opção válida @@@")

        opcao = menu()


#Chamando o código
main()
