'''   
Instituto Tecnológico de Costa Rica
    Aseguramiento de la calidad de software, IC-6831
    Semestre I,2021
    Profesor : Ignacio Trejos Zelaya  
    
       Estudiantes:                 

    Erick Alfonso Elizondo Ramírez      2018250453
    Steven Josué Retana Cedeño          2017144537 
    Anthony Andrés Ulloa Martínez       2018290801

   
    Asignación 1b: Programas alrededor del dominio del calendario gregoriano, extensión.
'''

#|------------------------------------------------------------------------------|
#|                          Variables Globales                                  |
#|------------------------------------------------------------------------------|

institucion_calendario_gregoriano=1582  # Fecha a partir de la cual se instituye el calendario Gregoriano en Roma 
nombres_meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Diciembre"] #Nombres de los meses
cantidades_meses=[31,28,31,30,31,30,31,31,30,31,30,31] #Arreglo de cantidad de días según el mes (Febrero modificable)
fecha_invalida = "La fecha ingresada es inválida"
#|------------------------------------------------------------------------------|
#|                     Requerimientos funcionales                               |
#|------------------------------------------------------------------------------|

#---------------------- R0 (fecha_es_tupla)----------------------------------------------

# Definición: Todas las fechas serán creadas como tuplas de tres números enteros positivos (ternas), 
# en este orden: (año, mes, día). El resultado debe ser un valor booleano, True o False.

def fecha_es_tupla(fecha) :
    if len(fecha) == 3 and type(fecha[0]) == int and type(fecha[1]) == int and type(fecha[2]) == int and fecha[0] >= institucion_calendario_gregoriano and fecha[1] >= 1 and fecha[1] <= 12 and fecha[2] >= 1 and fecha[2] <= 31:
        #Se revisa si es una terna
        #Se revisa si es una terna de enteros
        #Se revisa si empieza en el año del inicio del calendario gregoriano
        #Se revisa si el mes es valido
        #Se revisa si el dia es valido
        return True
    return False


#---------------------- R1 (bisiesto)----------------------------------------------

# Definición: Dado un año perteneciente al rango permitido, determinar si este es bisiesto. 
# El resultado debe ser un valor booleano, True o False. 

def bisiesto(year) :        
    if (year % 100) == 0 :  #Se revisa si es el cambio de un siglo como 1700 o 1800
        if (year % 400) == 0 :  #Si es un siglo y es divisible de 400 es bisiesto
            return True
    else :
        if (year % 4) == 0 :    #Si no es un cambio de siglo y es divible entre 4 es bisiesto
            return True
    return False


#---------------------- R2 (fecha_es_valida)----------------------------------------------

# Definición: Dada una fecha, determinar si esta es válida según el calendario gregoriano.
# El resultado debe ser un valor booleano, True or False

def fecha_es_valida(fecha):
    if (len(fecha)==3):
        for var in range(len(fecha)):
            if type(fecha[var])!=int or fecha[var]<0: return False
        if (fecha[0]>=institucion_calendario_gregoriano):       #Validación si fecha es mayor a la instituida
            return validar_dia_mes(fecha[0],fecha[1],fecha[2])  #Teniendo un año bisiesto, se valida el día
        else : return False
    else: return False

# Funcion auxiliar en R2 para validar un dia específico del mes según si se tienen años válidos o no 
def validar_dia_mes(ano, mes , dia):
    if (cantidades_meses[mes-1] ==31 and dia>=1): return (dia<=31) 
    elif (cantidades_meses[mes-1]==30 and dia>=1): return (dia<=30) 
    elif (mes==2 and dia>=1):
        if bisiesto(ano): return (dia<=29)
        else :return (dia<=28)
    else :return False


#---------------------- R3 (dia_siguiente)----------------------------------------------

# Definición: Dada una fecha válida, determinar la fecha del dia siguiente. El resultado debe ser una fecha válida 
# (tupla de 3 números enteros positivos, que corresponde a una fecha en el calendario gregoriano, 
# conforme a nuestra convención),el resultado debe ser un valor booleano, True or False   

