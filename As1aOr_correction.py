'''
    Instituto Tecnológico de Costa Rica
    Aseguramiento de la calidad de software, IC-6831
    Semestre I,2021
    Profesor : Ignacio Trejos Zelaya

       Estudiantes:

    Erick Alfonso Elizondo Ramírez      2018250453
    Steven Josué Retana Cedeño          2017144537
    Anthony Andrés Ulloa Martínez       2018290801


    Asignación 1a: Programas alrededor del dominio del calendario gregoriano.
'''

# |--------------------------------------------------------------------------|
# |                          Variables Globales                              |
# |--------------------------------------------------------------------------|

# Fecha a partir de la cual se instituye el calendario Gregoriano en Roma
institucion_calendario_gregoriano = 1582
# Arreglo de meses que tienen 31 días completos
meses_31_dias = [1, 3, 5, 7, 8, 10, 12]
# Arreglo de meses que tienen 30 días completos
meses_30_dias = [4, 6, 9, 11]


# |-------------------------------------------------------------------------|
# |                     Requerimientos funcionales                          |
# |-------------------------------------------------------------------------|

# ---------------------- R0 (fecha_es_tupla)---------------------------------

# Definición: Todas las fechas serán creadas como tuplas de
# tres números enteros positivos (ternas),
# en este orden: (año, mes, día).
# El resultado debe ser un valor booleano, True o False.

def fecha_es_tupla(fecha):
    if len(fecha) == 3:
        if type(fecha[0]) == int and type(fecha[1]) == int and type(fecha[2]) == int:
            if fecha[0] >= institucion_calendario_gregoriano:
                if fecha[1] >= 1 and fecha[1] <= 12:
                    if fecha[2] >= 1 and fecha[2] <= 31:
                        return True
    return False


# ---------------------- R1 (bisiesto)---------------------------

# Definición: Dado un año perteneciente al rango permitido,
# determinar si este es bisiesto.
# El resultado debe ser un valor booleano, True o False.

def bisiesto(year):
    if (year % 100) == 0:
        if (year % 400) == 0:
            return True
    else:
        if (year % 4) == 0:
            return True
    return False


# ---------------------- R2 (fecha_es_valida)-------------------------

# Definición: Dada una fecha, determinar si esta es válida
# según el calendario gregoriano.
# El resultado debe ser un valor booleano, True or False

def fecha_es_valida(fecha):
    if (len(fecha) == 3):
        for var in range(len(fecha)):
            if type(fecha[var]) != int or fecha[var] < 0:
                return False
        # Validación si fecha es mayor a la instituida
        if (fecha[0] >= institucion_calendario_gregoriano):
            # Teniendo un año bisiesto, se valida el día
            return validar_dia_mes(fecha[0], fecha[1], fecha[2])
        else:
            return False
    else:
        return False


# Funcion auxiliar en R2 para validar un dia específico del mes
# según si se tienen años válidos o no


def validar_dia_mes(ano, mes, dia):
    if (mes in meses_31_dias and dia >= 1):
        return (dia <= 31)
    elif (mes in meses_30_dias and dia >= 1):
        return (dia <= 30)
    elif (mes == 2 and dia >= 1):
        if bisiesto(ano):
            return (dia <= 29)
        else:
            return (dia <= 28)
    else:
        return False


# ---------------------- R3 (dia_siguiente)-----------------------------

# Definición: Dada una fecha válida, determinar la fecha del dia siguiente.
# El resultado debe ser una fecha válida (tupla de 3 números enteros positivos,
# que corresponde a una fecha en el calendario gregoriano,
# conforme a nuestra convención),
# el resultado debe ser un valor booleano, True or False

def dia_siguiente(fecha):
    # Si fecha ingresada es válida retorna True
    if(fecha_es_valida(fecha)):
        # Comprobación en los respectivos arreglos de meses
        if (fecha[1] in meses_31_dias):
            if (fecha[2] <= 30):
                return (fecha[0], fecha[1], fecha[2]+1)
            else:
                return aumentar_mes(fecha)
        elif (fecha[1] in meses_30_dias):
            if (fecha[2] <= 29):
                return (fecha[0], fecha[1], fecha[2]+1)
            else:
                # Se aumenta sólo el mes de manera normal
                return aumentar_mes(fecha)
        else:
            # Se aumenta el día o mes considerando bisiestos
            return aumentar_bisiesto(fecha)
    else:
        return "La fecha ingresada es inválida"


