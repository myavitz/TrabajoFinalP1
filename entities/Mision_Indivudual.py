from .Mision import Mision

class MisionIndividual(Mision):
    def  __init__(self, nombre, rango, recompensa):
        super().__init__(nombre, rango, recompensa)
        self.__aventurero_asignado = None   
    
    @property
    def aventurero_asignado(self):
        return self.__aventurero_asignado
    
    @aventurero_asignado.setter
    def aventurero_asignado(self, value):
        self.__aventurero_asignado = value

    def asignar_aventurero(self, aventurero):
        if self.aventurero_asignado is None:
            self.aventurero_asignado = aventurero
            print(f'Aventurero {aventurero} asignado a la misión "{self.nombre}".')
        else:
            print("La misión ya tiene un aventurero asignado.")
    
    def realizar_mision(self):
        self.aventurero_asignado.calcular_rango()
        rango_aventurero = self.aventurero_asignado.rango
        if rango_aventurero >= self.rango:
            print("Misión Realizada con Éxito!")
            self.completado = True
        else:
            self.aventurero_asignado = None
            raise ValueError("El rango del aventurero es insuficiente para realizar la misión.")
    
    
    def __repr__(self):
        return f'Misión: {self.nombre}, Rango: {self.rango}, Recompensa: {self.recompensa}, Completada: {self.completado}'
    
    def __eq__(self, value):
        if hasattr(self, "aventurero_asignado") and hasattr(value, "aventurero_asignado"):
            if self.aventurero_asignado != value.aventurero_asignado:
                return False
        return True
