class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def set_region(self, region):
        if region in self._pais:
            self._region = region    
        else:
            raise ValueError(f'La region {region} no es valida en {self._pais}')


if __name__ == "__main__":
    casilla = CasillaDeVotacion(123, ['CDMX', 'Morelos'])
    print(casilla.region)
    casilla.set_region = 'CDMX'
    print(casilla.region)
    # casilla.set_region = 'Puebla'
    # print(casilla.set_region)