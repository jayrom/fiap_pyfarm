
# Inicializar vetores

# Culturas tratadas pela aplicação
culturas = ["Amendoim", "Milho"]

# Insumos necessários para as culturas contempladas
insumos = ["Calcário", "Gesso agrícola", "Nitrogênio", "Fósforo", "Potássio", "Sementes", "Herbicida", "Inseticida", "Fungicida"]

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

print("\n\n\n\n----------------------------------------------------------------------------\n")
print("PyFarm - Fazenda Esperança")
print("\n----------------------------------------------------------------------------\n")
print("PyFarm permite que você gerencie as culturas de amendoim e milho da fazenda, \ne os insumos necessários ao plantio dessas culturas.\n")

menu_principal = -1

while menu_principal != 0:

    print("Menu principal")
    print("--------------")
    print("1. Gerenciar culturas - Inserir, editar e remover culturas")
    print("2. Gerenciar insumos - Listar, inserir, editar e remover insumos")
    print("0. Sair")

    menu_principal = int(input("\nSelecione a opção: "))

    print("\n\n")

    if menu_principal == 1:

        menu_gerenciar = -1

        # Menu Gerenciar culturas

        while menu_gerenciar != 0:

            print("--------------------------------------------------------------\n")
            print("Gerenciar culturas")
            print("------------------")
            print("1. Inserir cultura")
            print("2. Editar cultura")
            print("3. Remover cultura")
            print("9. Voltar")
            print("0. Sair")

            menu_gerenciar = int(input("\nSelecione a opção: "))

            print("\n\n")

            if menu_gerenciar == 1:

                if fazenda_culturas == [True, True]:

                    print("Já há duas culturas cadastradas! Para outras opções, consulte o menu Gerenciar culturas.")
                    input("Pressione Enter para continuar...\n")
                    break

                menu_inserir = -1

                # Menu Inserir cultura

                while menu_inserir != 0:

                    print("--------------------------------------------------------------\n")
                    print("Inserir cultura")
                    print("---------------")
                    print("Permite cadastrar até duas culturas, sendo uma de amendoim e \noutra de milho, em áreas retangulares.")
                    print("\n--------------------------------------------------------------")
                    print("1. " + culturas[0])
                    print("2. " + culturas[1])
                    print("9. Voltar")
                    print("0. Sair")

                    menu_inserir = int(input("\nSelecione a opção: "))

                    print("\n\n")

                    # Cultura amendoim

                    if menu_inserir == 1:

                        print("\nCultura: " + culturas[0])
                        
                        if fazenda_culturas[0]:
                            print("\nCultura já cadastrada! Para outras opções, consulte o menu Gerenciar culturas.")
                            input("Pressione Enter para continuar...\n")
                            menu_inserir = 9
                            break

                        fazenda_culturas[0] = True

                        fazenda_area_amendoim[0] = float(input("Comprimento (m): "))
                        fazenda_area_amendoim[1] = float(input("Largura (m): "))

                        # Cálculo da área disponível para plantio (considerados 90% da área total informada)

                        fazenda_area_amendoim[2] = fazenda_area_amendoim[0] * fazenda_area_amendoim[1]
                        fazenda_area_amendoim[3] = fazenda_area_amendoim[2] * 0.9 / 10000

                        print("\nÁrea total (m2): " + str(fazenda_area_amendoim[2]))
                        print("Área útil (ha): " + str(fazenda_area_amendoim[3]))

                        # Cálculo da quantidade de insumos necessários para a área útil calculada

                        i = 0
                        while i < len(insumos):
                            fazenda_insumos_amendoim[i] = fazenda_area_amendoim[3] * quant_insumos_amendoim[i]
                            print(insumos[i] + ": " + str(fazenda_insumos_amendoim[i]))
                            i += 1

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
                        while j < len(insumos):
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
                        input("Opção inválida. Pressione Enter para continuar...\n")
                        print("\n\n")

            elif menu_gerenciar == 2:

                print("--------------------------------------------------------------\n")
                print("Editar cultura")
                print("\n--------------")

                cultura = -1

                if fazenda_culturas == [True, True]:
                    print("Selecione qual cultura deseja editar:")
                    print("1. " + culturas[0])
                    print("2. " + culturas[1])

                    cultura = int(input("Selecione a cultura a ser editada: "))

                    print("\n\n")

                if fazenda_culturas == [True, False] or cultura == 1:
                    print("Cultura plantada na fazenda:")
                    print("Amendoim - Área de plantio: " + str(fazenda_area_amendoim[3]) + " ha")
                    fazenda_area_amendoim[0] = float(input("Comprimento (m): "))
                    fazenda_area_amendoim[1] = float(input("Largura (m): "))
                    print("Amendoim: " + str(fazenda_culturas[0]) + " - Área útil: " + str(fazenda_area_amendoim[3]) + " ha")
                    print("Insumos necessários para a cultura:")
                    i = 0
                    while i < len(insumos):
                        fazenda_insumos_amendoim[i] = fazenda_area_amendoim[3] * quant_insumos_amendoim[i]
                        print(insumos[i] + ": " + str(fazenda_insumos_amendoim[i]))
                        i += 1

                if fazenda_culturas == [False, True] or cultura == 2:
                    print("Cultura plantada na fazenda:")
                    print("Milho - Área de plantio: " + str(fazenda_area_milho[3]) + " ha")
                    fazenda_area_milho[0] = float(input("Comprimento (m): "))
                    fazenda_area_milho[1] = float(input("Largura (m): "))
                    print("Milho: " + str(fazenda_culturas[1]) + " - Área útil: " + str(fazenda_area_milho[3]) + " ha")
                    print("Insumos necessários para a cultura:")
                    j = 0
                    while j < len(insumos):
                        fazenda_insumos_milho[j] = fazenda_area_milho[3] * quant_insumos_milho[j]
                        print(insumos[j] + ": " + str(fazenda_insumos_milho[j]))
                        j += 1

                if fazenda_culturas == [False, False]:
                    input("Não há culturas cadastradas. Pressione Enter para continuar...\n")

                    print("\n\n")

            elif menu_gerenciar == 3:
                print("Remover cultura")

                if fazenda_culturas == [True, True]:
                    print("Selecione qual cultura deseja remover:")
                    print("1. " + culturas[0])
                    print("2. " + culturas[1])

                    cultura = int(input("Selecione a cultura a ser removida: "))  

                    print("\n\n")

                if fazenda_culturas == [True, False] or cultura == 1:
                    fazenda_culturas[0] = False
                    fazenda_area_amendoim = [0, 0, 0, 0]
                    fazenda_insumos_amendoim = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                
                if fazenda_culturas == [False, True] or cultura == 2:    
                    fazenda_culturas[1] = False
                    fazenda_area_milho = [0, 0, 0, 0]
                    fazenda_insumos_milho = [0, 0, 0, 0, 0, 0, 0, 0, 0]

                else:
                    input("Não há culturas cadastradas. Pressione Enter para continuar...\n")

                    print("\n\n")

            elif menu_gerenciar == 9:
                print("Voltar")
                break

            elif menu_gerenciar == 0:
                menu_principal = 0
                break

            else:
                input("Opção inválida. Pressione Enter para continuar...\n")
                print("\n\n")

    elif menu_principal == 2:

    #Gerencir insumos

        while True:

            menu_insumos = -1

            print("--------------------------------------------------------------\n")
            print("Gerenciar insumos")
            print("-----------------")
            print("1. Listar insumos - Lista de insumos e necessidades cadastrados no sistema")
            print("2. Inserir insumo")
            print("3. Editar insumo")
            print("4. Remover insumo")

            if fazenda_culturas[0] or fazenda_culturas[1]:
                print("5. Recalcular culturas")

            print("9. Voltar")
            print("0. Sair")

            menu_insumos = int(input("\nSelecione a opção: "))

            print("\n\n")

            if menu_insumos == 1:
                print("Listar insumos")
                print("--------------------------------------------------------------")

                i = 0
                while i < len(insumos):
                    print(insumos[i] + ": " + str(quant_insumos_amendoim[i]) + " kg/ha para amendoim e " + str(quant_insumos_milho[i]) + " kg/ha para milho")
                    i += 1  

            elif menu_insumos == 2:
                
                print("Inserir insumo")

                print(len(insumos))

                insumo = input("Insumo: ")
                insumos.append(insumo)
                fazenda_insumos_amendoim.append(0)
                fazenda_insumos_milho.append(0)
                quant_amendoim = float(input("Quantidade para amendoim (kg/ha): "))
                quant_insumos_amendoim.append(quant_amendoim)
                quant_milho = float(input("Quantidade para milho (kg/ha): "))
                quant_insumos_milho.append(quant_milho)

                print(len(insumos))

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

            elif menu_insumos == 5:
                print("Recalcular culturas")

                match fazenda_culturas:

                    case [True, False] | [True, True]:

                        i = 0
                        while i < len(insumos):
                            fazenda_insumos_amendoim[i] = fazenda_area_amendoim[3] * quant_insumos_amendoim[i]
                            print(insumos[i] + ": " + str(fazenda_insumos_amendoim[i]))
                            i += 1

                    case [False, True] | [True, True]: 

                        j = 0
                        while j < len(insumos):
                            fazenda_insumos_milho[j] = fazenda_area_milho[3] * quant_insumos_milho[j]
                            print(insumos[j] + ": " + str(fazenda_insumos_milho[j]))
                            j += 1

                    case [False, False]:

                        print("Não há culturas cadastradas.\nPara inserir uma cultura, selecione a opção 1 no menu principal")

                        print("\n\n")

            elif menu_insumos == 9:
                print("Voltar")
                print("\n\n")
                break

            elif menu_insumos == 0:
                menu_principal = 0
                break

            else:
                input("Opção inválida. Pressione Enter para continuar...\n")
                print("\n\n")

    elif menu_principal == 0:
        break

    else:
        input("Opção inválida. Pressione Enter para continuar...\n")
        print("\n\n")
    
print("\n--------------------------------------------------------------")
print("Agradecemos por utilizar o PyFarm.")
print("--------------------------------------------------------------\n")
