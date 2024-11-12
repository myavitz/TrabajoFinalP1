from .Aventurero import Aventurero

class Guerrero(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, exp, dinero, fuerza:int):
        super().__init__(nombre, id, puntos_habilidad, exp, dinero)
        self.__fuerza = fuerza
        self.__rango = 0
        self.__puntos_habilidad = puntos_habilidad
    
    @property
    def rango(self):
        return self.__rango
    
    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad
    
    @rango.setter
    def rango(self, valor):
        self.__rango = valor
   
    @property
    def fuerza(self):
        return self.__fuerza
    
    def calcular_rango(self):
        habilidadTotal = self.calcular_habilidad_total()
        if  habilidadTotal >= 1 and habilidadTotal <=20:
            self.rango = 1
        elif habilidadTotal >= 21 and habilidadTotal <=40:
            self.rango = 2
        elif habilidadTotal >= 41 and habilidadTotal <=60:
            self.rango = 3
        elif habilidadTotal >= 61 and habilidadTotal <=80:
            self.rango = 4
        else:
            self.rango = 5
    
    
    def calcular_habilidad_total(self):
        return self.__puntos_habilidad + (self.__fuerza)/2
    
    def __repr__(self):
        return f'Aventurero: {self.nombre}, id: {self.id}, Puntos de Habilidad: {self.puntos_habilidad}, Exp: {self.exp}, Dinero: {self.dinero}, Fuerza: {self.fuerza}.'