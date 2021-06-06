import numpy as np
from random import randint
import time
import timeit

numero_matriz =64

def rand_matriz(tamanho):
    matrix = []
    for i in range(tamanho):
        matrix.append(i)
        matrix[i] = []
        for j in range(tamanho):
            x = randint(0, 10)
            if (x < 5):
                matrix[i].append(0)
            elif (x < 8):
                matrix[i].append(1)
            else:
                matrix[i].append(2)
    return matrix


def split(matrix):
	
	row, col = matrix.shape
	row2, col2 = row//2, col//2
	return matrix[:row2, :col2], matrix[:row2, col2:], matrix[row2:, :col2], matrix[row2:, col2:]

def strassen(x, y):
	
	if len(x) == 1:
		return x * y
	a, b, c, d = split(x)
	e, f, g, h = split(y)

	p1 = strassen(a, f - h)
	p2 = strassen(a + b, h)		
	p3 = strassen(c + d, e)		
	p4 = strassen(d, g - e)		
	p5 = strassen(a + d, e + h)		
	p6 = strassen(b - d, g + h)
	p7 = strassen(a - c, e + f)

	c11 = p5 + p4 - p2 + p6
	c12 = p1 + p2		
	c21 = p3 + p4			
	c22 = p1 + p5 - p3 - p7

	c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))

	return c

a = np.array(rand_matriz(numero_matriz))
b = np.array(rand_matriz(numero_matriz))

inicio = timeit.default_timer()
c = strassen(a, b)
fim = timeit.default_timer()

print("Matriz A : ", numero_matriz)
print(a)
print("\n")
print("Matriz B :", numero_matriz)
print(b)
print("\n")
print("Matriz C :", numero_matriz)
print(c)
print("\n")
print('duração da execução: %f' % (fim - inicio))