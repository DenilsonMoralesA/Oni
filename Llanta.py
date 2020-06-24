"""
Este programa muestra en pantalla
cuantas vueltas da una llanda de 50 cm de diametro
en 1 kilometro
14/06/20
"""
print("¿Quieres saber cuantas vueltas da tu llanta en un km?")
radio=float(input("Escribe el radio de tu llanta en cm\n"))
perimetro= (2*3.14159)*radio

perimetro_en_km=perimetro/100000
vueltas_llanta=1/perimetro_en_km
print("Tu llanda da",vueltas_llanta, "vueltas en un kilometro")
