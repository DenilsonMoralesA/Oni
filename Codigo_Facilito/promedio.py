from statistics import * 
print("Bienvenido introduzca sus calificaciones")
español=float(input("Calificación Español\n"))
matematicas=float(input("Calificación Matemáticas\n"))
economia=float(input("Calificación Economía\n"))
programación=float(input("Calificación Programación\n"))
ingles= float(input("Calificación Ingles\n"))
data= [español, matematicas, economia, programación, ingles]
print("{:0.2f}".format(mean(data)))