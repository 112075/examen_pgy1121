asistentes = 100
entrada_vendida = 0
ganancia_total = 0
precio_entrada = 0
listado_asistentes = 0 
precio = 0 

#Precio de las entradas
precio_platinum = 120000
precio_gold = 80000
precio_silver = 50000

asistentes = {
    "23568910": "Juan Salinas",
    "12345678": "Raul Salazar",
    "89123456": "Jose Perez"
}

def comprar_entradas():
     cantidad_entrada = int(input("Ingrese la cantiad de entradas que desea comprar (entre 1 y 3): "))

     if cantidad_entrada < 1 or cantidad_entrada > 3 :
        print("La cantidad de entradas debe ser entre 1 y 3 ")
    
def mostrar_ubicacion_disponibles():
    entrada_disponible = asistentes - entrada_vendida
    print("Quedan", entrada_disponible, "entrada_disponible")

def mostrar_ubicaciones():
    print("Ubicaciones disponible")
    for i in range(100):
        print(f"{i+1}. Vendido")
    else:
        if i < 20:
            print(f"{i+1} Platinum (${precio[1]})")
        elif i < 50:
            print(f"[i+1] Gold (${precio[21]})")
        else:
            print(f"{i+1} Silver (${precio[51]})")


while True:
    print("Menu:")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")

    opcion = int(input("Escoja una opcion: "))

    if opcion == 1:
        comprar_entradas()
    elif opcion == 2:
        mostrar_ubicacion_disponibles()
    elif opcion == 3:
        listado_asistentes()
    elif opcion == 4:
        print("Las ganancia total son de $", ganancia_total)
    elif opcion == 5:
        break
    else:
        print("Ingrese una opcion valida ")  

if opcion == 2:
        ubicacion = int(input("Ingrese el numero de la ubicacion que estima comprar (entre 1 y 100): "))
        if ubicacion in entrada_vendida:
            print("Esta ubicacion esta ocupada, Por Favor , Selecione otra ubicacion ")
        elif ubicacion >= 1 and ubicacion <= 20:
            ganancia_total += precio_platinum
            entrada_vendida.append(ubicacion)
            print("Ha comprado una entrada de platinum en la ubicacion", ubicacion,"Por un total de $", precio_platinum)
        elif ubicacion >= 21 and ubicacion <= 50:
            ganancia_total += precio_gold
            entrada_vendida.append(ubicacion)
            print("Ha comprado una entrada de gold en la ubicacion", ubicacion, "Por un total de $", precio_gold)
        elif ubicacion >=51 and ubicacion <=100:
            ganancia_total += precio_silver
            entrada_vendida.append(ubicacion)
            print("Ha comprado una entrada de silver en la ubicacion", ubicacion, "Por un total de $", precio_silver)
        else:
            print("Ubicacion ocupada. Por favor, ingrese un valor entre 1 y 100 ") 
            
def validar_run(run):
    if run.isdigit() and len (run)== 8:
        return True
    else:
        return False
    
while True:
    run = input("Ingrese el RUN  de la persona que va a ocupar el asiento: ")
    if run.iddigit() and len(run) == 8:
        if run in asistentes:
            asiento = int(input("Ingrese el numero de asiento que has comprado: "))
            if asiento not in asiento:
                asiento[asiento] = run
                print("Registro completo correcto")
            else:
                print("Lo siento, esta ubicacion ya ha sido adquirida")
        else:
            print("Lo siento, no estas en la lista de asistente ")
    else:
        print("Run incorrecto., Por favor, ingrese 8 digitos sin guiones,puntos ni digito verificador 3")  


