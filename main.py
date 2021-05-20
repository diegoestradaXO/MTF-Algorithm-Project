#Diego Estrada
#18540
#Analisis y Diseño de Algoritmos

def swap_element(my_list, index):
    my_list.insert(0, my_list.pop(index)) #0 porque es la primera pos

def move2front(strng, configuration):
    sequence = []
    total_cost = 0
    for char in strng:
        unit_cost = 0
        print("Solicitud: " + str(char))
        print("Configuración previa a MTF: " + str(configuration))
        for i in configuration:
            if (configuration.index(char) == i):
                unit_cost = i + 1
                swap_element(configuration, configuration.index(char))
                print("Configuración posterior a MTF " + str(configuration))
                print("Costo de operación: : " + str(unit_cost) + "\n")
                total_cost += unit_cost
                sequence.append([configuration[:], unit_cost])
                break

    print("Costo total : " + str(total_cost) + "\n")
    return sequence

print("======  a)  =======\n")
configuration = [0, 1, 2, 3, 4]
request_sequence = [0, 1, 2, 3, 4,0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
move2front(request_sequence, configuration)

print("======  b)  =======\n")
configuration = [0, 1, 2, 3, 4]
request_sequence = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
move2front(request_sequence, configuration)

print("======  c)  =======\n")
print("Respuesta: La secuencia son 20 ceros, y el costo total es 20.\n")
configuration = [0, 1, 2, 3, 4]
request_sequence = [0] * 20
move2front(request_sequence, configuration)

print("======  d)  =======\n")
print("Respuesta: La secuencia es [4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0], y el costo total es 100.\n")
configuration = [0, 1, 2, 3, 4]
request_sequence = [4,3,2,1,0] * 4
move2front(request_sequence, configuration)

print("======  e)  =======\n")
configuration = [0, 1, 2, 3, 4]
request_sequence = [2] * 20
move2front(request_sequence, configuration)
print("¿Cuál es el costo total de acceso para una secuencia de 20 números 3's?")
print("Respuesta: el costo es de 23\n")
print("¿Cual sería la fórmula para calcular el costo de n solicitudes del mismo elemento si éste se encuentra inicialmente en la k-esima posición de la lista de configuración?\n")
print("Respuesta: n + k - 1\n")

def improved_move2front(strng, configuration):
    sequence = []
    total_cost = 0
    for j in range(len(strng)):
        unit_cost = 0
        print("Solicitud: " + str(strng[j]))
        print("Configuración previa a IMTF: " + str(configuration))
        for i in configuration:
            if (configuration.index(strng[j]) == i):
                ocurrences = []
                if (j+i < len(strng)):
                    for ocurrence in range(j+1, j+i+1):
                        ocurrences.append(strng[ocurrence])
                elif (j+i >= len(strng)):
                    for ocurrence in range(j+1, len(strng)):
                        ocurrences.append(strng[ocurrence])

                print("Revisión :" + str(ocurrences))

                if (strng[j] in ocurrences):
                    print("Se mueve al frente")
                    unit_cost = i + 1
                    swap_element(configuration, configuration.index(strng[j]))
                else:
                    unit_cost = i + 1
                    print("No se mueve al frente")
                print("Configuración posterior a IMTF " + str(configuration))
                print("Costo de operacion: " + str(unit_cost) + "\n")
                total_cost += unit_cost
                sequence.append([configuration[:], unit_cost])
                break

    print("costo total: " + str(total_cost) + "\n")
    return sequence

print("======  f)  =======\n")
print("El mejor de los casos, usando IMTF")
configuration = [0, 1, 2, 3, 4]
request_sequence = [0] * 20
improved_move2front(request_sequence, configuration)

print("El peor de los casos, usando IMTF")
configuration = [0, 1, 2, 3, 4]
request_sequence = [4,3,2,1,0] * 4
improved_move2front(request_sequence, configuration)

print("======  g)  =======\n")
print("¿Cuál es la diferencia entre un algoritmo online y uno offline?\n")
print("""
Respuesta: 
Un algoritmo online es aquel que puede realizar procesamiento de su entrada parte por parte en forma serializada, es deicr,
en el orden en que la entrada se alimenta al algoritmo, sin necesidad de tener toda la entrada disponible desde el principio. Por otro lado, 
un algoritmo offline se le es provisto toda la información del problema desde el principio y se le requiere que devuelva una 
respuesta que resuelve el problema en cuestión (Karp, 1992).

\n""")
print("""
¿Cambiarían en algo su desempeño o su comportamiento MTF e IMTF si se usaran como algoritmos online 
(considere el efecto de diferentes secuencias de solicitudes)?\n
""")
print("""
Respuesta: 
Para uno no, para el otro sí. En el caso del MTF no cambaría su desempeño ya que el algoritmo en general solo recibe una solicitud 
a la vez y realiza el movimiento hacia enfrente. En cambio, para el IMTF sí cambiaría el desempeño Y el comportamiento, y esto se debe a que se es necesario acceder a la lista
de solicitudes y hacer el look ahead, y finalmente determinar si el numero se mueve al frete o no.

\n""")

print("""
Investigue y describa al menos un algoritmo adicional que 
sea online y que sirva para atender una secuencia de solicitudes de accesos.\n
""")

print("""
Respuesta:
El insertion sort.
Este algoritmo de ordenamiento realiza iteraciones, tomando solo una entrada por repetición, y así va construyendo al lista final ordenada.
Por cada iteración, este algoritmo quita un elemento, encuentra la ubicación donde pertenece en la lista ordenada, y lo inserta en esea posición. 
Repite todo este proceso hasta que todos los elementos del arreglo estén ordenados. Si bien este algoritmo no mueve los elementos hasta el frente del arreglo, 
los mueve hasta la posición en donde los elementos no se encuentran ordenados.

\n""")

#Referencias
# Karp, Richard M. (1992). "On-line algorithms versus off-line algorithms: How much is it worth to know the future?" (PDF). IFIP Congress (1). 12: 416–429.
