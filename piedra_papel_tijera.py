# programa para simular el juego piedra, papel o tijera

import random

print("----------------------------------------")
print("----- juego piedra, papel o tijera -----")
print("----------------------------------------")

#input


#processing 
j = int(input("dijite su jugada: "))
m = random.randint (1,3)

if (j==1):
    rt = "PIEDRA"
elif (j==2):
    rt = "PAPEL"
elif (j==3):
    rt = "TIJERA"
else:
    rt = "NO ESTA JUGANDO PIEDRA PAPEL O TIJERA"

if (j==m):
    rta = "EMPATE"
else:
    (j==1) and (m==3)
    rta = "GANA EL JUGADOR"
    (j==1) and (m==2)
    rta = "GANA LA MAQUINA"
    (j==2) and (m==1)
    rta = "GANA EL JUGADOR"
    (j==2) and (m==3)
    rta = "GANA LA MAQUINA"
    (j==3) and (m==1)
    rta = "GANA LA MAQUINA"
    (j==3) and (m==2)
    rta = "GANA EL JUGADOR"
    
#output 
print ("usted esta jugando con: "+ str (rt))
print ("usted saco: " + str(j)) 
print ("maquina: " + str(m))
print ("el resultado del juego es: " + str(rta))