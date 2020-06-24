import math

altura= 20
angulo= 22
radianes= math.radians(angulo)
tangente= math.tan(radianes)
longitud_sombra= altura/tangente
print(tangente)
print("Longitud de la sombra del edificio: ", longitud_sombra)

