""" 
1) Realizar una función que permita la carga de n alumnos. Por cada alumno se deberá preguntar el nombre completo y
 permitir el ingreso de 3 notas . Las notas deben estar comprendidas entre 0 y 10. Devolver el listado de alumnos.

2) Definir una función que dado un listado de alumnos evalúe cuántos aprobaron y cuantos desaprobaron, teniendo
en cuenta que se aprueba con 4. La nota será el promedio de las 3 notas para cada alumno.

3) Informar el promedio de nota del curso total. 

4) Realizar una función que indique quien tuvo el promedio más alto y quien tuvo la nota promedio más baja.

5) Realizar una función que permita buscar un alumno por nombre, siendo el nombre completo o parcial, 
y devuelva una lista con los n alumnos que concuerden con ese nombre junto con todos sus datos, 
incluido el promedio de sus notas.

Por ejemplo : 
Entrada: Juan
Salida: [{"nombre": "Juan Perez", "notas": [ 2, 5, 9], "promedio": 5.33}, 
{"nombre": "Juana Vega", "notas": [ 5, 5, 6], "promedio": 5.33}]
"""
#1
def ingresar_alumnos():
    salir = ""
    alumnos = []

    while salir != "no":
        alumno = {"Nombre": "", "Nota1": "", "Nota2": "", "Nota3": ""}
        alumno["Nombre"] = input("Ingrese el nombre completo del alumno/a: ")
        alumno["Nota1"] = int(input("Ingrese la primera nota del alumno/a (del 0 al 10): "))
        alumno["Nota2"] = int(input("Ingrese la segunda nota: "))
        alumno["Nota3"] = int(input("Ingrese la tercera nota: "))
        alumnos.append(alumno)

        salir = input("Quiere agregar otro alumno/a? si / no : ")

    return alumnos

lista_alumnos = ingresar_alumnos()

#2
def alumnos_aprobados(alumnos):
    for alumno in alumnos:
        notas_alumno = int(alumno["Nota1"] + alumno["Nota2"] + alumno["Nota3"])
        prom_alumno = int(notas_alumno/3)
        if prom_alumno >=4:
            print("Alumno/a " +  alumno["Nombre"] + " aprobado/a con promedio: " , prom_alumno )
        else:
            print("Alumno/a " +  alumno["Nombre"] + " desaprobado/a con promedio: ", prom_alumno)     
    
    return alumnos_aprobados
alumnos_aprobados(lista_alumnos)

#3
def promedios (alumnos):
    sum_num = 0
    for alumno in alumnos:
        notas = int(alumno["Nota1"] + alumno["Nota2"] + alumno["Nota3"])
        sum_num = sum_num + notas
        avg = sum_num / len(alumnos)
        #divido 3 por la cantidad de notas
        avg_total = int(avg / 3)
    print (f"El promedio del curso fue de " + str(avg_total) )

    return promedios
promedios(lista_alumnos)

#4
def promedio_alto (alumnos):
    avg_max = 0
    avg_min = 0
    alumno_max = ""
    alumno_min = ""
    primera_entrada = True

    for alumno in alumnos:
        notas = int(alumno["Nota1"] + alumno["Nota2"] + alumno["Nota3"])
        prom_alumno = int(notas/3)
        if prom_alumno > avg_max:
            avg_max = prom_alumno
            alumno_max = alumno["Nombre"]
        if primera_entrada or prom_alumno < avg_min:
            avg_min = prom_alumno
            alumno_min = alumno["Nombre"]
        if primera_entrada:
            primera_entrada = False
    print (f"El promedio mas bajo es de {alumno_min} con {avg_min}")
    print(f"El promedio mas alto es de {alumno_max} con {avg_max}")

    return promedio_alto
promedio_alto (lista_alumnos)

#5
def buscar_alumno (alumnos, nombre):
    lista_busqueda = []
    for alumno in alumnos:
        nota_alumno = int(alumno["Nota1"] + alumno["Nota2"] + alumno["Nota3"])
        promedio_alumno = int(nota_alumno/3)
        nombre_alumno =  alumno["Nombre"].split()
        if (alumno["Nombre"].find(nombre) != -1): 
        #el -1 indica la posicion del index, pide que no sea -1 ya que sino no existe
            lista_busqueda.append(alumno) 
            alumno["Promedio"] = promedio_alumno
    return lista_busqueda

nom_alumno = input("Ingrese el nombre del alumno/a que quiere buscar: ")
resultado = buscar_alumno(lista_alumnos, nom_alumno)
print(resultado)

