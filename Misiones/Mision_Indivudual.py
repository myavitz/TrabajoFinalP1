from Misiones.Mision import Mision

class MisionIndividual(Mision):
    def  __init__(self, nombre, rango, recompensa, completado):
        super().__init__(nombre, rango, recompensa, completado)
        self.__aventurero_asignado = None
    
    def asignar_avenurero(self, aventurero):
        pass