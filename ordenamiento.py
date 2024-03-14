def menuNumeros():
    print(""" 
                CUANTOS NUMEROS DESEA ORDENAR 
          
                            2
                            3
                            4
          
          """)
    opcion = int(input("\n Seleccione la opcion: "))
    if (opcion == 2 ):
        num1 = int(input("ingrese un numero: ")) 
        num2 = int(input("ingrese un numero: ")) 
        numerosOrden = [num1 , num2]
        numerosOrden.sort()
        print(numerosOrden)
    elif(opcion == 3 ):
        num1 = int(input("ingrese un numero: ")) 
        num2 = int(input("ingrese un numero: ")) 
        num3 = int(input("ingrese un numero: "))
        numerosOrden = [num1 , num2, num3]
        numerosOrden.sort()
        print(numerosOrden)
    elif(opcion == 4 ):
        num1 = int(input("ingrese un numero: ")) 
        num2 = int(input("ingrese un numero: ")) 
        num3 = int(input("ingrese un numero: "))
        num4 = int(input("ingrese un numero: "))
        numerosOrden = [num1 , num2, num3, num4]
        numerosOrden.sort()
        print(numerosOrden)
menuNumeros()

# num1 = int(input("ingrse un numero: ")) 
# num2 = int(input("ingrse un numero: ")) 
# numerosOrden = [num1 , num2]
# numerosOrden.sort()
# print(numerosOrden)


