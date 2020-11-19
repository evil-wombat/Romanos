simbolos = {'M': 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}

tipo5 = ('V', 'D', 'L')
tipo1 = ('I', 'X', 'C', 'M')

restas = ('CD', 'CM', 'XL', 'XC', 'IV', 'IX')

def simbolo_a_entero(romano):
    if isinstance (romano, str) and romano.upper() in simbolos:
        return simbolos[romano.upper()]
    elif isinstance (romano, str):
        raise ValueError ("simbolo {} no permitido". format (romano))
    else:
        raise ValueError ("parametro {} debe ser un string". format (romano))

def orden_magnitud (caracter):
    valor = simbolo_a_entero (caracter)
    return len(str(valor))   

def romano_a_entero (num_romano):

    if not isinstance (num_romano, str):
        raise ValueError ("parametro {} debe ser un string". format  (num_romano))

    suma = 0
    c_repes = 0
    valor_anterior = ""
    om_global = 0
    om_caracter = 0
    ha_habido_resta = False

    for caracter in num_romano:
        om_caracter = orden_magnitud (caracter)
        if caracter == valor_anterior:
            om_global == om_caracter
            if caracter in tipo5:
                raise ValueError('No es romano')
            elif c_repes >= 2:
                raise ValueError ('Demasiadas repes')
            elif ha_habido_resta:
                raise ValueError ('Demasiadas restas')
            c_repes +=1

        elif valor_anterior and simbolo_a_entero (caracter) > simbolo_a_entero (valor_anterior):
            if valor_anterior + caracter not in restas:
                raise ValueError ('Resta no permitida')
            elif c_repes > 0:
                raise ValueError ('Resta tras repeticion no permitida')
            elif ha_habido_resta:
                raise ValueError ('Demasiadas restas')

            ha_habido_resta = True
            suma += -2*simbolo_a_entero(valor_anterior)
            c_repes = 0
        
        else:
            if om_global > om_caracter:
                ha_habido_resta = False
            
            if ha_habido_resta:
                raise ValueError ('Demasiadas restas')

            om_global = om_caracter
            c_repes = 0
                
        suma += simbolo_a_entero (caracter)
        valor_anterior = caracter

    return suma
   
def descomponer (numero):


    millares = int (numero / 1000)
    resto_millares = numero % 1000
    centenas = int (resto_millares / 100)
    resto_centenas = resto_millares % 100
    decenas = int (resto_centenas / 10)
    unidades = resto_centenas % 10

    l = [millares, centenas, decenas, unidades]

    # Varias formas de sacar los numeros ordenados en una lista.
    """
    l = []
    for pot in (1000, 100, 10):
        l.append (numero / pot)
        numero %= pot

    l.append(numero)

    for n in str(numero):
        l.append(int(n))
    
    return [int (n) for n in str(numero)] 
    """
    return l      

lista_millares = ('M',)
lista_centenas = ('C', 'D', 'M')
lista_decenas = ('X', 'L', 'C')
lista_unidades = ('I', 'V', 'X')

lista_ordenes = [lista_unidades, lista_decenas, lista_centenas, lista_millares]

def convertir (ordenes_magnitud):
    contador = 0
    resultado =[]
    for orden in ordenes_magnitud[::-1]:
        resultado.append [procesar_simbolo (orden, lista_ordenes[contador])]
        contador += 1

    return ''.join(reversed(resultado))


def procesar_simbolo (s, clave):
    if s == 9:
        return clave [0] + clave [2]
    elif s >= 5:
        return clave[1] + clave [0] * (s-5 )
    elif s == 4:
        return clave [0] + clave [1]
    else:
        return clave [0] * s      


def arabigo_a_romano (numero):
    if not isinstance (numero, int):
        raise SyntaxError (f"{numero} no es un numero entero")

    if numero > 3999 or numero < 1:
        raise OverflowError (f'{numero} debe estar entre 1 y 3999')

    ordenes_de_magnitud = descomponer (numero)
    romano = convertir (ordenes_de_magnitud)

    return romano