# Funcion auxiliar en R3 para aumentar el mes en la fecha
def aumentar_mes(fecha):
    if (fecha[1] < 12):
        return (fecha[0], fecha[1] + 1, 1)
    return (fecha[0] + 1, 1, 1)


# Funcion auxiliar en R3 para aumentar el día según si el año es bisiesto o no
def aumentar_bisiesto(fecha):
    if (bisiesto(fecha[0])):
        if (fecha[2] < 29):
            return (fecha[0], fecha[1], fecha[2] + 1)
        else:
            return aumentar_mes(fecha)
    else:
        if (fecha[2] < 28):
            return (fecha[0], fecha[1], fecha[2]+1)
        else:
            return aumentar_mes(fecha)

# ---------------------- R4 (ordinal_dia)-------------------------

# Definición: Dada una fecha válida (año,mes,día), determinar cuál
# es la posición de esa fecha dentro del año.
# Por ejemplo: ordinal_dia(2021,1,1)=1, ordinal_dia(2020,3,1)=61,
# ordinal_dia(2020,2,29)
# Note que corresponde a 1 + el número de días transcurridos desde
# el primero de enero de ese año,
# El resultado debe ser un mínimo entero


def ordinal_dia(fecha):
    if fecha_es_valida(fecha):
        # Lista generada a partir de días que hay al mes
        meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        cantidad_dias = 0
        if bisiesto(fecha[0]):  # En caso de ser bisiesto, modificar febrero
            meses[1] = 29
        for i in range(fecha[1]-1):  # Sumar días hasta el último mes
            cantidad_dias += meses[i]
        return cantidad_dias + fecha[2]  # Sumar los días restantes
    else:
        # Si devuelve 0, es una fecha no válida
        return "La fecha ingresada es inválida"


# ---------------------- R5 (dia_semana)--------------------------------

# Definición: Dada una fecha válida, determinar el día de la semana,
# con la siguiente codificación:
# 0 = domingo, 1 = lunes, 2 = martes, 3 = miércoles,
# 4 = jueves, 5 = viernes, 6 = sabado
# El resultado debe ser un mínimo entero, conforme a la codificación indicada

# El requerimiento R5 (dia_semana) fue basado en esta página:
# https://artofmemory.com/blog/how-to-calculate-the-day-of-the-week-4203.html
# el cuál está basado de este libro "Mind Performance Hacks" por Ron Hale-Evans
# Utiliza la fórmula
# (Year Code + Month Code + Century Code + Date Number – Leap Year Code) mod 7


def dia_semana(fecha):
    if(fecha_es_valida(fecha)):
        year_code = yearCode(fecha[0])
        month_code = monthCode(fecha[1])
        century_code = centuryCode(fecha[0])
        dia = fecha[2]
        # si es bisiesto se le resta en 1 antes de hacer mod 7,
        # pero es lo mismo restárselo al día
        # esto en caso de que sea Enero o Febrero
        if bisiesto(fecha[0]) and (fecha[1] == 1 or fecha[1] == 2):
            dia -= 1
        return ((year_code + month_code + century_code + dia) % 7)
    else:
        # En caso de que la fecha no es válida
        return "La fecha ingresada es inválida"


# Utiliza (YY + (YY div 4)) mod 7, siendo YY los primeros 2 dígitos del año


