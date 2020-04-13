import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    n1 = 1000
    n2 = 10000
    n3 = 50000
    n4 = 100000
    n5 = 200000
    n6 = 250000

    print(f'Tiempos {n1}')
    comienzo = time.time()
    factorial(n1)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n1)
    final = time.time()
    print(final - comienzo)

    print(f'Tiempos {n2}')
    comienzo = time.time()
    factorial(n2)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n2)
    final = time.time()
    print(final - comienzo)

    print(f'Tiempos {n3}')
    comienzo = time.time()
    factorial(n3)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n3)
    final = time.time()
    print(final - comienzo)

    print(f'Tiempos {n4}')
    comienzo = time.time()
    factorial(n4)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n4)
    final = time.time()
    print(final - comienzo)

    print(f'Tiempos {n5}')
    comienzo = time.time()
    factorial(n5)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n5)
    final = time.time()
    print(final - comienzo)

    print(f'Tiempos {n6}')
    comienzo = time.time()
    factorial(n6)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n6)
    final = time.time()
    print(final - comienzo)