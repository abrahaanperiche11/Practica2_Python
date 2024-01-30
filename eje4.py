diccionario={
    
}
total_alumnos=int(input('ingresa el número de alumnos que desea ingresar hoy: '))
alumnos=0
while alumnos<total_alumnos:
        nombre_alumno=input(f'ingresa el nombre del {alumnos+1}° alumno(a): ')
        nota_curso_1=int(input(f'ingresa la nota del(de la) alumno(a) {nombre_alumno} en el curso 01: '))
        nota_curso_2=int(input(f'ingresa la nota del(de la) alumno(a) {nombre_alumno} en el curso 02: '))
        nota_curso_3=int(input(f'ingresa la nota del(de la) alumno(a) {nombre_alumno} en el curso 03: '))
        lista_curso=[]
        lista_curso.append(nota_curso_1)
        lista_curso.append(nota_curso_2)
        lista_curso.append(nota_curso_3)
        diccionario[f"Alumno {alumnos+1}"]=nombre_alumno
        diccionario[f"Notas de {nombre_alumno}"]=lista_curso
        alumnos +=1
print(diccionario)