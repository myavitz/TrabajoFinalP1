from Clases import Aventurero, Guerrero, Mago, Ranger, Mascota
from Misiones import Mision, MisionGrupal, MisionIndividual
from random import randint

class Gremio():
    def __init__(self):
        self.__aventureros = {}
        self.__misiones = {}


    def registrar_aventurero(self, nombre: str, clase: str, id: int):
        if clase == "Guerrero":
            aventurero = Guerrero(nombre, id, randint(0, 100), 0, 0, randint(1,100))
            self.__aventureros(aventurero.nombre) = aventurero
        if clase == "Ranger":
            pass
        if clase == "Mago":
            pass