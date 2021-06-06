def BuscaSequencial(seq,x):
    for i in range(len(seq)):
        if seq[i]==x:
            return True,x
    return False

print(BuscaSequencial([11,23,58,31,56,77,43,12,65,19],11))

# Busca Sequencial