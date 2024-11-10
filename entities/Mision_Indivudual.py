from .Mision import Mision

class MisionIndividual(Mision):
    def  __init__(self, nombre, rango, recompensa):
        super().__init__(nombre, rango, recompensa)
        self.__aventurero_asignado = None   
    
    @property
    def aventurero_asignado(self):
        return self.__aventurero_asignado
    
    @aventurero_asignado.setter
    def aventurero_asignado(self, aventurero):
        self.__aventurero_asignado = aventurero

    def asignar_avenurero(self, aventurero):
        if self.aventurero is None:
            self.aventurero = aventurero
            print(f'Aventurero {aventurero} asignado a la misión "{self.nombre}".')
        else:
            print("La misión ya tiene un aventurero asignado.")
    
    def __repr__(self):
        return f'Misión: {self.nombre}, Rango: {self.rango}, Recompensa: {self.recompensa}'