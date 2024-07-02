def request_number():
    while True:
        try:
            number = int(input("Ingrese un numero positivo: "))
            if number < 0:
                raise ValueError(f'Usted ingreso un numero negativo: "{number}"')
            return number
        except ValueError as e:
            print(f'Error: {e}. Por favor, ingrese un numero valido.')
