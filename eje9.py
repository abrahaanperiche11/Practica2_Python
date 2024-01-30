texto=input('ingresa el mensaje a enviar:')
lista_vocales=['a','A','e','E','i','I','o','O','u','U']
for i in range(1,11):
    vocal=lista_vocales[i-1]
    texto_1=texto.replace(vocal,'')
    texto=texto_1
print(texto)