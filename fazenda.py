
print("Fazenda Tião B")
x = 0
while (x == 0):

    plantas = ["amendoim", "alface", "milho", "soja"]

    print("""

    1- Adicionar plantação
    2- Consultar estoque
    3- Remover plantação
    5- Sair      

    """)

    #seleciona = int(input(print("Escolha o que fazer: ")))
    seleciona = int(input("Escolha o que fazer: "))

    if seleciona == 1:  
        (print("voce quer adicionar plantacao "))
        insira = input("digite a cultura para plantacao: ")
        plantas.append(insira)
        print ("Nesta Fazenda teremos = ", "[", *plantas, "]")

    if seleciona == 2:
        (print("voce escolheu ver o que temos no estoque"))
        print ("Nesta Fazenda teremos = ", "[", *plantas, "]")

    if seleciona == 3:
        print("vamos remover uma cultura de plantacao\n")
        print ("Nesta Fazenda temos = ", "[", *plantas, "]\n")
        insira = input ("Digite uma plantacao para remover:")
        plantas.remove(insira)
        print ("Nesta Fazenda teremos = ", "[", *plantas, "]")

    if seleciona == 5:
        print("obrigado por usar o nosso programa")
        x = 1


    if x == 1:
        break


#print (seleciona)

#if seleciona == 1:  (print ("numero 1"))