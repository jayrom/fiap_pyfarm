
# Inicializar vetores

# Culturas tratadas pela aplicação
culturas = ["Amendoim", "Milho"]

# Insumos necessários para as culturas contempladas
insumos = ["Calcário", "Gesso agrícola", "Nitrogênio", "Fósforo", "Potássio", "Semente", "Herbicida", "Inseticida", "Fungicida"]

# Quantidade de insumos necessários para cada cultura, por hectare, por safra
quant_insumos_amendoim = [3000, 800, 0, 65, 45, 150000, 2.5, 1.5, 1.5]
quant_insumos_milho = [3000, 800, 200, 100, 70, 110000, 3, 2, 1.5]

# Culturas plantadas na fazenda
fazenda_culturas = [False, False]

# Características da área para plantio (comprimento, largura, área em m2 e área útil em ha) de amendoim, se houver. 
fazenda_area_amendoim = [0, 0, 0, 0]

# Características da área para plantio (comprimento, largura, área em m2 e área útil em ha) de milho, se houver.
fazenda_area_milho = [0, 0, 0, 0]

# Quantidades de insumos, por hectare útil, por safra, para plantio de amendoim da fazenda, se houver.
fazenda_insumos_amendoim = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Quantidades de insumos, por hectare útil, por safra, para plantio de milho da fazenda, se houver.
fazenda_insumos_milho = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Menu principal

menu_principal = -1

while menu_principal!=0:

    print("\n--------------------------------------------------------------\n")
    print("Menu principal")
    print("--------------")
    print("1. Gerenciar culturas")
    print("2. Informações meteorológicas")
    print("0. Sair")

    menu_principal = int(input("Opção: "))

    if menu_principal==1:

        menu_gerenciar = -1

        while menu_gerenciar!=0:

            # Menu Gerenciar culturas

            print("\n--------------------------------------------------------------\n")
            print("Gerenciar culturas")
            print("-----------")
            print("1. Inserir cultura")
            print("2. Visualizar/editar cultura")
            print("3. Remover cultura")
            print("9. Voltar")
            print("0. Sair")

            menu_gerenciar = int(input("Opção: "))

            if menu_gerenciar==1:

                menu_inserir = -1

                while menu_inserir!=0:
                        
                    # Menu Inserir cultura
                    print("\n--------------------------------------------------------------\n")
                    print("Inserir cultura")
                    print("-----------")
                    print("1. " + culturas[0])
                    print("2. " + culturas[1])
                    print("9. Voltar")
                    print("0. Sair")

                    menu_inserir = int(input("Opção: "))

                    if menu_inserir==1:

                    # Cultura amendoim

                        print("Cultura: " + culturas[0])

                        fazenda_culturas[0] = True

                        fazenda_area_amendoim[0] = float(input("Comprimento (m): "))
                        fazenda_area_amendoim[1] = float(input("Largura (m): "))


                        # Cálculo da área disponível para plantio (considerados 90% da área total informada)

                        fazenda_area_amendoim[2] = fazenda_area_amendoim[0] * fazenda_area_amendoim[1]
                        fazenda_area_amendoim[3] = fazenda_area_amendoim[2] * 0.9 / 10000

                        print("Área total (m2): " + str(fazenda_area_amendoim[2]))
                        print("Área útil (ha): " + str(fazenda_area_amendoim[3]))

                        # Cálculo da quantidade de insumos necessários para a área útil calculada

                        i=0
                        while i<8:
                            fazenda_insumos_amendoim[i] = fazenda_area_amendoim[3] * quant_insumos_amendoim[i]
                            print(insumos[i] + ": " + str(fazenda_insumos_amendoim[i]))
                            i+=1


                    elif menu_inserir==2:
                        print("Cultura: " + culturas[1])

                    elif menu_inserir==9:
                        print("Voltar")
                        break

                    elif menu_inserir==0:
                        menu_gerenciar=0
                        menu_principal=0
                        break
                    else:
                        print("Opção inválida")

            elif menu_gerenciar==2:
                print("Visualizar/editar cultura")

            elif menu_gerenciar==3:
                print("Remover cultura")

            elif menu_gerenciar==9:
                print("Voltar")
                break

            elif menu_gerenciar==0:
                menu_principal=0
                break

            else:
                print("Opção inválida")

    elif menu_principal==2:

    #Menu Informações meteorológicas

        print("Informações meteorológicas - em construção")

    elif menu_principal==0:
        break

    else:
        print("Opção inválida")
    
print("\n--------------------------------------------------------------")
print("Agradecemos por utilizar o PyFarm.")
print("--------------------------------------------------------------\n")
