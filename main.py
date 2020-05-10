from tabulate import tabulate

def menu():  
    options={'1':'Suma', 
             '2':'Resta', 
             '3':'Producto', 
             '4':'Divisón', 
             '5':'Raíz cuadrada', 
             '6':'Potencia',
             '7':'Salir'}

    headers = ['Opción', 'Operación']
    print ('Calculadora v1.0\nBeca Digitaliza 2020\n')
    print (tabulate(options.items(), headers = headers, tablefmt="fancy_grid", numalign="center"))
    
    #selection = input('Seleccione una opción: ')
    #s = options[selection]
    #print('Operación seleccionada --> ',s)    