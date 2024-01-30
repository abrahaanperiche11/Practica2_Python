lista_meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
fecha=input('ingresar la fecha "MM/DD/AAAA" o "[nombre del mes] [Número de día], [número de año]": ')
presencia=fecha.find("/")
if presencia>-1:
    mes, dia, anio=fecha.split('/')
    mes=int(mes)
    dia=int(dia)
    print(f'la fecha en formato AAAA-MM-DD es {anio}-{mes:02}-{dia:02}')
else:
    fecha=fecha.upper()
    for i in range(0,13):
        nombre_mes=lista_meses[i-1]
        nombre_mes=nombre_mes.upper()
        presencia_nombre=fecha.find(nombre_mes)
        if presencia_nombre>-1:
            mes_dia, anio=fecha.split(',')
            mes, dia=mes_dia.split(' ')
            dia=int(dia)
            print(f'la fecha en formato AAAA-MM-DD es {anio}-{i:02}-{dia:02}')