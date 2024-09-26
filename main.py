from textwrap import dedent




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

def calc_veiculo(CO_ALCOOL, CO_DIESEL, CO_GAS_NATURAL, CO_GASOLINA, opcao_veiculo, km):

    while (True):
        opcao_veiculo = input (dedent (menu_veiculos))
        
        
        #Gasolina 1.4
        if (opcao_veiculo == "g1"):
            
            consumo = km / 10.6
            emissao = consumo * CO_GASOLINA
            credito = emissao / 1000

            print (f"=== Sua emissão de carbono com um veículo até 1.4 a gasolina foi de {round (emissao, 3)}, o que gerou o crédito em tonelada de CO2 de {round (credito, 3)}. ===")
    
        #Gasolina 1.5
        elif (opcao_veiculo == "g2"):
            
            consumo = km / 9.3
            emissao = consumo * CO_GASOLINA
            credito = emissao / 1000

            print (f"=== Sua emissão de carbono com um veículo 1.5 à 2.0 a gasolina foi de {round (emissao, 3)}, o que gerou o crédito em tonelada de CO2 de {round (credito, 3)}. ===")

        #Gasolina 2.0
        elif (opcao_veiculo == "g3"):
            
            consumo = km / 7.2
            emissao = consumo * CO_GASOLINA
            credito = emissao / 1000

            print (f"=== Sua emissão de carbono com um veículo acima de 2.0 a gasolina foi de {round (emissao, 3)}, o que gerou o crédito em tonelada de CO2 de {round (credito, 3)}. ===")

        #Álcool 1.4
        elif (opcao_veiculo == "a1"):
            
            consumo = km / 6.7
            emissao = consumo * CO_ALCOOL
            credito = emissao / 1000

            print (f"=== Sua emissão de carbono com um veículo até 1.4 a álcool foi de {round (emissao, 3)}, o que gerou o crédito em tonelada de CO2 de {round (credito, 3)}. ===")

        #Álcool 1.5
        elif (opcao_veiculo == "a2"):
            
            consumo = km / 6.1
            emissao = consumo * CO_ALCOOL
            credito = emissao / 1000

            print (f"=== Sua emissão de carbono com um veículo 1.5 à 2.0 a álcool foi de {round (emissao, 3)}, o que gerou o crédito em tonelada de CO2 de {round (credito, 3)}. ===")

        #Álcool 2.0
        elif (opcao_veiculo == "a3"):
            
            consumo = km / 5.7
            emissao = consumo * CO_ALCOOL
            credito = emissao / 1000

            print (f"=== Sua emissão de carbono com um veículo acima de 2.0 a álcool foi de {round (emissao, 3)}, o que gerou o crédito em tonelada de CO2 de {round (credito, 3)}. ===")

        #Gás Natural
        elif (opcao_veiculo == "gn"):
            
            emissao = km * CO_GAS_NATURAL
            credito = emissao / 1000

            print (f"=== Sua emissão de carbono com um veículo a gás natural foi de {round (emissao, 3)}, o que gerou o crédito em tonelada de CO2 de {round (credito, 3)}. === ")

        elif (opcao_veiculo == "mp"):
            print ("\nRetornando ao Menu\n")
            break

        else:
            print ("@@@ Opção Inválida! @@@")   

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

            calc_veiculo(CO_ALCOOL, CO_DIESEL, CO_GAS_NATURAL, CO_GASOLINA)
            

        elif (opcao == "e"):    
            None

        elif (opcao == "s"):
            print ("\nAtendimento finalizado")
            break

        else:
            print ("\n@@@ Operação inválida, por favor coloque uma opção válida @@@")


main()