#Ley de la Suma

def f(n):

    for i in range(n):
        print(i)

    for i in range(n**2):
        print(i)

    #O(n) + O(n**2) = O(n + n) = O(2n) = O(n)

def f(n):

    for i in range(n):
        print(i)

    for i in range(n**2):
        print(i)

    #O(n) + O(n^2) = O(n + n^2) = O(n^2)
    #Se toma el valor de mayor exponente.


#Ley de la multiplicación

def f(n):

    for i in range(n):

        for j in range(n):
            print(i, j)

    #O(n) * O(n) = O(n*n) = O(n^2)

#Recursividad múltiple

def fibonacci(n):

    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

#O(2**n)