from Clases.Aventurero import Aventurero
from Clases.Mascota import Mascota

class Ranger(Aventurero):
    def __init__(self, nombre, ID, puntos_habilidad, exp, dinero, mascota = None):
        super().__init__(nombre, ID, puntos_habilidad, exp, dinero)
        #self.__mascota = mascota     
        self.__mascota = mascota if isinstance(mascota, Mascota) else None #revisar el tema de la mascota (como definirlo bien)
    
    def calcular_habilidad_total(self):
        if self.__mascota:
            return self.__puntos_habilidad + self.__mascota.puntos_habilidad
        return self.__puntos_habilidad