import operaciones.operacion as op  # importo la carpeta y el archivo py
import os  # emporto os para limpiar la cosola

os.system('cls' if os.name == 'nt' else 'clear')  # limpia la consola

print("---- CALCULADORA ----")


while True:
    print("\nMenu calculadora ")
    print("1. - Suma - ")
    print("2. - Resta - ")
    print("3. - Multiplicacion - ")
    print("4. - Divicion - ")
    print("5. - Modulo - ")
    print("6. - Expponente - ")
    print("7. - Salir - ")

    opcion = int(input("\nIngrese una opcion y presiones ENTER "))

    match opcion:
        case 1:
            print("Usted a elegido sumar ")
        case 2:
            print('Usted a elegido "restar".')
        case 3:
            print('Usted a elegido "multiplicacion".')
        case 4:
            print('Ha elegido la opcion "division".')
        case 5:
            print('Ha elegido la opcion "modulo".')
        case 6:
            print('Ha elegido la opcion "exponente".')
        case 7:
            print('Esta saliendo de la calculadora.......".')
            break  # aqui se rompe el bucle
        case _:
            print('Error, opcion invalida vuelva a intentar.')

    valor1 = float(input("\n\tIngrese primer numero : "))
    valor2 = float(input("\tIngrese segundo numero : "))

    match opcion:
        case 1:
            resultado = round(op.sumar(valor1, valor2), 2)
            print(f"\t\t {valor1} + {valor2} = {resultado}")
        case 2:
            resultado = round(op.restar(valor1, valor2), 2)
            print(f"\t\t {valor1} - {valor2} = {resultado}")
        case 3:
            resultado = round(op.multiplicar(valor1, valor2), 2)
            print(f"\t\t {valor1} x {valor2} = {resultado}")
        case 4:
            resultado = round(op.dividir(valor1, valor2), 2)
            print(f"\t\t {valor1} / {valor2} = {resultado}")
        case 5:
            resultado = round(op.modular(valor1, valor2), 2)
            print(f"\t\t {valor1} % {valor2} = {resultado}")
        case 6:
            resultado = round(op.exponente(valor1, valor2), 2)
            print(f"\t\t {valor1} elevado a {valor2} = {resultado}")
