nombre=input("¿Cuál es tu nombre?\n")
edad=int(input("¿Cuál es tu edad?\n"))
peso= float(input("¿Cuánto pesas?\n"))
autorizacion=input("¿Estas autorizado?\n")

allow= autorizacion=="si"

print("Hola", nombre)
print("Edad", edad)
print("Pesas", peso)
print("Autorizado", allow)

#Linea comentada no se ejecutan

"""
Este es un comentario con 
saltos
de linea
"""