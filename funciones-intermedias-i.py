x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# import pdb
# pdb.set_trace()


#soluciones
#1
x[1][0] = 15

#2
estudiantes[0]['last_name'] = 'Bryant' 

#3
directorio_deportes['fútbol'][0] = 'Andres'

#4
z[0]['y'] = 30





#2 Iterar a través de una lista de diccionarios
#Crea una función iterateDictionary(some_list)para que, 
# dada una lista de diccionarios, la función recorra cada 
# diccionarios de la lista e imprima cada llave y el valor asociado. 
# Por ejemplo, dada la siguiente lista:

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# import pdb
# pdb.set_trace()

# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


def iterateDictionary(estudiantes):
    for i in estudiantes:
        items = list(i.items())
        print(items[0][0], " - " , items[0][1], ",", items[1][0], "-", items[1][1])
        # print(f"first_name - {estudiantes[claves]['first_name']}, last_name - {estudiantes[claves]['last_name']}")

iterateDictionary(estudiantes)





#----------------------------------------------------------------------------------------------------------

# #Pregunta3
# #Obtener valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios 
# y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. 
# Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
# Michael
# John
# Mark
# KB

# Y iterateDictionary2('last_name', estudiantes) debería generar:

# Jordan
# Rosales
# Guillen
# Tonel


def iteratedictionary2(keys, estudiantes):
    for i in estudiantes:
        resultado = list(i.keys())
        valores = list(i.values())
        if keys == resultado[0]:
            print(valores[0])
        else:
            print(valores[1])

iteratedictionary2('last_name', estudiantes)








#--------------------------------------------------------------------------------------------------------------
# #Pregunta 4: 
# Iterar a través de un diccionarios con valores de lista
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos 
# valores son todos listas, imprima el nombre de cada clave junto con 
# el tamaño de su lista, y luego imprima los valores asociados dentro 
# de la lista de cada clave. Por ejemplo:


def printInfo(dicc):
    for llave, valores in dicc.items():
        num_valores = len(valores)
        
        print(f"{num_valores} {llave.upper()}")

        for valor in valores:
            print(valor)
        print("")

        print(llave)
        print(valores)


dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)







