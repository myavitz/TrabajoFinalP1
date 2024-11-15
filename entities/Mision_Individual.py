from .Mision import Mision

class MisionIndividual(Mision):
    def  __init__(self, nombre, rango, recompensa):
        super().__init__(nombre, rango, recompensa)
        self.__aventurero_asignado = None   
        self.__recompensa = recompensa
        self.__tipo = "Individual"


    @property
    def aventurero_asignado(self):
        return self.__aventurero_asignado
    
    @property
    def recompensa(self):
        return self.__recompensa
    
    @property
    def tipo(self):
        return self.__tipo
    
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
        if self.aventurero_asignado is None:
            raise ValueError("No hay aventurero asignado para realizar la misión.")
        
        self.aventurero_asignado.calcular_rango()
        rango_aventurero = self.aventurero_asignado.rango
        if rango_aventurero >= self.rango:
            self.completado = True
            print("Misión Realizada con Éxito!")
            self.otorgar_recompensas(self.aventurero_asignado)
        else:
            self.aventurero_asignado = None
            raise ValueError("El rango del aventurero es insuficiente para realizar la misión.")

    def otorgar_recompensas(self, aventurero):
        match self.rango:
            case 1:
                experiencia_otorgada = 5
            case 2:
                experiencia_otorgada = 10
            case 3:
                experiencia_otorgada = 20
            case 4:
                experiencia_otorgada = 50
            case 5:
                experiencia_otorgada = 100
            case _:
                experiencia_otorgada = 0

        #Asignamos recompensas al aventurero
        aventurero.exp += experiencia_otorgada
        print(f'{aventurero.nombre} ha ganado {experiencia_otorgada} puntos de experiencia por completar la misión.')
        aventurero.dinero += self.recompensa
        print(f'{aventurero.nombre} ha recibido {self.recompensa} libras de fenix por completar la misión.')

    def __repr__(self):
        return f'Misión: {self.nombre}, Rango: {self.rango}, Recompensa: {self.recompensa}'
    
    def __eq__(self, value):
        if hasattr(self, "aventurero_asignado") and hasattr(value, "aventurero_asignado"):
            if self.aventurero_asignado != value.aventurero_asignado:
                return False
        return True
