A = int(input("Ingrese los sets que ha ganado el primer jugador: "))
B = int(input("Ingrese los sets que ha ganado el segundo jugador: "))

# Sabiendo que el jugador A ha ganado m juegos, y el jugador B, n juegos, al periodista le gustaría saber:

# si A ganó el set, o
# si B ganó el set, o
# si el set todavía no termina, o
# si el resultado es inválido (por ejemplo, 8-6 o 7-3).
if A < B :
    if (A < 5) and (B < 5):
        print("Aun el set no se a terminado")
    elif (A < 5) and (B == 5):
        print("El segundo jugador gano el set")
    elif(A == 5) and (B == 6):
        print("Aun el set no se a terminado")
    elif(A == 5) and (B == 7):
        print("El segundo jugador gano el set")
    elif(A == 6) and (B == 7):
        print("El segundo jugador gano el set")
    else:
        print("el resultado es inválido")
elif A > B:
    if (A < 5) and (B < 5):
        print("Aun el set no se a terminado")
    elif (B < 5) and (A == 5):
        print("El segundo jugador gano el set")
    elif(B == 5) and (A == 6):
        print("Aun el set no se a terminado")
    elif(B == 5) and (A == 7):
        print("El segundo jugador gano el set")
    elif(B == 6) and (A == 7):
        print("El segundo jugador gano el set")
    else:
        print("el resultado es inválido")
elif A == B:
    if(A == 5) and (B == 5):
        print("Aun el set no se a terminado")
    elif(A == 6) and (B == 6):
        print("Aun el set no se a terminado")