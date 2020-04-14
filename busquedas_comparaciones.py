import random

def busqueda_lineal(lista, objetivo):
    match = False
    contador = 0

    for elemento in lista:        
        contador += 1
        if elemento == objetivo:
            match = True
            break
    
    print(f'Pasos lineal: {contador}')
    return match


def busqueda_binaria(lista, comienzo, final, objetivo, contador):
      
    contador+=1      
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}')
    
    if comienzo > final:
        contador+=1
        print(f'Pasos binaria: {contador}')   
        return False

    medio = (comienzo + final) // 2 #Aplica division sin residuo (enteros)
    contador+=1

    if lista[medio] == objetivo:
        contador+=1
        print(f'Pasos binaria: {contador}')         
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, contador)
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, contador)


if __name__ == "__main__":
    tamano_de_lista = int(input('¿De que tamaño será la lista?: '))
    objetivo = int(input('¿Qué número quieres encontrar?: '))

    lista = sorted([random.randint(0, tamano_de_lista) for i in range(tamano_de_lista)])

    encontrado_lineal = busqueda_lineal(lista, objetivo)
    # print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado_lineal else "no está"} en la lista')

    # lista = sorted(lista)
    encontrado_binaria = busqueda_binaria(lista, 0, len(lista), objetivo, 0)
    # print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado_binaria else "no está"} en la lista')