def dia_siguiente(fecha):
    if(fecha_es_valida(fecha)):   #Se valida si la fecha ingresada es válida, de lo contrario se retorna False
        if (cantidades_meses[fecha[1]-1]==31): #Comprobación en los respectivos arreglos de meses
            if (fecha[2] <=30): return (fecha[0],fecha[1],fecha[2]+1) 
            else : return aumentar_mes(fecha)
        elif (cantidades_meses[fecha[1]-1]==30):
            if (fecha[2] <=29): return (fecha[0],fecha[1],fecha[2]+1) 
            else : return aumentar_mes(fecha)  #Se aumenta sólo el mes de manera normal 
        else: return aumentar_bisiesto(fecha)  #Se aumenta el día o mes considerando bisiestos
    else: return fecha_invalida
   
#Funcion auxiliar en R3 para aumentar el mes en la fecha
def aumentar_mes(fecha):
    if (fecha[1]<12): return (fecha[0],fecha[1]+1,1)
    return (fecha[0]+1,1,1)

#Funcion auxiliar en R3 para aumentar el día según si el año es bisiesto o no
def aumentar_bisiesto(fecha):
    if (bisiesto(fecha[0])): 
        if (fecha[2]<29) : return (fecha[0],fecha[1],fecha[2]+1) 
        else : return aumentar_mes(fecha)
    else:
        if (fecha[2]<28) : return (fecha[0],fecha[1],fecha[2]+1) 
        else : return aumentar_mes(fecha)

#---------------------- R4 (ordinal_dia)----------------------------------------------

# Definición: Dada una fecha válida (año,mes,día), determinar cuál es la posición de esa fecha dentro del año. 
# Por ejemplo: ordinal_dia(2021,1,1)=1, ordinal_dia(2020,3,1)=61, ordinal_dia(2020,2,29) 
# Note que corresponde a 1 + el número de días transcurridos desde el primero de enero de ese año,
# El resultado debe ser un mínimo entero  


def ordinal_dia(fecha): 
    if fecha_es_valida(fecha):
        cantidad_dias = 0
        if bisiesto(fecha[0]):  # En caso de ser bisiesto, modificar febrero
            cantidades_meses[1] = 29
        for i in range(fecha[1]-1): # Sumar días hasta el último mes
            cantidad_dias += cantidades_meses[i]
        cantidades_meses[1]=28
        return cantidad_dias + fecha[2] # Sumar los días restantes                            
    else:
        return  fecha_invalida # Si devuelve 0, es una fecha no válida
      
#---------------------- R5 (dia_semana)----------------------------------------------

# Definición: Dada una fecha válida, determinar el día de la semana que corresponde, con la siguiente codificación:
# 0 = domingo, 1 = lunes, 2 = martes, 3 = miércoles, 4 = jueves, 5 = viernes, 6 = sabado
# El resultado debe ser un mínimo entero, conforme a la codificación indicada  

#El requerimiento R5 (dia_semana) fue basado en esta página https://artofmemory.com/blog/how-to-calculate-the-day-of-the-week-4203.html
#el cuál está basado de este libro "Mind Performance Hacks" por Ron Hale-Evans
#utiliza la siguiente fórmula (Year Code + Month Code + Century Code + Date Number – Leap Year Code) mod 7

def dia_semana(fecha): 
    if(fecha_es_valida(fecha)):
        year_code = year_code(fecha[0])
        month_code = month_code(fecha[1])
        century_code = century_code(fecha[0])
        dia = fecha[2]
        #si es bisiesto se le resta en 1 antes de hacer mod 7, pero es lo mismo restárselo al día
        #esto en caso de que sea Enero o Febrero
        if bisiesto(fecha[0]) and (fecha[1] == 1 or fecha[1] == 2): 
            dia-=1
        return ((year_code + month_code + century_code + dia) % 7)
    else:
        return fecha_invalida #En caso de que la fecha no es válida

