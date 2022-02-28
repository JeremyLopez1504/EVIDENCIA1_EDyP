from collections import namedtuple
import datetime
from time import monotonic

folio = 1
fecha = datetime
monto = float
Servicio = namedtuple
def Registrar():
    servicio = namedtuple('Servicio',"folio fecha monto ")
    lista_servicio= list()
    cliente = input('Cliente al que se le realizó la venta: ')
    folio = 1
    acumulado = 0
    while True:
        try:
            fecha_str= input('Fecha en la que se realizó el servicio (dd/mm/aaaa): ')
            fecha = datetime.datetime.strptime(fecha_str,"%d/%m/%Y").date()
        except ValueError:
            print('El valor de la fecha que proporcionada no puede ser procesada')
            continue
        except Exception:
            print('Se ha presentado una excepción')
            break
        else:
            while folio !=0:
                folio = int(input('\n Indique el folio del servicio: '))
                if folio ==0:
                    break
                else:
                    monto= float(input('Indique el precio del servicio: '))
                    Servicio = (folio, fecha, monto)
                    lista_servicio.append(Servicio)
                    #faltan más datos
                    acumulado += (monto * 1.16)
                    break
        
def consulta():
    input("Digite el folio del servicio a cosultar: ")
    while folio == True:
        try:
            print(folio)
            print(fecha)
            print("El servicio realizado fue: ", Servicio)
            print("El monto a pagar fue: ", monto)
        except ValueError:
            print("El folio digitado no puede ser procesado")
            continue
        except Exception:
            print("El folio que ingreso es nulo, por favor vuelva a intentarlo")
            break   

def menu():
    print('¿Qué desea hacer?')
    opciones = input('1.-Registrar un servicio(R) \n 2.- Consultar un servicio(C) \n 3.-Consultar los servicios realizados en una fecha específica(CS) \n 4.- Salir(S) \n ------ \n')
    if opciones == '1' or opciones == 'R':
        Registrar()
    if opciones == '2' or opciones == 'C':
        consulta()
    if opciones == '3' or opciones == 'CS':
        consulta( Servicio,)
    if opciones == '4' or opciones == 'S':
        exit()

