from Misiones.Mision import Mision

class MisionGrupal(Mision):
    def __init__(self, nombre, rango, recompensa, completado, miembros_minimos:int):
        super().__init__(nombre, rango, recompensa, completado)
        self.__miembros_minimos = miembros_minimos
        self.__aventureros_asignados = []