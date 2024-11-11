from entities import Aventurero, Guerrero, Mago, Ranger, Mascota, Mision, MisionGrupal, MisionIndividual, Gremio
from utils import pedir_entrada, es_convertible_a_float
import time

gremio = Gremio()

def menu():   
    a = True
    while a:
        # Mostrar el menú
        print("\nMenú de opciones:")
        time.sleep(0.2)
        print("1. Registrar Aventurero.")
        time.sleep(0.2)
        print("2. Registrar Misión.")
        time.sleep(0.2)
        print("3. Realizar Misión.")
        time.sleep(0.2)
        print("4. Otras Consultas")
        time.sleep(0.2)
        print("5. Salir.")
        # Solicitar opción del usuario
        opcion = pedir_entrada("Elige una opción (1-5): ", tipo_dato="int", rango=(1, 5))
        # Ejecutar la acción correspondiente
        if opcion == 1: 
            opcion1()
        elif opcion == 2:
            opcion2()
        elif opcion == 3:
            opcion3()
        elif opcion == 4:
            opcion4()
        elif opcion == 5:
            a = False
            print("Saliendo del programa...")
        else:
            print("Opción no válida. Intenta de nuevo.")


def opcion1():
    print("\nCargando...")
    time.sleep(1)
    nombre = pedir_entrada("Ingrese el nombre: ")
    time.sleep(0.5)
    id = pedir_entrada("Ingrese un id único: ", tipo_dato = "int")
    time.sleep(0.5)
    clase = pedir_entrada("Ingrese la clase(Guerrero, Mago o Ranger): ")
    time.sleep(0.5)
    puntos_habilidad = pedir_entrada("Ingrese los puntos de habilidad (1-100): ", tipo_dato="int", rango=(1, 100))
    time.sleep(0.5)
    exp = pedir_entrada("Ingrese los puntos de experiencia (número entero): ", tipo_dato="int")
    time.sleep(0.5)
    dinero = pedir_entrada("Ingrese la cantidad de dinero (máximo 2 dígitos después de la coma): ", tipo_dato="float")
    
    if clase.upper() == "GUERRERO":
        time.sleep(0.5)
        fuerza = pedir_entrada("Ingrese la fuerza (1-100): ", tipo_dato="int", rango=(1, 100))
        print(f"Registrando a {nombre} como Guerrero...")
        time.sleep(1)
        gremio.registrar_aventurero(nombre, id, clase, puntos_habilidad, exp, dinero, fuerza)
        print(f'¡Aventurero {nombre} registrado con éxito!')
    elif clase.upper() == "MAGO":
        time.sleep(0.5)
        mana = pedir_entrada("Ingrese el valor de maná (1-1000): ", tipo_dato="int", rango=(1, 1000))
        print(f"Registrando a {nombre} como Mago...")
        time.sleep(1)
        gremio.registrar_aventurero(nombre, id, clase, puntos_habilidad, exp, dinero, None, mana)
        print(f'¡Aventurero {nombre} registrado con éxito!')
    elif clase.upper() == "RANGER":
        time.sleep(0.5)
        yn = pedir_entrada("El ranger tiene mascota? (y/n): ")
        if yn == "y":
            time.sleep(0.5)
            nombre_mascota = pedir_entrada("Ingrese el nombre de la mascota: ")
            time.sleep(0.5)
            habilidad_mascota = pedir_entrada("Ingrese los puntos de habilidad de la mascota (1-50): ", tipo_dato="int", rango=(1, 50))
            mascota = Mascota(nombre_mascota, habilidad_mascota)
            print(f"Registrando a {nombre} como Ranger...")
            time.sleep(1)
            gremio.registrar_aventurero(nombre, id, clase, puntos_habilidad, exp, dinero, mascota)
        else:
            print("Registrando Aventurero como Ranger sin mascota...")
            time.sleep(1)
            gremio.registrar_aventurero(nombre, id, clase, puntos_habilidad, exp, dinero, None)
            print(f'¡Aventurero {nombre} registrado con éxito!')

