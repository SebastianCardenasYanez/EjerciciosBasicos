from time import localtime
def calcularEdad(dus, mus, aus):
    t = localtime()
    dia = t.tm_mday
    mes = t.tm_mon
    año = t.tm_year
    edad = año - aus
    if mes < mus or (mes == mus and dia < dus):
        edad -=1
    return edad

def main():
    print("Ingrse su fecha de nacimineto")
    dus = int(input("Ingrese el dia de su nacimiento: "))
    mus = int(input("Ingrese el numero del mes de su nacimiento: "))
    aus = int(input("Ingrese el año de su nacimiento: "))

    edad = calcularEdad(dus, mus, aus)
    print(f"Usted tiene {edad} años")

if __name__ == "__main__":
    main()

