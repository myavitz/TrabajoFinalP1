from abc import ABC, abstractmethod

class Mision(ABC):
    def __init__(self, nombre:str, rango:int, recompensa:float, completado = False):
        self.__nombre = nombre
        self.__rango = rango
        self.__recompensa = recompensa
        self.__completado = completado
    
    @property
    def nombre(self):
        return self.__nombre

    @property
    def rango(self):
        return self.__rango

    @property
    def recompensa(self):
        return self.__recompensa

    @property
    def completado(self):
        return self.__completado

    @completado.setter
    def completado(self, valor):
        if isinstance(valor, bool):
            self.__completado = valor
        else:
            raise ValueError("Tiene que ser un valor booleano")
    
    @abstractmethod
    def asignar_avenurero(self, aventurero):
        pass
