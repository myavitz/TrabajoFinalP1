from Clases.Aventurero import Aventurero

class Guerrero(Aventurero):
    def __init__(self, nombre, ID, puntos_habilidad, exp, dinero, fuerza:int):
        super().__init__(nombre, ID, puntos_habilidad, exp, dinero)
        self.__fuerza = fuerza
    
    def calcular_habilidad_total(self):
        return self.__puntos_habilidad + self.__fuerza