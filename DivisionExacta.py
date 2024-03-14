dividendo = int(input("Ingrese el dividendo : "))
divisor = int(input("Ingrese el divisor : "))
resto = dividendo % divisor
if resto == dividendo % divisor == 0 :
    print(f"la division es exacta el resto es {resto}")
else :
    print (f"la division no es exacta el resto es {resto}")