'''
Veja também a página com as soluções propostas pela comunidade em ExerciciosFuncoesSolucoes

    Faça um programa para imprimir:

            1
            2   2
            3   3   3
            .....
            n   n   n   n   n   n  ... n

        para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha. 


'''



def canc(n):
    for item in range(n):
        for item_second in range(n):
            print(item+1," ",end="")
            if(item==item_second):break
        print("\n")
    
entrada = int(input("digite o numero a começar"))
canc(entrada)