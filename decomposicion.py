class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._frenos = Frenos(calidad = 'buena')
        self._motor = Motor(cilindros = 4)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en_movimiento'

    def frenar(self, tipo='despacio'):
        if tipo == 'rapida' and self._frenos.calidad == 'buena':
            self._motor.inyecta_gasolina(0)
            self._frenos.friccion(100)
            self._estado = 'en_reposo'

        elif tipo == 'rapida' and self._frenos.calidad == 'regular':
            self.motor.inyecta_gasolina(0)
            self._frenos.friccion(50)

        elif tipo == 'despacio' and self._frenos.calidad == 'buena':
            self.motor.inyecta_gasolina(5)
            self._frenos.friccion(50)

        elif tipo == 'despacio' and self._frenos.calidad == 'regular':
            self.motor.inyecta_gasolina(5)
            self._frenos.friccion(30)
        

class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass


class Frenos:

    def __init__(self, calidad='buena'):
        self.calidad = calidad

    def friccion(self, intensidad):
        pass

    