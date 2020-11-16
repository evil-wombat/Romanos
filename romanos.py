simbolos = {'M': 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}

tipo5 = ('V', 'D', 'L')
tipo1 = ('I', 'X', 'C', 'M')

def simbolo_a_entero(romano):
    if isinstance (romano, str) and romano.upper() in simbolos:
        return simbolos[romano.upper()]
    elif isinstance (romano, str):
        raise ValueError ("simbolo {} no permitido". format (romano))
    else:
        raise ValueError ("parametro {} debe ser un string". format (romano))
    

def romano_a_entero (num_romano):

    if not isinstance (num_romano, str):
        raise ValueError ("parametro {} debe ser un string". format  (num_romano))

    suma = 0
    c_repes = 0
    valor_anterior = ""

    for caracter in num_romano:
        if caracter == valor_anterior and caracter in tipo5:
            raise OverflowError(f'Demasiados simbolos de tipo {caracter}')
        
        if caracter == valor_anterior:
            c_repes +=1
            if c_repes > 2:
                raise OverflowError(f'Demasiados simbolos de tipo {caracter}')
                
        suma += simbolo_a_entero (caracter)
        valor_anterior = caracter

    return suma
   
    
        
   
