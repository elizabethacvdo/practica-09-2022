#
from firmaDigital import * 
from asimetricaCripto import * 
from verificar import * 

print("Menu")
while(True):
    opcion = input("Ingrese una opcion\n [1] crear archivo \n [2] agregar mensaje al archivo: \n [3] crear llaves \n [4] generar firma para el archivo.\n [5] Verificar validez del mensaje\n [otro] Salir: ")
    if(opcion =="1"):
        with open("archivo.txt",'a') as file:
            file.close()
            print("archivo creado")
    elif(opcion == "2"):
        with open("archivo.txt",'w') as file:
            mensaje = input("ingrese un mesaje: ")
            file.write(mensaje)
            file.close()
    elif(opcion=="3"):
        generarLlaves()
    elif(opcion=="4"):
        with open('archivo.txt','r') as f1:
            mensaje = f1.read()
        mensaje = mensaje.encode()
        signature = firmar(mensaje)
    elif(opcion == "5"):
        with open("archivo.txt",'r') as f1:
            mensaje = f1.read()

        with open('firma.txt','r') as f2:
            firma = f2.read()

        mensaje = mensaje.encode()
        verificar(mensaje,firma)
    else:


        break

