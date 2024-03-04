t = int(input("ingrese la hora actual : "))
h = int(input("ingrese una cantidad de horas : "))

horas =  (t + h) %24
print(f"en {h} horas, el reloj marcara las {horas}")