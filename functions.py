number = 0

def request_number():
    """
    Solicita un numero y luego devuelve dicho numero.
    Si el usuario no ingresa un numero valido:
        1. Devuelve ValueError.
        2. Vuelve a solicitar un numero al usuario.
    Si el usuario ingresa un numero valido, devuelve dicho numero.
    """
    global number
    while True:
        try:
            number = int(input("Ingrese un numero positivo: "))
            if number < 0:
                raise ValueError(f'Usted ingreso un numero negativo: "{number}"')
            return number
        except ValueError as e:
            print(f'Error: {e}. Por favor, ingrese un numero valido: ')

def separate_into_units(n:int)->list:
    """
    Recibe un numero entero.
    Devuelve en una lista la descomposicion de dicho numero.
    """
    string = str(n)
    units = []
    count = 1
    for i in string:
        units.append(int(i + ("0" * (len(string) - count))))
        count += 1
    return units