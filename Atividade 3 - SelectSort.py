def selectsort(seq):
    lista=range(0,len(seq)-1)
    for i in lista:
        min_valor = i
        for j in range(i+1,len(seq)):
            if seq[min_valor] > seq[j]:
                    min_valor=j
                    temp=seq[i]
                    seq[i]=seq[min_valor]
                    seq[min_valor]=temp
    return seq
                  
print(selectsort([90,15,60,50,25,14,78,2,1]))

