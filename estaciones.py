mes= input('digite mes: ')

if(mes == 'enero' or mes == 'febrero' or mes == 'marzo'):
    print(f'el mes es {mes} y la estacion es invierno')
elif(mes == 'abril' or mes == 'mayo' or mes == 'junio'):
    print(f'el mes es {mes} y la estacion es primavera')
elif(mes == 'julio' or mes == 'agosto' or mes == 'septiembre'):
    print(f'el mes es {mes} y la estacion es verano')
elif(mes == 'octubre' or mes == 'noviembre' or mes == 'diciembre'):
    print(f'el mes es {mes} y la estacion es primavera')
else: f'no se reconocio mes, digite nuevamente'

mes2= int(input('digite el num de mes correspondiente: 1.Enero \n 2.Febrero  \n 3. Marzo 4.Abril 5.Mayo 6.Junio 7.Julio 8.Agosto 9.Septiembre 10.Octubre  11.Noviembre 12.Diembre:'))

if(mes2 == 1 or mes2 == 2 or mes2 == 3):
    print(f' la estacion es invierno')
elif(mes2 == 4 or mes2 == 5 or mes2 == 6):
    print(f'la estacion es primavera')
elif(mes2 == 7 or mes2 == 8 or mes2 == 9):
    print(f'la estacion es verano')
elif(mes2 == 10 or mes2 == 11 or mes2 == 12):
    print(f'la estacion es primavera')
else: f'no se reconocio mes, digite nuevamente'


## si un usuario ingresa un texto en mayuscula, ingrsarlo como minuscula
## hacer las estaciones con días segun el calendario. Que le pida al cx el mes y el dia
## estudiar ciclos
## hacr validaciones, cuando se pide un  num y se da una letra