def yearCode(year):
    year = year % 100
    return (year + (year // 4)) % 7

# De acuerdo al mes, se obtiene un número necesario para la fórmula


def monthCode(month):
    codeList = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    return codeList[month-1]


# Dependiendo del siglo de un año dado,
# se obtiene otro número utilizado en la fórmula,
# cabe recalcar que estos códigos es para el calendario Gregoriano,
# en el Juliano es distinto


def centuryCode(year):
    if year < 1800:
        return 4
    elif year < 1900:
        return 2
    elif year < 2000:
        return 0
    elif year < 2100:
        return 6
    elif year < 2200:
        return 4
    elif year < 2300:
        return 2
    else:
        return 0

# |--------------------------------------------------------------------------|
# |                              Pruebas                                     |
# |--------------------------------------------------------------------------|


# ---------------------- R0 (fecha_es_tupla)---------------------------------


def pruebaR0():
    print("\n-------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R0 (fecha_es_tupla):\n")
    fecha1 = (1900, 12, 29)         # Resultado: true
    fecha2 = (1, 12, 31)              # Resultado: false
    fecha3 = ("Hola mundo", 2, 28)    # Resultado: false
    fecha4 = (2016, 12, 31)           # Resultado: true
    fecha5 = (12, 2019, 31)           # Resultado: false
    fecha6 = (2016, 2, 0)             # Resultado: false
    fecha7 = (2015, 2, 2017)          # Resultado: false
    fecha8 = (1, 2, 1200)             # Resultado: false
    print("Fecha: ", fecha1, "=> Resultado: ", fecha_es_tupla(fecha1))
    print("Fecha: ", fecha2, "=> Resultado: ", fecha_es_tupla(fecha2))
    print("Fecha: ", fecha3, "=> Resultado: ", fecha_es_tupla(fecha3))
    print("Fecha: ", fecha4, "=> Resultado: ", fecha_es_tupla(fecha4))
    print("Fecha: ", fecha5, "=> Resultado: ", fecha_es_tupla(fecha5))
    print("Fecha: ", fecha6, "=> Resultado: ", fecha_es_tupla(fecha6))
    print("Fecha: ", fecha7, "=> Resultado: ", fecha_es_tupla(fecha7))
    print("Fecha: ", fecha8, "=> Resultado: ", fecha_es_tupla(fecha8))

# ---------------------- R1 (bisiesto)---------------------------------


def pruebaR1():
    print("\n-------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R1 (bisiesto):\n")
    year1 = 2024    # Resultado: true
    year2 = 1500    # Resultado: false
    year3 = 2000    # Resultado: true
    year4 = 1600    # Resultado: true
    year5 = 2021    # Resultado: false
    year6 = 2005    # Resultado: false
    year7 = 2010    # Resultado: false
    year8 = 2018    # Resultado: false
    print("Año: ", year1, "=> Resultado: ", bisiesto(year1))
    print("Año: ", year2, "=> Resultado: ", bisiesto(year2))
    print("Año: ", year3, "=> Resultado: ", bisiesto(year3))
    print("Año: ", year4, "=> Resultado: ", bisiesto(year4))
    print("Año: ", year5, "=> Resultado: ", bisiesto(year5))
    print("Año: ", year6, "=> Resultado: ", bisiesto(year6))
    print("Año: ", year7, "=> Resultado: ", bisiesto(year7))
    print("Año: ", year8, "=> Resultado: ", bisiesto(year8))


# ---------------------- R2 (fecha_es_valida)---------------------------
def pruebaR2():
    print("\n-------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R2 (fecha_es_valida):\n")
    fecha1 = (2016, 12, 1)    # Resultado: true
    fecha2 = (2016, 12, 31)   # Resultado: true
    fecha3 = (2016, 2, 28)    # Resultado: true
    fecha4 = (2016, 2, 29)    # Resultado: true
    fecha5 = (2016, 11, 31)   # Resultado: false
    fecha6 = (2016, 2, 0)     # Resultado: false
    fecha7 = (2015, 2, 29)    # Resultado: false
    fecha8 = (1200, 2, 1)     # Resultado: false
    print("Fecha: ", fecha1, "=> Resultado: ", fecha_es_valida(fecha1))
    print("Fecha: ", fecha2, "=> Resultado: ", fecha_es_valida(fecha2))
    print("Fecha: ", fecha3, "=> Resultado: ", fecha_es_valida(fecha3))
    print("Fecha: ", fecha4, "=> Resultado: ", fecha_es_valida(fecha4))
    print("Fecha: ", fecha5, "=> Resultado: ", fecha_es_valida(fecha5))
    print("Fecha: ", fecha6, "=> Resultado: ", fecha_es_valida(fecha6))
    print("Fecha: ", fecha7, "=> Resultado: ", fecha_es_valida(fecha7))
    print("Fecha: ", fecha8, "=> Resultado: ", fecha_es_valida(fecha8))

# ---------------------- R3 (dia_siguiente)-------------------------------


def pruebaR3():
    print("\n-------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R3 (dia_siguiente):\n")

    fecha1 = (2016, 12, 1)    # Resultado: (2016,12,2)
    fecha2 = (2016, 12, 31)   # Resultado: (2017,1,1)
    fecha3 = (2016, 2, 28)    # Resultado: (2016,2,29)
    fecha4 = (2016, 2, 29)    # Resultado: (2016,3,1)
    fecha5 = (2016, 11, 31)   # Resultado: false (fecha inválida)
    fecha6 = (2016, 2, 0)     # Resultado: false (fecha inválida)
    fecha7 = (2015, 2, 29)    # Resultado: false (fecha inválida)
    fecha8 = (1200, 2, 1)     # Resultado: false (fecha inválida)
    print("Fecha: ", fecha1, "=> Resultado: ", dia_siguiente(fecha1))
    print("Fecha: ", fecha2, "=> Resultado: ", dia_siguiente(fecha2))
    print("Fecha: ", fecha3, "=> Resultado: ", dia_siguiente(fecha3))
    print("Fecha: ", fecha4, "=> Resultado: ", dia_siguiente(fecha4))
    print("Fecha: ", fecha5, "=> Resultado: ", dia_siguiente(fecha5))
    print("Fecha: ", fecha6, "=> Resultado: ", dia_siguiente(fecha6))
    print("Fecha: ", fecha7, "=> Resultado: ", dia_siguiente(fecha7))
    print("Fecha: ", fecha8, "=> Resultado: ", dia_siguiente(fecha8))

# ---------------------- R4 (ordinal_dia)------------------------------


def pruebaR4():
    print("\n-------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R4 (ordinal_dia):\n")
    fecha1 = (2016, 12, 1)    # Resultado: 336
    fecha2 = (2016, 12, 31)   # Resultado: 366
    fecha3 = (2016, 2, 28)    # Resultado: 59
    fecha4 = (2016, 2, 29)    # Resultado: 60
    fecha5 = (2016, 11, 31)   # Resultado: 0 (fecha inválida)
    fecha6 = (2016, 2, 0)     # Resultado: 0 (fecha inválida)
    fecha7 = (2015, 2, 29)    # Resultado: 0 (fecha inválida)
    fecha8 = (1200, 2, 1)     # Resultado: 0 (fecha inválida)
    print("Fecha: ", fecha1, "=> Resultado: ", ordinal_dia(fecha1))
    print("Fecha: ", fecha2, "=> Resultado: ", ordinal_dia(fecha2))
    print("Fecha: ", fecha3, "=> Resultado: ", ordinal_dia(fecha3))
    print("Fecha: ", fecha4, "=> Resultado: ", ordinal_dia(fecha4))
    print("Fecha: ", fecha5, "=> Resultado: ", ordinal_dia(fecha5))
    print("Fecha: ", fecha6, "=> Resultado: ", ordinal_dia(fecha6))
    print("Fecha: ", fecha7, "=> Resultado: ", ordinal_dia(fecha7))
    print("Fecha: ", fecha8, "=> Resultado: ", ordinal_dia(fecha8))

# ---------------------- R5 (dia_semana)------------------------------


def pruebaR5():
    print("\n-------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R5 (dia_semana):\n")
    fecha1 = (2016, 12, 1)  # Resultado: 4 Jueves
    fecha2 = (2016, 12, 31)  # Resultado: 6 Sábado
    fecha3 = (2016, 2, 28)  # Resultado: 0 Domingo
    fecha4 = (2016, 2, 29)  # Resultado: 1 Lunes
    fecha5 = (2016, 11, 31)  # Resultado: -1 (fecha inválida)
    fecha6 = (2016, 2, 0)  # Resultado: -1 (fecha inválida)
    fecha7 = (2015, 2, 29)  # Resultado: -1 (fecha inválida)
    fecha8 = (1200, 2, 1)  # Resultado: -1 (fecha inválida)
    print("Fecha: ", fecha1, "=> Resultado: ", dia_semana(fecha1))
    print("Fecha: ", fecha2, "=> Resultado: ", dia_semana(fecha2))
    print("Fecha: ", fecha3, "=> Resultado: ", dia_semana(fecha3))
    print("Fecha: ", fecha4, "=> Resultado: ", dia_semana(fecha4))
    print("Fecha: ", fecha5, "=> Resultado: ", dia_semana(fecha5))
    print("Fecha: ", fecha6, "=> Resultado: ", dia_semana(fecha6))
    print("Fecha: ", fecha7, "=> Resultado: ", dia_semana(fecha7))
    print("Fecha: ", fecha8, "=> Resultado: ", dia_semana(fecha8))


pruebaR0()
pruebaR1()
pruebaR2()
pruebaR3()
pruebaR4()
pruebaR5()
