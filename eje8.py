def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
numero=int(input('introduce un número entero no negativo: '))
if numero<0:
    print('este no es un número no negativo')
elif numero>=0:
    resultado=factorial(numero)
    print(f'el factorial de {numero} es {resultado}')