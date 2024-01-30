lista_cinco=[]
lista_siete=[]
for i in range(1500,2700):
    div_cinco=i%5
    div_siete=i%7
    if div_cinco==0:
        lista_cinco.append(i)
    elif div_siete==0:
        lista_siete.append(i)
print(f' Los números entre 1500 y 2700 divisibles por 7 son {lista_siete}')
print(f' Los números entre 1500 y 2700 múltiplos de 5 son {lista_cinco}')