from .Aventurero import Aventurero
from .Mascota import Mascota

class Ranger(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, exp, dinero, mascota = None):
        super().__init__(nombre, id, puntos_habilidad, exp, dinero)    
        self.__mascota = mascota
        self.__puntos_habilidad = puntos_habilidad
        self.__rango = 0
        self.__exp = exp
        self.__dinero = dinero
        self.__misiones_completadas = 0
    
    @property
    def misiones_completadas(self):
        return self.__misiones_completadas
    
    @misiones_completadas.setter
    def misiones_completadas(self,):
        self.__misiones_completadas += 1

    @property
    def rango(self):
        return self.__rango
    
    @property
    def exp(self):
        return self.__exp

    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad

    @property
    def mascota(self):
        return self.__mascota
    
    @property
    def dinero(self):
        return self.__dinero
    
    @exp.setter
    def exp(self, valor):
        self.__exp = valor

    @rango.setter
    def rango(self, valor):
        self.__rango = valor

    @dinero.setter
    def dinero(self, valor):
        self.dinero = valor
    
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
        if self.__mascota != None:
            if self.puntos_habilidad <= 80:
                return self.__puntos_habilidad + self.__mascota.puntos_habilidad
        return self.__puntos_habilidad or 0
    
    def __repr__(self):
        return f'Aventurero: {self.nombre}, id: {self.id}, Puntos de Habilidad: {self.puntos_habilidad}, Exp: {self.exp}, Dinero: {self.dinero}, Mascota: {self.mascota}.'