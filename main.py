from Clases import Aventurero, Guerrero, Mago, Ranger, Mascota
from Misiones import Mision, MisionGrupal, MisionIndividual
from Gestion import Gremio



def opcion1():
    print("Ingrese los datos del Aventurero: ")
    nombre = input("Ingrese el nombre: ")
    if not isinstance(nombre, str):
        raise TypeError("Error: Tipo de dato erróneo.")

    clase = input("Ingrese la clase(Guerrero, Mago o Ranger): ")
    if clase not in ["Guerrero", "Mago", "Ranger"]:
        raise ValueError("Error: Tipo de dato inválido.")
    
    id = input("Ingrese el ID: ")
    if not isinstance(id, int):
        raise ValueError("Error.")

    pass

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
            pass
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            b = False
            print("Saliendo del submenú..")
        else:
            print("Opción no válida. Intenta de nuevo.")


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



def main():
    menu()

if __name__ == "__main__":
    main()