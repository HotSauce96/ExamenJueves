#Ejercicio de los ciclistas


opcion = 5
listaCiclistas =[]

print("***Lista de ciclistas***")
print("1. Registrar un ciclista")
print("2. Mirar todos los ciclistas")
print("3. Corregir el tiempo del ciclista")
print("4. Eliminar un ciclista")

contadorId = 1

while opcion != 0:
    opcion = int(input("Ingrese un numero del menú: "))
    if opcion == 1:
        ciclista = {}
        ciclista["id"] = contadorId
        contadorId += 1
        ciclista["nombre"] = input("Ingrese el nombre del ciclista: ")
        ciclista["edad"] = int(input("Ingrese por favor la edad del ciclista: "))
        ciclista["pais"] = input("Ingrese el país del ciclista: ")
        ciclista["equipo"] = input("Ingrese el equipo del ciclista: ")
        ciclista["tiempo"] = int(input("Ingrese tiempo en minutos del ciclista: "))
        listaCiclistas.append(ciclista)
    elif opcion == 2:
        print(f"La lista de ciclistas lleva estos ciclistas: {listaCiclistas}")
    elif opcion == 3:
        ciclistaaBuscar = int(input("Ingrese por favor el ciclista para corregir el tiempo "))
        bandera = False
        for ciclistaSeleccionado in listaCiclistas:
            if ciclistaSeleccionado["id"] == ciclistaaBuscar:
                ciclistaSeleccionado["tiempo"] = int(input("Ingrese el nuevo tiempo del ciclista: "))
                bandera = True
                break
            else:
                print("El ciclista no se ha encontrado")
    elif opcion == 4:
        ciclistaaBuscar = int(input("Ingrese por favor ciclista a eliminar: "))
        for ciclistaSeleccionado in listaCiclistas:
            if ciclistaSeleccionado["id"] == ciclistaaBuscar:
               listaCiclistas.remove(ciclistaSeleccionado)
               print(f"La lista de ciclistas a quedado así: {listaCiclistas}" ) 
            else:
                print("El ciclista no se ha encontrado")
    else:
        print("No encuentro el número que escribes ... ")
