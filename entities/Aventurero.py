from abc import ABC, abstractmethod

class Aventurero(ABC):
    
    def __init__(self, nombre:str, id:int,  puntos_habilidad:int, exp:int, dinero:float):
        self.__nombre = nombre
        self.__id = id
        self.__puntos_habilidad = puntos_habilidad
        self.__exp = exp
        self.__dinero = round(dinero, 2)
        self.__misiones_completadas = 0
    
    
    @property
    def misiones_completadas(self):
        return self.__misiones_completadas


    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def id(self):
        return self.__id
    
    @property
    def puntos_habilidad(self):
        return self.__puntos_habilidad
    
    @property
    def exp(self):
        return self.__exp
    
    @property
    def dinero(self):
        return self.__dinero
    
    @misiones_completadas.setter
    def misiones_completadas(self, value):
        self.__misiones_completadas = value
        
   # @abstractmethod
    #def __str__(self):
     #   pass
    
    @abstractmethod
    def calcular_habilidad_total(self):
        pass
