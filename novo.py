from random import uniform, normalvariate
from matplotlib import pyplot as plt

elementos = 100000
count = 0
A = []
eixox = []
eixoy = []

# Nesta etapa é criada a função bucket sort, onde cria 
# 100 listas e seus respectivos indices são inseridos de forma ordenada 
# por meio da funcao sort 

def bucketsort(array):
    bucket = []
   
    for i in range(100):
        bucket.append([])

    for j in array:
        index_b = int(100 * j)
        bucket[index_b].append(j)
  
    for i in range(100):
        bucket[i] = sorted(bucket[i])
    return bucket


# cada balde "bucket" é passado para o array 

def bucketToArray(array):
    k = 0
    temp = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            temp.append(array[i][j])
            k += 1
    return temp

print('\n')
opt = input("Gerar numeros do tipo 1)Uniforme  or 2)Aleatorios: ")

# Preenchimento de forma randômica o vetor A de 100000 elementos tipo float 0.0≤x<1.0
if int(opt) == 1:
    for x in range(elementos):
        #função round para não passar o intervalo 
        y = round(uniform(0.0, 0.99999), 5)
        A.append(y)
elif int(opt) == 2:
    for x in range(elementos):
        y = round(normalvariate(0.5, 0.1), 5)
        A.append(y)

#vetor B, ordenado com bucket sort
B = bucketsort(A)

#vetor original A
A = bucketToArray(B)

#vetor B com a lista encadeada.
for x in B:
    print ("[" + str(count) + "]", x)
    count += 1
    eixox.append(count)
    eixoy.append(len(x))

# Exibir a quantidade de itens nas listas
print("\n")
opt = input("Quantidade de itens do vetor B? (n/y): ")
count = 0
if opt == "y":
   for x in B:
    print ("[" + str(count) + "]", len(x))
    count += 1

print("\n")
opt = input("Ver o vetor A ordenado? (n/y): ")
if opt == "y":
    for x in A:
        print(x)

# Limpar o vetor
A=[]

print("\n")
opt = input("Mostrar Gráficos? (n/y): ")
if opt == "y":
    # Exibir o grafico
    plt.bar(eixox, eixoy,color=(0.2, 0.2, 0.2, 0.2),  edgecolor='red')
    plt.show()
    
  