def opcion2():
    print("\nCargando...")
    time.sleep(1)
    nombre = pedir_entrada("Ingrese el nombre de la Misión: ")
    time.sleep(0.5)
    rango = pedir_entrada("Ingrese el Rango de la Misión (1-5): ", tipo_dato="int", rango=(1, 5))
    time.sleep(0.5)
    recompensa = pedir_entrada("Ingrese la recompensa de la Misión (dinero): ", tipo_dato="float")
    time.sleep(0.5)
    tipo_de_mision = pedir_entrada("La Misión es individual (1) o grupal (2)? ", tipo_dato="int", rango=(1, 2))

    if tipo_de_mision == 1:
        tipo_de_mision = True
        gremio.registrar_mision(nombre, tipo_de_mision, rango, recompensa)
        time.sleep(0.5)
        print("Misión individual registrada con éxito.")
    elif tipo_de_mision == 2:
        tipo_de_mision = False
        time.sleep(0.5)
        miembros_minimos = pedir_entrada("Ingrese la cantidad mínima de miembros (para misión grupal): ", tipo_dato="int", rango=(2, 100))
        gremio.registrar_mision(nombre, tipo_de_mision, rango, recompensa, miembros_minimos)
        time.sleep(0.5)
        print("Misión grupal registrada con éxito.")

def opcion3():
    print("\nCargando...")
    time.sleep(1)
    print ("Seleccione el tipo de mision:")
    mision = pedir_entrada("1.Mision Individual\n2.Mision Grupal\n ", tipo_dato = "int", rango = (1,2))
    if mision == 1:
        for key, value in gremio.misiones.items():
            if isinstance(value, MisionIndividual):
                print(f"Las misiones disponibles son: \n{value}\n")
        mision_elegida = pedir_entrada("Elija la mision a completar: ")
        for key, value in gremio.misiones.items():
            if isinstance(value, MisionIndividual):
                if mision_elegida.upper() == value.nombre.upper():
                    print (f"La mision elegida es: {mision_elegida}.")
        print("Elija un aventurero para realizar la mision (elija por ID): ")
        for key, value in gremio.aventureros.items():
            if isinstance(value, (Guerrero, Mago, Ranger)):
                print(f"\n{value}")
        aventurero_elegido = pedir_entrada("",tipo_dato = "int")
        for key, value in gremio.aventureros.items():
            if value.id == aventurero_elegido:
                print(f"El aventurero elegido es: {gremio.aventureros[aventurero_elegido]}")
                print("Intentando Mision")
                time.sleep(1)


    elif mision == 2:
        for key, value in gremio.misiones.items():
            if isinstance(value, MisionGrupal):
                print(f"Las misiones disponibles son: \n{value}\n")
    

def opcion4():
    b = True
    while b:
        print("\nOtras Consultas:")
        print("1. Ver Top 10 Aventureros con más misiones resueltas.")
        print("2. Ver Top 10 Aventureros por mayor Habilidad.")
        print("3. Ver Top 5 Misiones con mayor recompensa.")
        print("4. Volver al Menú.")
        
        opcion = pedir_entrada("Elige una opción (1-4): ", tipo_dato="int", rango=(1, 4))


        if opcion == 1:
            print(gremio.aventureros)
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            b = False
            print("Saliendo del submenú..")
        else:
            print("Opción no válida. Intenta de nuevo.")

def main():
    try:
        menu()
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        print("Saliendo del programa.")

if __name__ == "__main__":

    def pruebas():  
        gremio.registrar_aventurero("Marcelo", 12, "Guerrero", 45, 888, 23, 54)
        gremio.registrar_aventurero("Marcela", 22,"Mago", 62, 455, 2665, None, 544)
        mascota1 = Mascota("Winnie", 35)
        gremio.registrar_aventurero("Jhonnie", 34,"Ranger", 47, 211, 9665, None, None, mascota1)

        gremio.registrar_mision("Mondongo", True, 3, 500)
        gremio.registrar_mision("Ojo de Halcon", False, 4, 2000, 3)
    
        return
    
    pruebas()
    main()      