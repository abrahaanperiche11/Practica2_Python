def primo(n):
    if n==1 or n==2:
        return True
    elif n>2:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
            else:
                return True
n=int(input('Ingresa el número que desees comprobar: '))
resultado=primo(n)
if resultado==True:
    print(f'el número {n} es un número primo')
else:
    print(f'el número {n} NO es un número primo')