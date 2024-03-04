def optenerParteDecimal (num):
    parteEntera = int(num)
    parteDecimal = num - parteEntera
    return parteDecimal


num = float(input("ingrese un numero decimal : "))

perteDecimalResult = optenerParteDecimal(num)
print(f"La parte decimal de {num} es igual a {perteDecimalResult}" )