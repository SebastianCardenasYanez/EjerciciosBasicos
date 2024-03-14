def compararPalabras():
    p1 = input("ingrese la primera palabra: ")
    p2 = input("ingrese la segunda palabra: ")
    longitud1 = len(p1)
    longitud2 = len(p2)
    if longitud1 > longitud2:
        print(f"la palabra {p1} es mas larga que {p2} ")
    elif longitud1 < longitud2:
        print(f"la palabra {p2} es mas larga que {p1}")
    else :
        print("ambas palabras son igual de largas")

compararPalabras()