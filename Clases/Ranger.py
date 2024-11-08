from Clases.Aventurero import Aventurero
from Clases.Mascota import Mascota

class Ranger(Aventurero):
    def __init__(self, nombre, id, puntos_habilidad, exp, dinero, mascota = None):
        super().__init__(nombre, id, puntos_habilidad, exp, dinero)    
        self.__mascota = mascota if isinstance(mascota, Mascota) else None #revisar el tema de la mascota (como definirlo bien)
    
    
    @property
    def mascota(self):
        return self.__mascota
    
    def calcular_habilidad_total(self):
        if self.__mascota:
            return self.__puntos_habilidad + self.__mascota.puntos_habilidad
        return self.__puntos_habilidad
    
    def __repr__(self):
        return f'Aventurero: {self.nombre}, id: {self.id}, Puntos de Habilidad: {self.puntos_habilidad}, Exp: {self.exp}, Dinero: {self.dinero}, Mascota: {self.mascota}.'