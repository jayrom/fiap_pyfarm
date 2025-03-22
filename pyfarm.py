#---------------------------------------------------
# fiap_pyfarm
# A simple python application for farmers.
# Por favor, leia o README.md para mais informações.
#---------------------------------------------------

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

# Abertura

print("\n\n\n\n----------------------------------------------------------------------------\n")
print("PyFarm - Fazenda Esperança")
print("\n----------------------------------------------------------------------------\n")
print("PyFarm permite que você gerencie as culturas de amendoim e milho da fazenda, \ne os insumos necessários ao plantio dessas culturas.\n")

menu_principal = -1

while menu_principal != 0:

    #Menu principal

    print("Menu principal")
    print("--------------")
    print("1. Gerenciar culturas - Inserir, editar e remover culturas")
    print("2. Gerenciar insumos - Listar, inserir, editar e remover insumos")
    print("0. Sair")

    menu_principal = int(input("\nSelecione a opção: "))

    print("\n\n")

    if menu_principal == 1:

        menu_gerenciar = -1

        # Usando while / condição aninhados, para facilitar a navegação entre os menus.

        while menu_gerenciar != 0:

            # Menu Gerenciar culturas

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

                # Verifica se já há o limite de culturas cadastradas

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

                    # Trata a opção selecionada, baseada no index da cultura, para evitar repetição de código.

                    if menu_inserir in [1, 2]:
                        cultura_index = menu_inserir - 1
                        cultura_nome = culturas[cultura_index]

                        print("\nCultura: " + cultura_nome)

                        # Verifica se já há uma cultura cadastrada.
                        if fazenda_culturas[cultura_index]:
                            print("\nCultura já cadastrada! Para outras opções, consulte o menu Gerenciar culturas.")
                            input("Pressione Enter para continuar...\n")
                            menu_inserir = 9
                            break

                        # Ativa a cultura no vetor de culturas da fazenda.
                        fazenda_culturas[cultura_index] = True

                        print("Defina a área (m) disponível para o plantio:")

                        if cultura_index == 0:
                            fazenda_area = fazenda_area_amendoim
                            quant_insumos = quant_insumos_amendoim
                            fazenda_insumos = fazenda_insumos_amendoim
                        else:
                            fazenda_area = fazenda_area_milho
                            quant_insumos = quant_insumos_milho
                            fazenda_insumos = fazenda_insumos_milho

                        fazenda_area[0] = float(input("Comprimento (m): "))
                        fazenda_area[1] = float(input("Largura (m): "))

                        # Cálculo da área disponível para plantio (considerados 90% da área total informada)
                        fazenda_area[2] = fazenda_area[0] * fazenda_area[1]
                        fazenda_area[3] = fazenda_area[2] * 0.9 / 10000

                        print("\nCultura cadastrada com sucesso.\n")

                        print("Com base nas dimensões informadas, temos:")
                        print(f"Área total (m2): {fazenda_area[2]:.2f}")
                        print(f"Área útil (ha): {fazenda_area[3]:.2f}")

                        # Cálculo da quantidade de insumos necessários para a área útil calculada
                        print("\nPara essa área, os insumos necessários para um ano são:")

                        for i in range(len(insumos)):
                            fazenda_insumos[i] = fazenda_area[3] * quant_insumos[i]
                            print(f"{insumos[i]}: {fazenda_insumos[i]:.2f}")

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

                if fazenda_culturas != [False, False]:

                    print("--------------------------------------------------------------\n")
                    print("Editar cultura")
                    print("--------------")
                    print("Permite editar as dimensões da área de plantio das culturas cadastradas.")
                    print("\n--------------------------------------------------------------")

                    cultura = -1

                    print("Culturas cadastradas:")
                    if fazenda_culturas[0]:
                        print("1. " + culturas[0])
                    if fazenda_culturas[1]:
                        print("2. " + culturas[1])

                    cultura = int(input("Selecione a cultura a ser editada: "))
                    print("\n\n")

                    # Trata a opção selecionada, baseada no index da cultura, para evitar repetição de código.

                    if cultura in [1, 2]:
                        cultura_index = cultura - 1
                        cultura_nome = culturas[cultura_index]

                        if not fazenda_culturas[cultura_index]:
                            input("Cultura não cadastrada. Pressione Enter para continuar...\n")
                            print("\n\n")
                            break

                        print("\nEditando cultura: " + cultura_nome)

                        # Licença para usar operadores ternários.

                        fazenda_area = fazenda_area_amendoim if cultura_index == 0 else fazenda_area_milho
                        quant_insumos = quant_insumos_amendoim if cultura_index == 0 else quant_insumos_milho
                        fazenda_insumos = fazenda_insumos_amendoim if cultura_index == 0 else fazenda_insumos_milho

                        print(f"Área atual de plantio: {fazenda_area[3]:.2f} ha")

                        print("\nInforme as novas dimensões da área de plantio e ajuste de insumos:")

                        fazenda_area[0] = float(input("Comprimento (m): "))
                        fazenda_area[1] = float(input("Largura (m): "))

                        fazenda_area[2] = fazenda_area[0] * fazenda_area[1]
                        fazenda_area[3] = fazenda_area[2] * 0.9 / 10000
                        print(f"\n{cultura_nome} - Nova área de plantio: {fazenda_area[3]:.2f} ha")

                        print("\nRevisão dos insumos necessários para a cultura:")
                        print("--------------------------------------------------------------")
                        
                        for i in range(len(insumos)):
                            fazenda_insumos[i] = fazenda_area[3] * quant_insumos[i]
                            print(f"{insumos[i]}: {fazenda_insumos[i]:.2f}")

                else:
                    input("Não há culturas cadastradas. Pressione Enter para continuar...\n")
                    print("\n\n")

            elif menu_gerenciar == 3:

                if fazenda_culturas != [False, False]:

                    print("--------------------------------------------------------------\n")
                    print("Remover cultura")
                    print("\n--------------")

                    cultura = -1

                    print("Culturas cadastradas:")
                    if fazenda_culturas[0]:
                        print("1. " + culturas[0])
                    if fazenda_culturas[1]:
                        print("2. " + culturas[1])

                    cultura = int(input("Selecione a cultura a ser removida: "))
                    print("\n\n")

                    if cultura in [1, 2]:

                        cultura_index = cultura - 1
                        cultura_nome = culturas[cultura_index]

                        if not fazenda_culturas[cultura_index]:
                            input("Cultura não cadastrada. Pressione Enter para continuar...\n")
                            print("\n\n")
                            break

                        print("\nCultura: " + cultura_nome)

                        fazenda_culturas[cultura_index] = False

                        fazenda_area = fazenda_area_amendoim if cultura_index == 0 else fazenda_area_milho
                        fazenda_insumos = fazenda_insumos_amendoim if cultura_index == 0 else fazenda_insumos_milho

                        fazenda_area = [0, 0, 0, 0]
                        fazenda_insumos = [0, 0, 0, 0, 0, 0, 0, 0, 0]

                        print(f"Cultura {cultura_nome} removida com sucesso.")
                        input("Pressione Enter para continuar...\n")
                        print("\n\n")

                else:
                    input("Não há culturas cadastradas. Pressione Enter para continuar...\n")
                    print("\n\n")

            elif menu_gerenciar == 9:
                print("Voltar")
                print("\n\n")
                break

            elif menu_gerenciar == 0:
                menu_principal = 0
                break

            else:
                input("Opção inválida. Pressione Enter para continuar...\n")
                print("\n\n")

    elif menu_principal == 2:

        # Usando while / True

        while True:

            #Menu Gerencir insumos

            menu_insumos = -1

            print("--------------------------------------------------------------\n")
            print("Gerenciar insumos")
            print("-----------------")
            print("1. Listar insumos - Lista de insumos e necessidades cadastrados no sistema")
            print("2. Inserir insumo - Prmite cadastrar um novo insumo e suas necessidades")
            print("3. Editar insumo - Permite ajustar as quantidades de insumos cadastrados")
            print("4. Remover insumo - Permite excluir um insumo")

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

                # Inserindo itens em uma lista

                insumo = input("Insumo: ")
                insumos.append(insumo)
                fazenda_insumos_amendoim.append(0)
                fazenda_insumos_milho.append(0)
                quant_amendoim = float(input("Quantidade para amendoim (kg/ha): "))
                quant_insumos_amendoim.append(quant_amendoim)
                quant_milho = float(input("Quantidade para milho (kg/ha): "))
                quant_insumos_milho.append(quant_milho)

                print(f"Insumo {insumo} cadastrado com sucesso")
                print("\nAo inserir um insumo, sugerimos recalcular as culturas para \najustar as quantidades necessárias. Utilize a opção 5 no menu Gerencir insumos.")

            elif menu_insumos == 3:
                print("Editar insumo")
                insumo = input("Insumo: ")

                if insumo in insumos:
                    index = insumos.index(insumo)
                    quant_amendoim = float(input("Quantidade para amendoim (kg/ha): "))
                    quant_insumos_amendoim[index] = quant_amendoim
                    quant_milho = float(input("Quantidade para milho (kg/ha): "))
                    quant_insumos_milho[index] = quant_milho

                    print(f"Insumo {insumo} editado com sucesso")
                    print("\nAo editar um insumo, sugerimos recalcular as culturas para \najustar as quantidades necessárias. Utilize a opção 5 no menu Gerencir insumos.")

                else:
                    print("Insumo não encontrado")

            elif menu_insumos == 4:
                print("Remover insumo")

                # Removendo itens de uma lista

                insumo = input("Insumo: ") 

                if insumo in insumos:
                    index = insumos.index(insumo)
                    insumos.remove(insumo)
                    quant_insumos_amendoim.pop(index)
                    quant_insumos_milho.pop(index)

                    print(f"Insumo {insumo} removido com sucesso")
                    print("\nAo remover um insumo, sugerimos recalcular as culturas para \najustar as quantidades necessárias. Utilize a opção 5 no menu Gerencir insumos.")

                else:
                    print("Insumo não encontrado")

            elif menu_insumos == 5:
                print("Recalcular culturas")

                # Usando match / case

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

# Encerramento

print("\n--------------------------------------------------------------")
print("Agradecemos por utilizar o PyFarm.")
print("--------------------------------------------------------------\n")
