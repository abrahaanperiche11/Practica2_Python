numeros_ingresados=[]
numeros_pares=[]
numeros_impares=[]
while True:
    ingresa_numero=input('Desea ingresar un número?: ')
    ingresa_numero=ingresa_numero.upper()
    if ingresa_numero=="SI":
        numero=int(input('Ingrese el numero: '))
        numeros_ingresados.append(numero)
        if numero%2==0:
            numeros_pares.append(numero)
        elif numero%2==1:
            numeros_impares.append(numero)
        continue
    elif ingresa_numero=="NO":
        break
    else:
        print('Esta opción no es valida')
print(numeros_ingresados)
print(f'Cantidad de números pares: {len(numeros_pares)}')
print(f'Cantidad de números impares: {len(numeros_impares)}')