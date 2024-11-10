from .es_convertible_a_float import es_convertible_a_float

def pedir_entrada(prompt, tipo_dato="str", rango=None):
    while True:
        try:
            entrada = input(prompt)
            if tipo_dato == "str":
                if entrada.isdigit():  # Si es solo un número, considera que no es válido
                    raise ValueError("No puede ser un número.")
                return entrada
            elif tipo_dato == "int":
                if not entrada.isdigit():
                    raise ValueError("Debe ser un número entero.")
                num = int(entrada)
                if rango and (num < rango[0] or num > rango[1]):
                    raise ValueError(f"El número debe estar entre {rango[0]} y {rango[1]}.")
                return num
            elif tipo_dato == "float":
                if not es_convertible_a_float(entrada):
                    raise ValueError("Debe ser un número decimal.")
                return round(float(entrada), 2)
        except ValueError as e:
            print(f"Error: {e}. Inténtalo de nuevo.")