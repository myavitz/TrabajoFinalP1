from Clases import Aventurero, Guerrero, Mago, Ranger, Mascota
from Misiones import Mision, MisionGrupal, MisionIndividual
from Gestion import Gremio

gremio = Gremio()

def menu():
    
   
    a = True
    while a:
        # Mostrar el menú
        print("\nMenú de opciones:")
        print("1. Registrar Aventurero.")
        print("2. Registrar Misioón.")
        print("3. Realizar Misión.")
        print("4. Otras Consultas")
        print("5. Salir.")

        # Solicitar opción del usuario
        try:
            opcion = int(input("Elige una opción (1-5): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

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



def es_convertible_a_float(cadena):
    try:
        float(cadena)  
        return True    
    except ValueError:
        return False




def opcion1():
    print("Ingrese los datos del Aventurero: ")
    nombre = input("Ingrese el nombre: ")
    if  nombre.isdigit():
        raise TypeError("Error: Tipo de dato erróneo.")

    clase = input("Ingrese la clase(Guerrero, Mago o Ranger): ")
    if clase not in ["Guerrero", "Mago", "Ranger"]:
        raise ValueError("Error: Tipo de dato inválido.")
    
    id = input("Ingrese el ID: ")
    if id.isdigit():
       id = int(id)
    else :
        raise TypeError("Error, el valor no es un numero entero positivo.")
    
    puntos_habilidad = input("Ingrese los puntos de habilidad(1-100): ")
    if puntos_habilidad.isdigit():
      puntos_habilidad = int(puntos_habilidad)
    elif puntos_habilidad > 100 or puntos_habilidad < 1:
        raise ValueError
    else:
        raise TypeError("Error, el valor no es un numero entre 1 y 100.")
    
    exp = input("Ingrese los puntos de exp(número entero): ")
    if exp.isdigit():
       exp = int(exp)
    else:
        raise ValueError("Error, valor inválido.")
    
    dinero = input("Ingrese la cantidad de dinero(máximo 2 digitos después de la coma): ")
    if es_convertible_a_float(dinero):
       dinero = round(float(dinero), 2)
    else:
        raise ValueError("El valor ingresado no es válido.")
    
    if clase == "Guerrero":
        fuerza = input("Ingrese la fuerza(1-100): ")
        if not fuerza.isdigit():
            raise ValueError()
        else:
            fuerza = int(fuerza)
            if fuerza > 100 or fuerza < 1:
                raise ValueError()
            else:
                gremio.registrar_aventurero(nombre, clase, id, puntos_habilidad, exp, dinero, fuerza)
    
    elif clase == "Mago":
        
        manaM = input("Ingrese el valor de maná(1-1000): ")
        if not manaM.isdigit():
            raise ValueError()
        else:
            manaM = int(manaM)
            if manaM > 1000 or manaM < 1:
                raise ValueError()
            else:
                gremio.registrar_aventurero(nombre, clase, id, puntos_habilidad, exp, dinero, None, manaM)
    
    
    elif clase == "Ranger":
        yn = input("El ranger tiene mascota? y/n: ")
        if yn not in ["y", "n"]:
            raise ValueError()
        elif yn == "n":
            pass
        elif yn == "y":
            nombre_mascota = input("Ingrese el nombre de la mascota: ")
            if nombre_mascota.isdigit() or es_convertible_a_float(nombre_mascota):
                raise ValueError
            habilidad_mascota = input("Ingrese los puntos de habilidad de la mascota(1-50): ")
            if not habilidad_mascota.isdigit():
                raise ValueError()
            else:
                habilidad_mascota = int(habilidad_mascota)
                if habilidad_mascota > 50 or habilidad_mascota < 1:
                    raise ValueError()
                mascotaR = Mascota(nombre_mascota, habilidad_mascota)
                gremio.registrar_aventurero(nombre, clase, id, puntos_habilidad, exp, dinero, mascotaR)
    

    
                



def opcion2():
    pass

def opcion3():
    pass

def opcion4():
    b = True
    while b:
        print("\nOtras Consultas:")
        print("1. Ver Top 10 Aventureros con más misiones resueltas.")
        print("2. Ver Top 10 Aventureros por mayor Habilidad.")
        print("3. Ver Top 5 Misiones con mayor recompensa.")
        print("4. Volver al Menú.")
        try:
            opcion = int(input("Elige una opción (1-5): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue


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
    menu()

if __name__ == "__main__":
    main()