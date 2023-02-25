level = float(input('Digite el nivel del agua: '))

if level < 200:
    print(f'El nivel esta por debajo de lo recomendado')
elif level >= 200 and level < 450:
    print(f'El nivel del agua es normal')
else:
    print(f'El nivel del agua esta por encima del limite')
