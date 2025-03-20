
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

while menu_principal != 0:

    print("\n--------------------------------------------------------------\n")
    print("Menu principal")
    print("--------------")
    print("1. Gerenciar culturas")
    print("2. Gerenciar insumos")
    print("0. Sair")

    menu_principal = int(input("Opção: "))

    if menu_principal == 1:

        menu_gerenciar = -1

        # Menu Gerenciar culturas

        while menu_gerenciar != 0:

            print("\n--------------------------------------------------------------\n")
            print("Gerenciar culturas")
            print("-----------")
            print("1. Inserir cultura")
            print("2. Visualizar/editar cultura")
            print("3. Remover cultura")
            print("9. Voltar")
            print("0. Sair")

            menu_gerenciar = int(input("Opção: "))

            if menu_gerenciar == 1:

                menu_inserir = -1

                # Menu Inserir cultura

                while menu_inserir != 0:
                        
                    print("\n--------------------------------------------------------------\n")
                    print("Inserir cultura")
                    print("-----------")
                    print("1. " + culturas[0])
                    print("2. " + culturas[1])
                    print("9. Voltar")
                    print("0. Sair")

                    menu_inserir = int(input("Opção: "))

                    # Cultura amendoim

                    if menu_inserir == 1:

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

                        i = 0
                        while i < len(insumos):
                            fazenda_insumos_amendoim[i] = fazenda_area_amendoim[3] * quant_insumos_amendoim[i]
                            print(insumos[i] + ": " + str(fazenda_insumos_amendoim[i]))
                            i += 1

                        print(len(fazenda_insumos_amendoim))

                    # Cultura milho

                    elif menu_inserir == 2:

                        print("Cultura: " + culturas[1])

                        fazenda_culturas[1] = True

                        fazenda_area_milho[0] = float(input("Comprimento (m): "))
                        fazenda_area_milho[1] = float(input("Largura (m): "))   

                        # Cálculo da área disponível para plantio (considerados 90% da área total informada)

                        fazenda_area_milho[2] = fazenda_area_milho[0] * fazenda_area_milho[1]
                        fazenda_area_milho[3] = fazenda_area_milho[2] * 0.9 / 10000     

                        print("Área total (m2): " + str(fazenda_area_milho[2]))
                        print("Área útil (ha): " + str(fazenda_area_milho[3]))

                        # Cálculo da quantidade de insumos necessários para a área útil calculada

                        j = 0
                        while j < 8:
                            fazenda_insumos_milho[j] = fazenda_area_milho[3] * quant_insumos_milho[j]
                            print(insumos[j] + ": " + str(fazenda_insumos_milho[j]))
                            j += 1

                    elif menu_inserir == 9:
                        print("Voltar")
                        break

                    elif menu_inserir == 0:
                        menu_gerenciar = 0
                        menu_principal = 0
                        break

                    else:
                        print("Opção inválida")

            elif menu_gerenciar == 2:
                print("Visualizar/editar cultura")

            elif menu_gerenciar == 3:
                print("Remover cultura")

            elif menu_gerenciar == 9:
                print("Voltar")
                break

            elif menu_gerenciar == 0:
                menu_principal = 0
                break

            else:
                print("Opção inválida")

    elif menu_principal == 2:

    #Gerencir insumos

        while True:

            menu_insumos = -1

            print("\n--------------------------------------------------------------\n")
            print("Gerenciar insumos")
            print("-----------")
            print("1. Listar insumos")
            print("2. Inserir insumo")
            print("3. Editar insumo")
            print("4. Remover insumo")
            print("9. Voltar")
            print("0. Sair")

            menu_insumos = int(input("Opção: "))

            if menu_insumos == 1:
                print("Listar insumos")

                i = 0
                while i < len(insumos):
                    print(insumos[i] + ": " + str(quant_insumos_amendoim[i]) + " kg/ha para amendoim e " + str(quant_insumos_milho[i]) + " kg/ha para milho")
                    i += 1  

            elif menu_insumos == 2:
                
                print("Inserir insumo")

                insumo = input("Insumo: ")
                insumos.append(insumo)
                quant_amendoim = float(input("Quantidade para amendoim (kg/ha): "))
                quant_insumos_amendoim.append(quant_amendoim)
                quant_milho = float(input("Quantidade para milho (kg/ha): "))
                quant_insumos_milho.append(quant_milho)

            elif menu_insumos == 3:
                print("Editar insumo")
                insumo = input("Insumo: ")
                if insumo in insumos:
                    index = insumos.index(insumo)
                    quant_amendoim = float(input("Quantidade para amendoim (kg/ha): "))
                    quant_insumos_amendoim[index] = quant_amendoim
                    quant_milho = float(input("Quantidade para milho (kg/ha): "))
                    quant_insumos_milho[index] = quant_milho
                else:
                    print("Insumo não encontrado")

            elif menu_insumos == 4:
                print("Remover insumo")
                insumo = input("Insumo: ") 
                if insumo in insumos:
                    index = insumos.index(insumo)
                    insumos.remove(insumo)
                    quant_insumos_amendoim.pop(index)
                    quant_insumos_milho.pop(index)
                else:
                    print("Insumo não encontrado")

            elif menu_insumos == 9:
                print("Voltar")
                break

            elif menu_insumos == 0:
                menu_principal = 0
                break


    elif menu_principal == 0:
        break

    else:
        print("Opção inválida")
    
print("\n--------------------------------------------------------------")
print("Agradecemos por utilizar o PyFarm.")
print("--------------------------------------------------------------\n")
