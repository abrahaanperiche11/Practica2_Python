def fibonacci(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
intento=0
while True:
    if fibonacci(intento)<=50:
        print(fibonacci(intento))
        intento +=1
    else:
        break