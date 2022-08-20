edad= int(input('Digite la edad: '))
if(edad >= 0 and edad<15):
    print(f'niño')
elif(edad >=15 and edad<28):
    print(f'joven')
elif(edad >=28 and edad <60):
    print(f'adulto')
elif(edad >= 60 and edad <110):
    print(f'adulto mayor')
elif(edad >110):
    print(f'Edad incorrecta')
else:
    print(f'no se reconoce la edad')