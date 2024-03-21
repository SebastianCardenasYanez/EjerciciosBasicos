while True:
    try:
        Operando1 = int(input("Ingrese el primer operando: "))
        Operador = input("Ingrese el operador que desea (+, -, /, *): ")
        Operando2 = int(input("Ingrese el segundo operando: "))
        suma = Operando1 + Operando2
        resta = Operando1 - Operando2
        division =Operando1 / Operando2
        multiplicacion = Operando1 * Operando2
        if Operador == "+":
            print(f"{Operando1} + {Operando2} = {suma}")
            break
        elif Operador == "-":
            print(f"{Operando1} - {Operando2} = {resta}")
            break
        elif Operador == "/":
            print(f"{Operando1} / {Operando2} = {division}")
            break
        elif Operador == "*":
            print(f"{Operando1} * {Operando2} = {multiplicacion}")
            break
        else:
            print("Ingreso de forma incorrecta el operador")
    except Exception as error:
        print(f"Ingreso el valor incorrecto {error}")