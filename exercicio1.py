numeros = []

for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

for i in range(len(numeros)):
    if numeros.count(numeros[i]) > 1:
        print(f"O número {numeros[i]} se repete nas seguintes posições:")
        for j in range(i+1, len(numeros)):
            if numeros[i] == numeros[j]:
                print(f"- Posição {j+1}")