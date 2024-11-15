from .Mision import Mision
import time
class MisionGrupal(Mision):
    def __init__(self, nombre, rango, recompensa, miembros_minimos:int):
        super().__init__(nombre, rango, recompensa)
        self.__miembros_minimos = miembros_minimos
        self.__aventureros_asignados = {}
        self.__tipo = "Grupal"
    
    @property
    def aventureros_asignados(self):
        return self.__aventureros_asignados
    
    @property
    def miembros_minimos(self):
        return self.__miembros_minimos
    
    @property
    def tipo(self):
        return self.__tipo
    
    @aventureros_asignados.setter
    def aventureros_asignados(self, aventurero):
        if aventurero.id not in self.aventureros_asignados:
            self.__aventureros_asignados[aventurero.id] = aventurero
        else:
            print(f"El aventurero {aventurero.nombre} ya está asignado a la misión.")

    def asignar_aventureros(self, aventurero):
            self.aventureros_asignados = aventurero
            print(f"Aventurero {aventurero.nombre} asignado a la misión.")
    
    def asignar_aventurero(self, aventurero):
        pass
    
    def realizar_mision(self):
        #Verificar si el número de aventureros es correcto.
        if len(self.aventureros_asignados) < self.miembros_minimos:
            print(f"Error: No hay suficientes aventureros para realizar la misión '{self.nombre}'.")
            return

        #Verificamos que todos cumplan con el rango.
        for key, value in self.aventureros_asignados.items():
            value.calcular_rango()
            if value.rango < self.rango:
                print(f"{value.nombre} no tiene el rango suficiente para la misión '{self.nombre}'.")
                return  # Si uno de los aventureros no tiene el rango bien, abortamos misión.

        #Si todos los aventureros cumplen con el rango, se completa la misión.
        print(f"Misión '{self.nombre}' realizada con éxito.")
        self.completado = True

        #Asignamos a cada aventurero la exp
        for key, value in self.aventureros_asignados.items():
            self.otorgar_experiencia(value)
            self.otorgar_recompensa(value)

    def otorgar_experiencia(self, aventurero):
        if self.rango == 1:
            experiencia_otorgada = 5
        elif self.rango == 2:
            experiencia_otorgada = 10
        elif self.rango == 3:
            experiencia_otorgada = 20
        elif self.rango == 4:
            experiencia_otorgada = 50
        elif self.rango == 5:
            experiencia_otorgada = 100
        else:
            experiencia_otorgada = 0

    def otorgar_recompensa(self, aventurero):
        # Repartir la recompensa equitativamente entre todos los aventureros
        recompensa_por_aventurero = self.recompensa / len(self.aventureros_asignados)
        aventurero.dinero += recompensa_por_aventurero
        print(f'{aventurero.nombre} ha recibido {recompensa_por_aventurero} libras de fenix por completar la misión.')

    def __eq__(self, value):
        if value.miembros_minimos != None:
            return True
        
    def __repr__(self):
        return (f"Nombre: {self.nombre}, Rango: {self.rango}, Recompensa: {self.recompensa}, Miembros Minimos: {self.miembros_minimos}.")