# Utiliza (YY + (YY div 4)) mod 7, siendo YY los primeros 2 dígitos del año
def year_code(year):
    year = year % 100
    return (year + (year // 4)) % 7

# De acuerdo al mes, se obtiene un número necesario para la fórmula
def month_code(month):
    _codelist_= [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    return _codelist_[month-1]

# Dependiendo del siglo de un año dado, se obtiene otro número utilizado en la fórmula,
# cabe recalcar que estos códigos es para el calendario Gregoriano, en el Juliano es distinto
def century_code(year): 
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

#---------------------- R6 (imprimir_3x4)----------------------------------------------

# Definición: Dado un año perteneciente al rango permitido, desplegar en consola el calendario de ese año 
# en formato 3 secuencias ("filas") de 4 meses cada una. 

#Funcion principal, se encarga de separar el problema en 4 meses cada iteración para poder imprimirlos en la función auxiliar
#También revisa si el año introducido es válido de acuerdo a las especificaciones del problema

def imprimir_3x4(anio):
    if type(anio) == int and anio >= institucion_calendario_gregoriano:  #Validación de año válido
        if bisiesto(anio): 
            print("Calendario del año {} D.C   =>  Año bisiesto   <=".format(anio))
            cantidades_meses[1]=29
        else: print("Calendario del año {} D.C".format(anio))
        i=0
        while i<12:
            primer_dia=[0,0,0,0]                         #Arreglo del primer día de cada mes
            contador_mes=[1,1,1,1]                       #Arreglo contador de días de cada mes
            banderas=[False,False,False,False]           #Arreglo de banderas para lógica interna de cada mes
            j=0
            for j in range(4):
                primer_dia[j]=dia_semana((anio,(j+i)+1,1))          #Asigna el primer día a cada mes
            imprimir_meses4(i,primer_dia,contador_mes,banderas)  #Llama a función que se encarga de imprimir los 4 meses en línea
            i+=4
        print(("-"*144))
        cantidades_meses[1]=28

    else:
        print("ERROR => El valor del año introducido (",anio,") debe ser de tipo entero positivo y ser mayor o igual al año ",institucion_calendario_gregoriano)

#Funcion auxiliar que se encarga de imprimir 4 meses dados en línea en la pantalla
#Recibe los arreglos provenientes de la función principal para trabajarlos y los modifica para la impresión de los valores
def imprimir_meses4(mes,primer_dia,contador_mes,banderas):
    indice_mes=dia=0
    print(("-"*144))
    print("{:^35}|{:^35}|{:^35}|{:^35}|".format(nombres_meses[mes],nombres_meses[mes+1],nombres_meses[mes+2],nombres_meses[mes+3]))  #Imprime los nombres de los 4 meses 
    for _ in range(4): print("{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}{:^5}|".format('D','L','K','M','J','V','S'),end="")                      #Imprime las siglas de los 7 días de la semana para cada mes
    print("")
    for _ in range(6):              #Recorre las 6 líneas de impresión de cada mes en forma vertical
        for indice_mes in range(4):     #Recorre los 4 meses para imprimir sus días en forma horizontal
            for dia in range(7):        #Recorre cada uno de los 7 días de la semana para imprimir el valor 
                if dia+1<=primer_dia[indice_mes] and banderas[indice_mes]!=True:print("{:^5}".format(" "),end="")    #Si no se ha llegado el primer día del mes se imprime un espacio en blanco
                elif contador_mes[indice_mes]>cantidades_meses[indice_mes+mes]: print("{:^5}".format(""),end="")         #Si ya imprimió todos los días y quedan campos se imprime un espacio en blanco
                else:                                                                                                #Imprime el valor del día según las iteraciones
                    banderas[indice_mes]=True
                    print("{:^5}".format(contador_mes[indice_mes]),end="")  
                    contador_mes[indice_mes]+=1  
            print("|",end="") 
        print("")

#Funcion auxiliar que se encarga de retornar un número si toca imprimir o en caso contrario un espacio en blanco para imprimir
#Recibe los arreglos provenientes de la la función auxiliar (imprimir_meses4) y retorna el número o un espacio en blanco según corresponda
def mostrar_numero(primer_dia,contador_mes,indice):
    if contador_mes[indice]<=primer_dia:
        contador_mes[indice]+=1
        return " "
    else: 
        numero=contador_mes[indice]
        contador_mes[indice]+=1
        return numero

#---------------------- R7 (fecha_futura)----------------------------------------------

# Definición: Dados una fecha válida f y un número entero no-negativo n, determinar 
# la fecha que está n días naturales en el futuro.
# El resultado debe ser una fecha válida
def fecha_futura(fecha,dias):
    if isinstance(dias, int) and dias>=0 and fecha_es_valida(fecha): #Verificación de datos
        fecha = list(fecha)    #Tupla no es mutable
        cambiar_mes(fecha)       
        while dias != 0:
            dia_actual = fecha[2]
            dia_temp = dia_actual + dias
            if dia_temp > cantidades_meses[fecha[1] - 1]: #Si excede en la cantidad de días del mes actual
                dias = dias - (cantidades_meses[fecha[1] - 1] - dia_actual) - 1 #Días restantes a sumar
                if fecha[1] == 12: #En caso de que sea diciembre, se requiere cambiar de año
                    fecha[0] += 1
                    fecha[1]  = 1
                    fecha[2]  = 1
                    cambiar_mes(fecha)                   
                else: #De caso contrario, solo se cambia el mes
                    fecha[1] += 1
                    fecha[2]  = 1
            else:
                fecha[2] = dia_temp #Asigna la suma de días
                break
        cantidades_meses[1]=28    
        return fecha
    else:
        return "Los parámetros son inválidos"

def cambiar_mes(fecha): # En caso de ser bisiesto, modificar febrero 
    if bisiesto(fecha[0]):
        cantidad_meses[1] = 29
    else:
        cantidad_meses[1] = 28

#---------------------- R8 (dias_entre)----------------------------------------------

# Definición: Dadas 2 fechas válidas, f1 y f2, sin importar si f1 <= f2 o f2 <= f1, determinar el número de 
# días naturales entre las 2 fechas. Si f1 = f2, entonces dias_entre(f1,f2)=0.
# El resultado debe ser un número entero no negativo
def dias_entre(fecha1, fecha2):
    if fecha_es_valida(fecha1) and fecha_es_valida(fecha2) :    #Se revisa si son fechas validas
        _diasextra_, _smallestyear_ = 0, 0
        if fecha1[0] >= fecha2[0]:          #Se obtiene el año de la fecha más pequeña
            rep = fecha1[0] - fecha2[0]     #Se saca la diferencia entre los años
            _smallestyear_ = fecha2           #Se guarda ese año para más adelante
        else:
            rep = fecha2[0] - fecha1[0]
            _smallestyear_ = fecha1

        #Se usa la diferencia entre los años para determinar cuantas veces se tiene que hacer el aumento
        #El año más pequeño es utilizado para saber si es bisiesto
        for var in range(0, rep):               #Se hace un loop para aumentar la diferencia que hay entre los años
            if bisiesto(_smallestyear_[0] + var): #Se revisa si es bisiesto para aumentar el día extra
                _diasextra_ += 366
            else:
                _diasextra_ += 365

        if fecha_mayor(fecha1, fecha2) == fecha1: #Se compara con la fecha mayor haciendo uso de la funcion auxiliar
            return abs(ordinal_dia(fecha1) - ordinal_dia(fecha2) + _diasextra_)
        else:
            return abs(ordinal_dia(fecha2) - ordinal_dia(fecha1) + _diasextra_)
    else:
        return fecha_invalida

# Funcion auxiliar de R8, para poder determinar cual fecha es la mayor
def fecha_mayor(fecha1, fecha2):
    if fecha1[0] > fecha2[0]:           #Se comparan los años
        return fecha1
    elif fecha1[0] == fecha2[0]:        #Se verifica si son años iguales
        if fecha1[1] > fecha2[1]:       #Se comparan los meses
            return fecha1
        elif fecha1[1] == fecha2[1]:    #Se verifica si son meses iguales
            if fecha1[2] >= fecha2[2]:  #Se comparan los días
                return fecha1
        else:
            return fecha2
    return fecha2

#---------------------- R9 (fecha_futura_habil)----------------------------------------------

# Definición: Dada una fecha válida f y un número entero no-negativo n, 
# determinar la fecha que está n días hábiles en el futuro. 
# El resultado debe ser una fecha válida que corresponda a un día hábil. 
# Note que f puede corresponder a la fecha de un día no hábil
def fecha_futura_habil(fecha,dias):
    for _ in range(0, dias):                      # Se hara un ciclo para ir agregando dias a las fechas validas
        _nfecha_ = dia_semana(fecha_futura(fecha, 1)) # Se hace esto en cada ciclo para ir verificando la valides de la fecha
        if _nfecha_ != 6 and nFecha != 0:             # Se revisa si la fecha más 1 día es valida
            fecha = fecha_futura(fecha, 1)          # Si es así se le suma el día
        else:
            if nFecha == 6:                         # Se verifica si cae Sabado o Domingo
                fecha = fecha_futura(fecha,3)       # Si la fecha cae Sabado con ese día de más, se le suman 3 días para quedar en Lunes
            else:
                fecha = fecha_futura(fecha,2)       # Si la fecha cae Domingo con ese día de más, se le suman 2 días para quedar en Lunes
    return fecha
#|--------------------------------------------------------------------------------|
#|                              Pruebas                                           |
#|--------------------------------------------------------------------------------|


#---------------------- R0 (fecha_es_tupla)---------------------------------------
def prueba_r0():
    print("\n-------------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R0 (fecha_es_tupla):\n")
    fecha1 = (1900,12,29)           #Resultado: true
    fecha2 = (1,12,31)              #Resultado: false
    fecha3 = ("Hola mundo",2,28)    #Resultado: false
    fecha4 = (2016,12,31)           #Resultado: true
    fecha5 = (12,2019,31)           #Resultado: false
    fecha6 = (2016,2,0)             #Resultado: false
    fecha7 = (2015,2,2017)          #Resultado: false
    fecha8 = (1,2,1200)             #Resultado: false
    print("Fecha: ",fecha1,"=> Resultado: ",fecha_es_tupla(fecha1))
    print("Fecha: ",fecha2,"=> Resultado: ",fecha_es_tupla(fecha2))
    print("Fecha: ",fecha3,"=> Resultado: ",fecha_es_tupla(fecha3))
    print("Fecha: ",fecha4,"=> Resultado: ",fecha_es_tupla(fecha4))
    print("Fecha: ",fecha5,"=> Resultado: ",fecha_es_tupla(fecha5))
    print("Fecha: ",fecha6,"=> Resultado: ",fecha_es_tupla(fecha6))
    print("Fecha: ",fecha7,"=> Resultado: ",fecha_es_tupla(fecha7))
    print("Fecha: ",fecha8,"=> Resultado: ",fecha_es_tupla(fecha8))
    

#---------------------- R1 (bisiesto)---------------------------------------------
def prueba_r1():
    print("\n-------------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R1 (bisiesto):\n")
    year1 = 2024    #Resultado: true
    year2 = 1500    #Resultado: false
    year3 = 2000    #Resultado: true
    year4 = 1600    #Resultado: true
    year5 = 2021    #Resultado: false
    year6 = 2005    #Resultado: false
    year7 = 2010    #Resultado: false
    year8 = 2018    #Resultado: false
    print("Año: ",year1,"=> Resultado: ",bisiesto(year1))
    print("Año: ",year2,"=> Resultado: ",bisiesto(year2))
    print("Año: ",year3,"=> Resultado: ",bisiesto(year3))
    print("Año: ",year4,"=> Resultado: ",bisiesto(year4))
    print("Año: ",year5,"=> Resultado: ",bisiesto(year5))
    print("Año: ",year6,"=> Resultado: ",bisiesto(year6))
    print("Año: ",year7,"=> Resultado: ",bisiesto(year7))
    print("Año: ",year8,"=> Resultado: ",bisiesto(year8))

#---------------------- R2 (fecha_es_valida)--------------------------------------
def prueba_r2():
    print("\n-------------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R2 (fecha_es_valida):\n")
    fecha1 = (2016,12,1)    #Resultado: true
    fecha2 = (2016,12,31)   #Resultado: true
    fecha3 = (2016,2,28)    #Resultado: true
    fecha4 = (2016,2,29)    #Resultado: true
    fecha5 = (2016,11,31)   #Resultado: false
    fecha6 = (2016,2,0)     #Resultado: false
    fecha7 = (2015,2,29)    #Resultado: false
    fecha8 = (1200,2,1)     #Resultado: false
    print("Fecha: ",fecha1,"=> Resultado: ",fecha_es_valida(fecha1))
    print("Fecha: ",fecha2,"=> Resultado: ",fecha_es_valida(fecha2))
    print("Fecha: ",fecha3,"=> Resultado: ",fecha_es_valida(fecha3))
    print("Fecha: ",fecha4,"=> Resultado: ",fecha_es_valida(fecha4))
    print("Fecha: ",fecha5,"=> Resultado: ",fecha_es_valida(fecha5))
    print("Fecha: ",fecha6,"=> Resultado: ",fecha_es_valida(fecha6))
    print("Fecha: ",fecha7,"=> Resultado: ",fecha_es_valida(fecha7))
    print("Fecha: ",fecha8,"=> Resultado: ",fecha_es_valida(fecha8))

#---------------------- R3 (dia_siguiente)----------------------------------------
def prueba_r3():
    print("\n-------------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R3 (dia_siguiente):\n")

    fecha1 = (2016,12,1)    #Resultado: (2016,12,2)
    fecha2 = (2016,12,31)   #Resultado: (2017,1,1)
    fecha3 = (2016,2,28)    #Resultado: (2016,2,29)
    fecha4 = (2016,2,29)    #Resultado: (2016,3,1)
    fecha5 = (2016,11,31)   #Resultado: false (fecha inválida)
    fecha6 = (2016,2,0)     #Resultado: false (fecha inválida)
    fecha7 = (2015,2,29)    #Resultado: false (fecha inválida)
    fecha8 = (1200,2,1)     #Resultado: false (fecha inválida)  
    print("Fecha: ",fecha1,"=> Resultado: ",dia_siguiente(fecha1))
    print("Fecha: ",fecha2,"=> Resultado: ",dia_siguiente(fecha2))
    print("Fecha: ",fecha3,"=> Resultado: ",dia_siguiente(fecha3))
    print("Fecha: ",fecha4,"=> Resultado: ",dia_siguiente(fecha4))
    print("Fecha: ",fecha5,"=> Resultado: ",dia_siguiente(fecha5))
    print("Fecha: ",fecha6,"=> Resultado: ",dia_siguiente(fecha6))
    print("Fecha: ",fecha7,"=> Resultado: ",dia_siguiente(fecha7))
    print("Fecha: ",fecha8,"=> Resultado: ",dia_siguiente(fecha8))  

#---------------------- R4 (ordinal_dia)------------------------------------------
def prueba_r4():
    print("\n-------------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R4 (ordinal_dia):\n")
    fecha1 = (2016,12,1)    #Resultado: 336
    fecha2 = (2016,12,31)   #Resultado: 366
    fecha3 = (2016,2,28)    #Resultado: 59
    fecha4 = (2016,2,29)    #Resultado: 60
    fecha5 = (2016,11,31)   #Resultado: 0 (fecha inválida)
    fecha6 = (2016,2,0)     #Resultado: 0 (fecha inválida)
    fecha7 = (2015,2,29)    #Resultado: 0 (fecha inválida)
    fecha8 = (1200,2,1)     #Resultado: 0 (fecha inválida)  
    print("Fecha: ",fecha1,"=> Resultado: ",ordinal_dia(fecha1))
    print("Fecha: ",fecha2,"=> Resultado: ",ordinal_dia(fecha2))
    print("Fecha: ",fecha3,"=> Resultado: ",ordinal_dia(fecha3))
    print("Fecha: ",fecha4,"=> Resultado: ",ordinal_dia(fecha4))
    print("Fecha: ",fecha5,"=> Resultado: ",ordinal_dia(fecha5))
    print("Fecha: ",fecha6,"=> Resultado: ",ordinal_dia(fecha6))
    print("Fecha: ",fecha7,"=> Resultado: ",ordinal_dia(fecha7))
    print("Fecha: ",fecha8,"=> Resultado: ",ordinal_dia(fecha8))  

#---------------------- R5 (dia_semana)-------------------------------------------
def prueba_r5():
    print("\n-------------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R5 (dia_semana):\n")
    fecha1 = (2016,12,1)    #Resultado: 4 Jueves
    fecha2 = (2016,12,31)   #Resultado: 6 Sábado
    fecha3 = (2016,2,28)    #Resultado: 0 Domingo
    fecha4 = (2016,2,29)    #Resultado: 1 Lunes
    fecha5 = (2016,11,31)   #Resultado: -1 (fecha inválida)
    fecha6 = (2016,2,0)     #Resultado: -1 (fecha inválida)
    fecha7 = (2015,2,29)    #Resultado: -1 (fecha inválida)
    fecha8 = (1200,2,1)     #Resultado: -1 (fecha inválida)  
    print("Fecha: ",fecha1,"=> Resultado: ",dia_semana(fecha1))
    print("Fecha: ",fecha2,"=> Resultado: ",dia_semana(fecha2))
    print("Fecha: ",fecha3,"=> Resultado: ",dia_semana(fecha3))
    print("Fecha: ",fecha4,"=> Resultado: ",dia_semana(fecha4))
    print("Fecha: ",fecha5,"=> Resultado: ",dia_semana(fecha5))
    print("Fecha: ",fecha6,"=> Resultado: ",dia_semana(fecha6))
    print("Fecha: ",fecha7,"=> Resultado: ",dia_semana(fecha7))
    print("Fecha: ",fecha8,"=> Resultado: ",dia_semana(fecha8))  

#---------------------- R6 (imprimir_3x4)-------------------------------------------
def prueba_r6():
    print("\n-------------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R6 (imprimir_3x4):\n")
    imprimir_3x4(2021)
    imprimir_3x4(2016)
    imprimir_3x4(1100)

#---------------------- R7 (fecha_futura)-------------------------------------------
def prueba_r7():
    print("\n-------------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R7 (fecha_futura):\n")
    fecha1 = (2016,12,1)  
    fecha2 = (2021,2,28)  
    fecha3 = (2016,4,1)  
    fecha4 = (2018,1,1)   
    dias1=10
    dias2=30
    dias3=366
    dias4=5840
    print("Fecha inicial: ",fecha1,"=>  Resultado de la fecha después de ",dias1," dias: ",fecha_futura(fecha1,dias1)) 
    print("Fecha inicial: ",fecha2,"=>  Resultado de la fecha después de ",dias2," dias: ",fecha_futura(fecha2,dias2)) 
    print("Fecha inicial: ",fecha3,"=>  Resultado de la fecha después de ",dias3," dias: ",fecha_futura(fecha3,dias3)) 
    print("Fecha inicial: ",fecha4,"=>  Resultado de la fecha después de ",dias4," dias: ",fecha_futura(fecha4,dias4)) 


#---------------------- R8 (dias_entre)-------------------------------------------
def prueba_r8():
    print("\n-------------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R8 (dias_entre):\n")
    fecha1 = (2016,1,1)
    fecha2 = (2015,12,31)

    fecha3 = (2019,11,1)    
    fecha4 = (2019,12,1)  

    fecha5 = (2015,3,1)
    fecha6 = (2016,3,1)   
    print("Fecha1: ",fecha1,"Fecha 2: ",fecha1,"=> Resultado: ",dias_entre(fecha1,fecha1))
    print("Fecha1: ",fecha1,"Fecha 2: ",fecha2,"=> Resultado: ",dias_entre(fecha1,fecha2))
    print("Fecha1: ",fecha3,"Fecha 2: ",fecha4,"=> Resultado: ",dias_entre(fecha3,fecha4))
    print("Fecha1: ",fecha5,"Fecha 2: ",fecha6,"=> Resultado: ",dias_entre(fecha5,fecha6))


#---------------------- R9 (fecha_futura_habil)-------------------------------------------
def prueba_r9():
    print("\n-------------------------------------------------------------------\n")
    print("\t\tPruebas requerimiento R9 (fecha_futura_habil):\n")
    fecha1, dias1 = (2021,4,10), 1   
    fecha2, dias2 = (2020,7,1), 10
    fecha3, dias3 = (2021,1,10), 12
    fecha4, dias4 = (2019,3,10), 5
    print("Fecha inicial: ",fecha1,"=>  Resultado de la fecha después de ",dias1," dias hábiles: ",fecha_futura_habil(fecha1,dias1))
    print("Fecha inicial: ",fecha2,"=>  Resultado de la fecha después de ",dias2," dias hábiles: ",fecha_futura_habil(fecha2,dias2))
    print("Fecha inicial: ",fecha3,"=>  Resultado de la fecha después de ",dias3," dias hábiles: ",fecha_futura_habil(fecha3,dias3))
    print("Fecha inicial: ",fecha4,"=>  Resultado de la fecha después de ",dias4," dias hábiles: ",fecha_futura_habil(fecha4,dias4)) 


prueba_r0()
#prueba_r1()
#prueba_r2()
#prueba_r3()
#prueba_r4()
#prueba_r5()
#prueba_r6()
#prueba_r7()
#prueba_r8()
#prueba_r9()
