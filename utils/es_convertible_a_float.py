def es_convertible_a_float(cadena):
    try:
        float(cadena)  
        return True    
    except ValueError:
        return False