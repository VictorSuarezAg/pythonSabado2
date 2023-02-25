age = float(input('Cual es su edad? '))

if age < 15:
    print(f'Eres un Niño')
elif age >= 15 and age < 28:
    print(f'Eres un Joven')
elif age >= 28 and age < 60:
    print(f'Eres Adulto')
elif age >= 60:
    print(f'Eres un Adulto Mayor')
else:
    print(f'Edad incorrecta')