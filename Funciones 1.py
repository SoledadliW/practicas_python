"""
En una escuela se necesita un programa para obtener los datos de los alumnos y calcular el promedio de la clase.

1) Realizar una función que permita la carga de n alumnos, se deberá preguntar el nombre completo y la nota. Devolver el listado de alumnos.

2) Dado el anterior listado de alumnos, escribir una función que tome ese listado por parámetro y evalúe alumno por alumno determinando si aprobó o no. Se aprueba con 4 en adelante. Devolver una lista de aprobados y una lista de desaprobados.

3) Dada la lista de alumnos del ejercicio 1, realizar una función que tome ese listado como parámetro y saque el promedio de nota del curso general. Imprimir el valor de la siguiente manera: "El promedio del curso fue de <nota>"
"""

def ingresar_alumnos():
    salir = ""
    alumnos = []

    while salir != "no":
        alumno = {"nombre y apellido": "", "nota":""}
        alumno["nombre y apellido"] = input("Ingrese el nombre completo del alumno/a: ")
        alumno["nota"] = int(input("ingrese la nota del alumno/a: "))
        alumnos.append(alumno)

        salir = input("Quiere agregar otro alumno/a? si / no : ")
    return alumnos

lista_alumnos = ingresar_alumnos()

def aprobados(alumnos):
    dicc_aprobados = []
    dicc_desaprobados = []
    for alumno in alumnos:
        notas = int(alumno["nota"])
        if notas >= 4:
            dicc_aprobados.append(notas)
        else:
            dicc_desaprobados.append(notas)

    print("Notas aprobadas: ",dicc_aprobados)
    print("Notas desaprobadas: ",dicc_desaprobados)
	
    return aprobados
aprobados(lista_alumnos)

def promedios (alumnos):
    sum_num = 0
    for alumno in alumnos:
        notas = int(alumno["nota"])
        sum_num = sum_num + notas
        avg = sum_num / len(alumnos)
    print (f"El promedio del curso fue de " + str(avg) )

    return promedios

promedios(lista_alumnos)
