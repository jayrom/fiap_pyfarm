
# Inicializar vetores

culturas = ["Amendoim", "Milho"]



menu_principal = -1

while menu_principal!=0:

    # Menu principal

    print("\n-------------------------------\n")
    print("Menu principal")
    print("-----------")
    print("1. Gerenciar culturas")
    print("2. Informações meteorológicas")
    print("0. Sair")
    print("\n-------------------------------\n")

    menu_principal = int(input("Opção: "))

    if menu_principal==1:

        menu_gerenciar = -1

        while menu_gerenciar!=0:

            # Menu Gerenciar culturas

            print("\n-------------------------------\n")
            print("Gerenciar culturas")
            print("-----------")
            print("1. Inserir cultura")
            print("2. Visualizar/editar cultura")
            print("3. Remover cultura")
            print("9. Voltar")
            print("0. Sair")
            print("\n-------------------------------\n")

            menu_gerenciar = int(input("Opção-: "))

            print(menu_gerenciar)

            if menu_gerenciar==1:

                menu_inserir = -1

                while menu_inserir!=0:
                        
                    # Menu Inserir cultura

                    print("\n-------------------------------\n")
                    print("Inserir cultura")
                    print("-----------")
                    print("1. " + culturas[0])
                    print("2. " + culturas[1])
                    print("9. Voltar")
                    print("0. Sair")
                    print("\n-------------------------------\n")

                    menu_inserir = int(input("Opção: "))

                    if menu_inserir==1:

                        menu_cultura = -1

                        print("Cultura: " + culturas[0])

                    elif menu_inserir==2:
                        print("Editar cultura")

                    elif menu_inserir==3:
                        print("Remover cultura")

                    elif menu_inserir==9:
                        print("Voltar")
                        break

                    elif menu_inserir==0:
                        print("Sair")
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
                print("Sair")
                menu_principal=0
                break

            else:
                print("Opção inválida")

    elif menu_principal==2:

    #Menu Informações meteorológicas

        print("Informações meteorológicas - em construção")

    elif menu_principal==0:
        print("\n-------------------------------\n")
        print("Agradecemos por utilizar o PyFarm.")
        print("\n-------------------------------\n")
        break

    else:
        print("Opção inválida")
    

