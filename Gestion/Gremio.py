from Clases import Aventurero, Guerrero, Mago, Ranger, Mascota
from Misiones import Mision, MisionGrupal, MisionIndividual
from random import randint

class Gremio():
    def __init__(self):
        self.__aventureros = {}
        self.__misiones = {}


    
    @property
    def aventureros(self):
        return self.__aventureros
    
    @property
    def misiones(self):
        return self.__misiones
    
    
    def registrar_aventurero(self, nombre: str, clase: str, id: int, puntos_habilidad: int, exp: int, dinero:float, fuerza:int =None, mana: int = None, mascota: object = None):
        if clase == "Guerrero":
            self.aventureros[id] = Guerrero(nombre, id, puntos_habilidad, exp, dinero, fuerza)
        
        if clase == "Mago":
            self.aventureros[id] = Mago(nombre, id, puntos_habilidad, exp, dinero, mana)
    
        
        if clase == "Ranger":
            self.aventureros[id] = Ranger(nombre, id, puntos_habilidad, exp, dinero, mascota)
        