def BuscaBinaria(seq,x):
    inicio = 0
    final = len(seq)-1
    
    while inicio <= final:
        meio = (inicio + final)//2
        if seq[meio] == x:
            return meio 
        else:
            if x < seq[meio]:
                final = meio - 1
            else:
                inicio = meio + 1
    return -1
           
print(BuscaBinaria([1,4,5,12,14,20,30],4)) 

