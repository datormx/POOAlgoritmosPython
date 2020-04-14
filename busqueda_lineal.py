import random

def busqueda_lineal(lista, objetivo):
    match = False
    contador = 0

    for elemento in lista: #O(n)
        print(f'Paso lineal: {contador}')
        print(elemento)
        contador += 1
        if elemento == objetivo:
            match = True
            break

    return match

if __name__ == "__main__":
    tamano_de_lista = int(input('¿De que tamaño será la lista?: '))
    objetivo = int(input('¿Qué número quieres encontrar?: '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')

    
