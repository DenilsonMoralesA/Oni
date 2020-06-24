distancia= 1
#km
diametro= 50
#cm
longitud_llanta= 2*3.1416*(diametro/2)

#Tranformar la longitud a metros
longitud= longitud_llanta/100

resultado= ((distancia*1000)/longitud)

print("Una llanta de 50 cm puede dar" +" "+ str(resultado) +" "+ "vueltas en 1 km")