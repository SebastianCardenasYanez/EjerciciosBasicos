def determinarCaracter(caracter):
    if caracter.isalpha():
        if caracter.isupper(): 
            print(f"{caracter} es un letra Mayuscula")
        else: print(f"{caracter} es una letra Minuscula")
    elif caracter.isdigit():
        print(f"{caracter} es un numero")
    else : print(f"{caracter} no es ni numero ni letra")

caracter = input("ingrese un caracter: ")
determinarCaracter(caracter)