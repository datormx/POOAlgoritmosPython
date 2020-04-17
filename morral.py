def morral(tamano_morral, pesos, valores, n):
    
    print(f't_morral: {tamano_morral}, peso: {pesos[n-1]}, valor: {valores[n-1]}')

    if n == 0 or tamano_morral == 0:
        print('return 0')
        return 0

    if pesos[n - 1] > tamano_morral:
        print('return morral')
        return morral(tamano_morral, pesos, valores, n - 1)    
    
    # valor_1 = valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1)
    # valor_2 = morral(tamano_morral, pesos, valores, n - 1)
    # print(f'Valor 1: {valor_1}, Valor 2: {valor_2}')

    maximo = max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
    morral(tamano_morral, pesos, valores, n - 1))

    print(f'valor maximo: {maximo}')
    print('return max')
    return maximo
    

if __name__ == "__main__":
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 20
    n = len(valores)
    
    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)
    