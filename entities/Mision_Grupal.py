from .Mision import Mision

class MisionGrupal(Mision):
    def __init__(self, nombre, rango, recompensa, miembros_minimos:int):
        super().__init__(nombre, rango, recompensa)
        self.__miembros_minimos = miembros_minimos
        self.__aventureros_asignados = []
    
    @property
    def aventureros_asignados(self):
        return self.__aventureros_asignados
    
    @property
    def miembros_minimos(self):
        return self.__miembros_minimos

    @aventureros_asignados.setter
    def aventureros_asignados(self, aventurero):
        self.__aventureros_asignados.append(aventurero)

    def asignar_avenureros(self, aventurero):
        if len(self.aventureros_asignados) < self.miembros_minimos:
            self.asignar_avenureros(aventurero)
            print(f"Aventurero {aventurero} asignado a la misión.")
    
    def asignar_aventurero(self, aventurero):
        pass
    
    def realizar_mision(self, algo: list):
        pass

    def __eq__(self, value):
        if value.miembros_minimos != None:
            return True
        
    def __repr__(self):
        return (f"Nombre: {self.nombre}, Rango: {self.rango}, Recompensa: {self.recompensa}, Miembros Minimos: {self.miembros_minimos}, Completado: {self.completado}")