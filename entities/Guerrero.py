from .Aventurero import Aventurero

class Guerrero(Aventurero):
    def __init__(self, nombre, puntos_habilidad, exp, dinero, fuerza:int):
        super().__init__(nombre, puntos_habilidad, exp, dinero)
        self.__fuerza = fuerza
    
    @property
    def fuerza(self):
        return self.__fuerza
    
    def calcular_habilidad_total(self):
        return self.__puntos_habilidad + self.__fuerza
    
    def __repr__(self):
        return f'Aventurero: {self.nombre}, id: {self.id}, Puntos de Habilidad: {self.puntos_habilidad}, Exp: {self.exp}, Dinero: {self.dinero}, Fuerza: {self.fuerza}.'