def conteo(n,d):
    txt=str(n)
    d=str(d)
    numero=txt.count(d)
    return numero
n=int(input('introduce el número: '))
d=int(input('ingrese el dígito a verificar: '))
resultado=conteo(n,d)
print(f'el digito "{d}" aparece {resultado} veces en el número "{n}" ')
