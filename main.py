from entities import Aventurero, Guerrero, Mago, Ranger, Mascota, Mision, MisionGrupal, MisionIndividual, Gremio
from utils import pedir_entrada, es_convertible_a_float
import time, random

gremio = Gremio()

def menu():   
    a = True
    while a:
        # Mostrar el menú
        print("\nMenú de opciones:")
        time.sleep(0.1)
        print("1. Registrar Aventurero.")
        time.sleep(0.1)
        print("2. Registrar Misión.")
        time.sleep(0.1)
        print("3. Realizar Misión.")
        time.sleep(0.1)
        print("4. Otras Consultas")
        time.sleep(0.1)
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
    time.sleep(0.8)
    nombre = pedir_entrada("Ingrese el nombre: ")
    time.sleep(0.3)
    c=True
    while c:
        try: 
            id = pedir_entrada("Ingrese un id único: ", tipo_dato = "int")
            if  gremio.verificar_id(id):
                raise ValueError("Error, ese id ya se encuentra registrado.")
            else:
                c=False
        except ValueError as e:
            print(f"Error: {e}")
            time.sleep(0.3)
    time.sleep(0.3)
    clase = pedir_entrada("Ingrese la clase: \n1.Guerrero\n2.Mago\n3.Ranger\n: ", tipo_dato="int", rango=(1, 3))
    time.sleep(0.3)
    puntos_habilidad = pedir_entrada("Ingrese los puntos de habilidad (1-100): ", tipo_dato="int", rango=(1, 100))
    time.sleep(0.3)
    exp = pedir_entrada("Ingrese los puntos de experiencia (número entero): ", tipo_dato="int")
    time.sleep(0.3)
    dinero = pedir_entrada("Ingrese la cantidad de dinero (máximo 2 dígitos después de la coma): ", tipo_dato="float")
    
    if clase == 1:
        time.sleep(0.3)
        fuerza = pedir_entrada("Ingrese la fuerza (1-100): ", tipo_dato="int", rango=(1, 100))
        print(f"Registrando a {nombre} como Guerrero...")
        time.sleep(0.8)
        gremio.registrar_aventurero(nombre, id, clase, puntos_habilidad, exp, dinero, fuerza)
        print(f'¡Aventurero {nombre} registrado con éxito!')
        time.sleep(0.8)
    elif clase == 2:
        time.sleep(0.3)
        mana = pedir_entrada("Ingrese el valor de maná (1-1000): ", tipo_dato="int", rango=(1, 1000))
        print(f"Registrando a {nombre} como Mago...")
        time.sleep(0.8)
        gremio.registrar_aventurero(nombre, id, clase, puntos_habilidad, exp, dinero, None, mana)
        print(f'¡Aventurero {nombre} registrado con éxito!')
        time.sleep(0.8)
    elif clase == 3:
        time.sleep(0.3)
        yn = pedir_entrada("El ranger tiene mascota? (y/n): ")
        if yn == "y":
            time.sleep(0.3)
            nombre_mascota = pedir_entrada("Ingrese el nombre de la mascota: ")
            time.sleep(0.3)
            habilidad_mascota = pedir_entrada("Ingrese los puntos de habilidad de la mascota (1-50): ", tipo_dato="int", rango=(1, 50))
            mascota = Mascota(nombre_mascota, habilidad_mascota)
            print(f"Registrando a {nombre} como Ranger...")
            time.sleep(0.8)
            gremio.registrar_aventurero(nombre, id, clase, puntos_habilidad, exp, dinero, mascota)
            print(f'¡Aventurero {nombre} registrado con éxito!')
            time.sleep(0.8)
        else:
            print("Registrando Aventurero como Ranger sin mascota...")
            time.sleep(0.8)
            gremio.registrar_aventurero(nombre, id, clase, puntos_habilidad, exp, dinero, None)
            print(f'¡Aventurero {nombre} registrado con éxito!')
            time.sleep(0.8)

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
    mision = pedir_entrada("1.Mision Individual\n2.Mision Grupal\nElegir 1 o 2: ", tipo_dato = "int", rango = (1,2))
    if mision == 1:
        print("Las misiones disponibles son:")
        for key, value in gremio.misiones.items():
            if isinstance(value, MisionIndividual):
                print(f"{value} ")
        mision_elegida = pedir_entrada("Elija la mision a completar: ")
        for key, value in gremio.misiones.items():
            if isinstance(value, MisionIndividual):
                if mision_elegida.upper() == value.nombre.upper():
                    print (f"La mision elegida es: {mision_elegida}.")
        print("Elija un aventurero para realizar la mision (elija por ID): ")
        for key, value in gremio.aventureros.items():
            if isinstance(value, (Guerrero, Mago, Ranger)):
                print(f"{value}")
        aventurero_elegido = pedir_entrada("Seleccione el id del aventurero deseado: ",tipo_dato = "int")
        for key, value in gremio.aventureros.items():
            if value.id == aventurero_elegido:
                aventurero_para_mision = gremio.aventureros[aventurero_elegido]
                print(f"El aventurero elegido es: {aventurero_para_mision}")
                time.sleep(0.3)
                print("Intentando Mision")
                time.sleep(1)
                mision_a_realizar = gremio.misiones[mision_elegida]
                mision_a_realizar.asignar_aventurero(aventurero_para_mision)
                mision_a_realizar.realizar_mision()
                aventurero_para_mision.mision_completada()
                time.sleep(0.5)

    elif mision == 2:
        print(f"Las misiones disponibles son: ")
        for key, value in gremio.misiones.items():
            if isinstance(value, MisionGrupal):
                print(f"{value}")
        mision_elegida = pedir_entrada("Elija la mision a completar: ")
        for key, value in gremio.misiones.items():
            if isinstance(value, MisionIndividual):
                if mision_elegida.upper() == value.nombre.upper():
                    print (f"La mision elegida es: {mision_elegida}.")
        print("Elija un aventurero para realizar la mision (elija por ID): ")
        for key, value in gremio.aventureros.items():
            if isinstance(value, (Guerrero, Mago, Ranger)):
                print(f"{value}")
        mision_a_realizar = gremio.misiones[mision_elegida]
        d = True
        while d:
            if len(mision_a_realizar.aventureros_asignados) < mision_a_realizar.miembros_minimos:
                aventurero_elegido = pedir_entrada("Seleccione el id del aventurero deseado: ",tipo_dato = "int")
                aventurero_para_mision = gremio.aventureros[aventurero_elegido]
                mision_a_realizar.asignar_aventureros(aventurero_para_mision)

            else:
                d = False
            
            if len(mision_a_realizar.aventureros_asignados) < mision_a_realizar.miembros_minimos:
                respuesta = pedir_entrada("¿Registrar otro aventurero? (S/N): ", tipo_dato="str").upper()
            if respuesta.upper() != 'S':
                d = False
         
        print("Intentando Mision")
        time.sleep(1)
        mision_a_realizar.realizar_mision()
        time.sleep(0.5)
    

