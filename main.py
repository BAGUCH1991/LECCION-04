palabra="christian"

print(palabra[0])
print(palabra[1])
print(palabra[2])
print(palabra[3])
print(palabra[4])
print(palabra[5])

for letra in palabra:
    print(letra+ 'b'+'a')


marcas=["BMW", "HONDA", "NISSAN"]


indice=0
for letra in palabra:
    print(indice, letra )
    indice = indice + 1

for indice, letra in enumerate(palabra):
    print(indice, letra)

    


