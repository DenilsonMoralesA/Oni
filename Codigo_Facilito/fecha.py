from datetime import date
from datetime import datetime
from datetime import timedelta


#Dia actual 
hoy=date.today()
#Fecha actual
now= datetime.now()
print(hoy)
print(now)

print("El día actual es {}".format(hoy.day))
print("El mes actual es {}".format(hoy.month))
print("El año actual es {}".format(hoy.year))

print("La hora actual es {}".format(now.hour))
print("El segundo actual es {}".format(now.second))

año, mes, dia, hora= input("Introduzca la fecha en formato año mes día hora ").split()
año=int(año)
mes=int(mes)
dia=int(dia)
hora=int(hora)
new_date= datetime(año, mes, dia, hora, 00, 00000)

current=(12*(hoy.year - new_date.year)) +(hoy.month - new_date.month)
print("Has vivido",current,"meses")
