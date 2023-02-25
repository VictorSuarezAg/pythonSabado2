mounth = input('Ingrese el mes del año: ')
day = int (input('Ingrese el día del mes: '))

if mounth == 'enero':
    mounth = 1
elif mounth == 'febrero':
    mounth = 2
elif mounth == 'marzo':
    mounth = 3
elif mounth == 'abril':
    mounth = 4
elif mounth == 'mayo':
    mounth = 5
elif mounth == 'junio':
    mounth = 6
elif mounth == 'julio':
    mounth = 7
elif mounth == 'agosto':
    mounth = 8
elif mounth == 'septiembre':
    mounth = 9
elif mounth == 'octubre':
    mounth = 10
elif mounth == 'noviembre':
    mounth = 11
elif mounth == 'diciembre':
    mounth = 12

if mounth <= 3:
    if mounth == 3:
        if day <= 20:
            print(f'La estación es invierno')
        else:
            print(f'La estación es verano')
    else:
        print(f'La estación es invierno')
elif mounth >= 4 and mounth <= 6:
    if mounth == 6:
        if day <= 23:
            print(f'La estación es verano')
        else:
            print(f'La estacion es primavera')
    else:
        print(f'La estación es verano')
elif mounth >= 7 and mounth <= 9:
    if mounth == 9:
        if day <= 21:
            print(f'La estación es primavera')
        else:
            print(f'La estación es otoño')
    else:
         print(f'La estación es primavera')
elif mounth >= 10 and mounth <= 12:
    if mounth == 12:
        if day <= 21:
            print(f'La estación es primavera')
        else:
            print(f'La estación es otoño')
    else:
        print(f'La estación es otoño')