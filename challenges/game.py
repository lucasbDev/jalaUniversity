print("""Você está em uma carvena escura e deve escolher  o túnel #1 ou o túnel #2?""")

tunel = input("> ")

if tunel == "1":
    print("Droga! tem um elfo zumbi nesse túnel")
    print("Qual a ideia??")
    print("1. pular sobre o elfo e correr desesperadamente!.")
    print("2. Voltar para o inicio da caverna!.")

    elfo = input("> ")

    if elfo == "1":
        print("Isso aí, você fugiu do elfo!")
    else: 
        print("Droga! surgiram vários baratas voadoras gigantes!!!, aghhhhhh")
   

elif tunel == "2":
    print("Caraca,  tem um Monster geladinho ali no canto")
    print("Qual a ideia??")
    print("1. Beber sem culpa de ser feliz")
    print("2. Continuar até o final do túnel!.")
    

    decisao = input("> ")

    if decisao == "1" or decisao == "2":
        print("Droga, não é energético")
        print("AGHHHHHHHH")
        print("Você se transformou em um elfo zumbi!!!")
    else:
        print("Voê escolheu bem jovem!!!")
        print("Tome este bolo de jaca de prêmio!")