def opcion4():
    print("\nCargando...")
    time.sleep(0.8)
    b = True
    while b:
        print("\nOtras Consultas:")
        time.sleep(0.1)
        print("1. Ver Top 10 Aventureros con más misiones resueltas.")
        time.sleep(0.1)
        print("2. Ver Top 10 Aventureros por mayor Habilidad.")
        time.sleep(0.1)
        print("3. Ver Top 5 Misiones con mayor recompensa.")
        time.sleep(0.1)
        print("4. Volver al Menú.")
        time.sleep(0.1)
        
        opcion = pedir_entrada("Elige una opción (1-4): ", tipo_dato="int", rango=(1, 4))


        if opcion == 1:
            # Ordenar por misiones completadas
            ordenado_misiones = dict(sorted(gremio.aventureros.items(), key=lambda item: (-item[1].misiones_completadas, item[1].nombre.lower())))
            
            top_misiones = list(ordenado_misiones.items())[:10]
    
            # Imprimir los aventureros con índice
            print("Top 5 Aventureros por misiones completadas:")
            for idx, (clave, aventurero) in enumerate(top_misiones, start=1):
                print(f"{idx}. {aventurero.nombre} - Misiones completadas: {aventurero.misiones_completadas}")
                time.sleep(0.3)
        elif opcion == 2:
            ordenado_habilidad = dict(sorted(gremio.aventureros.items(), key=lambda item: (-item[1].puntos_habilidad, item[1].nombre.lower())))
            top_10_habilidad = list(ordenado_habilidad.items())[:10]
            if top_10_habilidad:
                print("Top 10 Aventureros por puntos de habilidad:")
                for idx, (clave, aventurero) in enumerate(top_10_habilidad, start=1):
                    print(f"{idx}. {aventurero.nombre} - Puntos de habilidad: {aventurero.puntos_habilidad}")
                    time.sleep(0.3)
            else:
                print("No hay aventureros para mostrar.")

        elif opcion == 3:
            ordenado_recompensa = dict(sorted(gremio.misiones.items(), key=lambda item: (-item[1].recompensa, item[1].nombre.lower())))
            top_5_recompensa = list(ordenado_recompensa.items())[:5]
            if top_5_recompensa:
                print("Top 5 Misiones por recompensa:")
                for idx, (clave, mision) in enumerate(top_5_recompensa, start=1):
                    print(f"{idx}. {mision.nombre} - Recompensa: {mision.recompensa}")
                    time.sleep(0.3)
            else:
                print("No hay misiones para mostrar.")
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
        #Aventureros y Mascotas
        gremio.registrar_aventurero("Marcelo", 12, 1, 45, 888, 23, 54)
        gremio.registrar_aventurero("Marcela", 22, 2, 62, 455, 2665, None, 544)
        mascota1 = Mascota("Winnie", 35)
        gremio.registrar_aventurero("Jhonnie", 34, 3, 47, 211, 9665, None, None, mascota1)
        gremio.registrar_aventurero("Lucia", 28, 2, 30, 320, 1350, 12, None)
        gremio.registrar_aventurero("Gustavo", 19, 1, 50, 500, 740, 25, 30)
        gremio.registrar_aventurero("Diego", 25, 2, 40, 150, 4700, None, 500)
        gremio.registrar_aventurero("Sofia", 30, 3, 38, 900, 1230, 45, 78, None)
        mascota2 = Mascota("Sombra", 50)
        gremio.registrar_aventurero("Carlos", 33, 3, 55, 270, 890, None, None, mascota2)
        gremio.registrar_aventurero("Ana", 27, 1, 70, 123, 4560, 15, 32)
        gremio.registrar_aventurero("Luis", 20, 2, 34, 750, 3100, None, 420)
        gremio.registrar_aventurero("Elena", 24, 1, 65, 520, 2100, 10, 15)
        mascota3 = Mascota("Relámpago", 40)
        gremio.registrar_aventurero("Miguel", 29, 3, 50, 580, 900, None, None, mascota3)
        gremio.registrar_aventurero("Patricia", 31, 2, 55, 450, 2100, 5, None)
        gremio.registrar_aventurero("Fernando", 26, 1, 60, 610, 950, 18, 20)
        gremio.registrar_aventurero("Alicia", 33, 3, 44, 620, 2700, None, None)  
        mascota4 = Mascota("Neblina", 20)
        gremio.registrar_aventurero("Victor", 28, 3, 41, 320, 740, None, None, mascota4)
        gremio.registrar_aventurero("Gabriel", 22, 1, 57, 700, 810, 22, 35)
        gremio.registrar_aventurero("Monica", 30, 2, 44, 560, 2500, None, 600)
        gremio.registrar_aventurero("Daniel", 35, 3, 60, 1100, 3000, 55, 85)
        mascota5 = Mascota("Ares", 25)
        gremio.registrar_aventurero("Hugo", 34, 3, 49, 930, 4000, None, None, mascota5)

        for aventurero in gremio.aventureros.values():
            misiones_aleatorias = random.randint(0, 30)
            aventurero.misiones_completadas = misiones_aleatorias

        #Misiones Individuales
        gremio.registrar_mision("Mondongo", True, 3, 500)
        gremio.registrar_mision("El Bosque Encantado", True, 2, 1500)
        gremio.registrar_mision("Misión de Rescate", True, 4, 2100)
        gremio.registrar_mision("Protección de Aldea", True, 3, 1250)
        gremio.registrar_mision("Patrulla de Bosque", True, 2, 1100)
        gremio.registrar_mision("Escolta de Caravana", True, 5, 1600)
        gremio.registrar_mision("Expedición al Valle", True, 4, 1800)
        gremio.registrar_mision("Misión de Asalto", True, 3, 1400)
        gremio.registrar_mision("Investigación de Ruinas", True, 5, 2500)
        gremio.registrar_mision("Defensa de Fortaleza", True, 3, 1350)
        gremio.registrar_mision("Caza de Bestias", True, 4, 1900)

        #Misiones Grupales
        gremio.registrar_mision("Ojo de Halcon", False, 4, 2000, 3)
        gremio.registrar_mision("Montaña de la Muerte", False, 5, 4000, 2)
        gremio.registrar_mision("Batalla en el Castillo", False, 4, 2300, 3)
        gremio.registrar_mision("Río de las Sombras", False, 2, 1200, 5)
        gremio.registrar_mision("Templo Perdido", False, 3, 1550, 2)
        gremio.registrar_mision("Isla Fantasma", False, 5, 3000, 4)
        gremio.registrar_mision("Montaña de los Lamentos", False, 4, 1700, 3)
        gremio.registrar_mision("La Cueva Maldita", False, 3, 1450, 5)
        gremio.registrar_mision("Campo de los Caídos", False, 2, 1000, 2)
        gremio.registrar_mision("Pico del Terror", False, 5, 2750, 4)
        gremio.registrar_mision("Fortaleza Oculta", False, 4, 2200, 3)
        return
    
    pruebas()
    main()      