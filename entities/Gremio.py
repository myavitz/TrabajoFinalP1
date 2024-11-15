from entities import Aventurero, Guerrero, Mago, Ranger, Mascota, MisionGrupal, MisionIndividual

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
    
    
    def registrar_aventurero(self, nombre: str, id: int, clase: int, puntos_habilidad: int, exp: int, dinero:float, fuerza:int =None, mana: int = None, mascota: object = None):
        if clase == 1:
            guerrero = Guerrero(nombre, id, puntos_habilidad, exp, dinero, fuerza)
            self.aventureros[guerrero.id] = guerrero
        
        if clase == 2:
            mago = Mago(nombre, id, puntos_habilidad, exp, dinero, mana)
            self.aventureros[mago.id] = mago
    
        
        if clase == 3:
            rangos = Ranger(nombre, id, puntos_habilidad, exp, dinero, mascota)
            self.aventureros[rangos.id] = rangos

        self.__aventureros = dict(sorted(self.aventureros.items()))

    def registrar_mision(self, nombre:str, tipo_de_mision: bool, rango:int, recompensa:float, miembros_minimos= None):
        if tipo_de_mision:
            mision = MisionIndividual(nombre, rango, recompensa)
            self.misiones[mision.nombre] = mision
        else:
            mision = MisionGrupal(nombre, rango, recompensa, miembros_minimos)
            self.misiones[mision.nombre] = mision

    def verificar_id(self, id: int):
        for key, value in self.aventureros.items():
            if value.id == id:
                return True
        return False