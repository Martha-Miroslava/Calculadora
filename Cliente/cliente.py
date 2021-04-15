#!/usr/bin/env python

import sys
sys.path.append("gen-py")

from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol
from decimal import Decimal
from simple import Calculadora

transporte = TSocket.TSocket("localhost", 8080)
protocolo = TBinaryProtocol.TBinaryProtocol(transporte)
cliente = Calculadora.Client(protocolo)

transporte.open()
while True:
    print("\n[Cliente]")
    linea = input("a)Suma\nb)Resta\nc)Multiplicacion\nd)division\ne)Salir\nElija una ópcion:")
    try:
        if linea == 'e':
            break
        else:
            if linea == 'a':
                numeroA = input("Numero A: ")
                numeroB = input("Numero B: ")
                numeroA= Decimal(numeroA)
                numeroB= Decimal(numeroB)
                respuesta = cliente.sumar(numeroA,numeroB)
                print(respuesta)
            else:
                if linea =='b':
                    numeroA = input("Numero A: ")
                    numeroB = input("Numero B: ")
                    numeroA= Decimal(numeroA)
                    numeroB= Decimal(numeroB)
                    respuesta = cliente.restar(numeroA,numeroB)
                    print(respuesta)
                else:
                    if linea =='c':
                        numeroA = input("Numero A: ")
                        numeroB = input("Numero B: ")
                        numeroA= Decimal(numeroA)
                        numeroB= Decimal(numeroB)
                        respuesta = cliente.multiplicar(numeroA,numeroB)
                        print(respuesta)
                    else:
                        if linea == 'd':
                            numeroA = input("Numero A: ")
                            numeroB = input("Numero B: ")
                            numeroA= Decimal(numeroA)
                            numeroB= Decimal(numeroB)
                            respuesta = cliente.dividir(numeroA,numeroB)
                            print(respuesta)
                        else:
                            print("Eliga una opcion correcta")
    except:
        print ("Ingrese números")
transporte.close()