from Clases.Aventurero import Aventurero

class Mago(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, exp, dinero, mana:int):
        super().__init__(nombre, id, puntos_habilidad, exp, dinero)
        self.__mana = mana
    
    @property
    def mana(self):
        return self.__mana
    
    
    def calcular_habilidad_total(self):
        return self.__puntos_habilidad + self.__mana/10
    
    def __repr__(self):
        return f'Aventurero: {self.nombre}, id: {self.id}, Puntos de Habilidad: {self.puntos_habilidad}, Exp: {self.exp}, Dinero: {self.dinero}, Mana: {self.mana}.'