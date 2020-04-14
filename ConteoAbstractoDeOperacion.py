def f(x): 
    
    respuesta = 0 # 1 paso

    for i in range(1000): #1000 pasos
        respuesta += 1

    for i in range(x): #X pasos
        respuesta += x

    for i in range(x): #
        for j in range(x):
            respuesta += 1 #2*X*X = 2*X**2
            respuesta += 1

    return respuesta # 1 + 1000 + X + 2X**2 + 1 = 1002 + X +2X**2


    #Este programa no importa lo que retorna, es un ejemplo de cómo se puede
    #medir complejidad algorítmica con Conteo Abstracto de Operaciones
