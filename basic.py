from main import *
import math

menu()

def operar():
    selection = int(input('Seleccione una opción: '))
    while selection > 0 and selection < 7:
        
    # Suma
        if selection == 1:
            a = float(input('Introduzca el primer valor = '))
            b = float(input('Introduzca el segundo valor = '))
            print ('Resultado = ', a+b)
            selection = int(input('Seleccione otra opción o, si desea salir, pulse 7 >'))
    # Resta
        elif selection == 2:
            a = float(input('Introduzca el primer valor = '))
            b = float(input('Introduzca el segundo valor = '))
            print ('Resultado = ', a-b)
            selection = int(input('Seleccione otra opción o, si desea salir, pulse 7 >'))
    # Multiplicación
        elif selection == 3:
            a = float(input('Introduzca el primer valor = '))
            b = float(input('Introduzca el segundo valor = '))
            print ('Resultado = ', a*b)
            selection = int(input('Seleccione otra opción o, si desea salir, pulse 7 >'))
    # División
        elif selection == 4:
            a = float(input('Introduzca el primer valor = '))
            b = float(input('Introduzca el segundo valor = '))
            # EXCEPCIÓN
            try:
                print ('Resultado = ', a/b)
                selection = int(input('Seleccione otra opción o, si desea salir, pulse 7 >'))
            except ZeroDivisionError:
                print ("No es posible dividir entre 0. Por favor, indique de nuevo los valores.")
    # Raíz cuadrada
        elif selection == 5:
            a = float(input('Introduzca el primer valor = '))
            print ('Resultado = ', math.sqrt(a))
            selection = int(input('Seleccione otra opción o, si desea salir, pulse 7 >'))
    # Potencia
        elif selection == 6:
            a = float(input('Introduzca el primer valor = '))
            b = float(input('Introduzca el segundo valor = '))
            print ('Resultado = ', a**b )
            selection = int(input('Seleccione otra opción o, si desea salir, pulse 7 >'))
    # Salir del programa
        elif selection == 7:
            print('Gracias por utilizar la calculadora')
            end
    
operar()

