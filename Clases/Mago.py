from Clases.Aventurero import Aventurero

class Mago(Aventurero):
    def __init__(self, nombre, ID, puntos_habilidad, exp, dinero, mana:int):
        super().__init__(nombre, ID, puntos_habilidad, exp, dinero)
        self.__mana = mana
    
    def calcular_habilidad_total(self):
        return self.__puntos_habilidad + self.__mana/10