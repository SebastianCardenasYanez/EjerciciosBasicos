def invertir_entero():
    n = int(input("Ingrese un número entero: "))
    n = str(n)  # Convertir el entero a una cadena
    n = n[::-1]  # Invertir la cadena
    n = int(n)  # Convertir la cadena invertida a un entero
    print (n)
    return n
invertir_entero()