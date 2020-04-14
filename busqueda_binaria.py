import random

def busqueda_binaria(lista, comienzo, final, objetivo, contador):
    
    contador+=1
    print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    
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
    tamano_de_lista = int(input('De qué tamano es la lista: '))
    objetivo = int(input('¿Cuál número quieres encontrar?: '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo, 0)

    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')
    
