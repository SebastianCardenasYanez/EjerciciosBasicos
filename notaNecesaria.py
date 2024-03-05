nota1 = float(input("Ingrese la primera nota del certamen : "))
nota2 = float(input("Ingrese la segunda nota del certamen : "))
notaLab = float(input("Ingrese la nota del laboratorio : "))

notaF = 60
promedio = (notaF - (notaLab * 0.3)) / 0.7
nota3 = 3 * promedio - nota1 - nota2
print(f"la tercera nota que necesita para pasar es {nota3}")

