import random
import time
import quickSort, heapSort, mergeSort

vetor5000 = random.sample(range(1, 5001), 5000)
vetor10000 = random.sample(range(1, 10001), 10000)

#VETOR ALEATÓRIO DE 5000 ELEMENTOS
print('Vetor aleatório: ')
tempo_inicial = (time.time())
print(vetor5000)
tempo_final = (time.time())
resultado = tempo_final - tempo_inicial
print(f'{resultado}', 'segundos')

#VETOR ALEATÓRIO DE 10000 ELEMENTOS
print('Vetor aleatório: ')
tempo_inicial = (time.time())
print(vetor10000)
tempo_final = (time.time())
resultado = tempo_final - tempo_inicial
print(f'{resultado}', 'segundos')

#QUICKSORT COM PARTIÇÃO ORDENADO E INVERTIDO DE 5000 ELEMENTOS
tempo_inicial = (time.time())
quickSort(vetor5000)
print('QuickSort com Partição Ordenado: ', vetor5000)
tempo_final = (time.time())
resultado = tempo_final - tempo_inicial
print(f'{resultado}', 'segundos')

tempo_inicial = (time.time())
quickSort(vetor5000)
print('Invertido: ', vetor5000)
tempo_final = (time.time())
resultado = tempo_final - tempo_inicial
print(f'{resultado}', 'segundos')

#QUICKSORT COM PARTIÇÃO ORDENADO E INVERTIDO DE 10000 ELEMENTOS
tempo_inicial = (time.time())
quickSort(vetor10000)
print('QuickSort com Partição Ordenado: ', vetor10000)
tempo_final = (time.time())
resultado = tempo_final - tempo_inicial
print(f'{resultado}', 'segundos')

tempo_inicial = (time.time())
quickSort(vetor10000)
print('Invertido: ', vetor10000)
tempo_final = (time.time())
resultado = tempo_final - tempo_inicial
print(f'{resultado}', 'segundos')

#HEAPSORT COM PARTIÇÃO ORDENADO E INVERTIDO DE 10000 ELEMENTOS
tempo_inicial = (time.time())
heapSort(vetor5000)
print('HeapSort com Partição Ordenado: ', vetor5000)
tempo_final = (time.time())
resultado = tempo_final - tempo_inicial
print(f'{resultado}', 'segundos')

tempo_inicial = (time.time())
heapSort(vetor5000)
print('Invertido: ', vetor5000)
tempo_final = (time.time())
resultado = tempo_final - tempo_inicial
print(f'{resultado}', 'segundos')

#HEAPSORT COM PARTIÇÃO ORDENADO E INVERTIDO DE 10000 ELEMENTOS
tempo_inicial = (time.time())
heapSort(vetor10000)
print('HeapSort com Partição Ordenado: ', vetor10000)
tempo_final = (time.time())
resultado = tempo_final - tempo_inicial
print(f'{resultado}', 'segundos')

tempo_inicial = (time.time())
heapSort(vetor10000)
print('Invertido: ', vetor10000)
tempo_final = (time.time())
resultado = tempo_final - tempo_inicial
print(f'{resultado}', 'segundos')

#MERGESORT COM PARTIÇÃO ORDENADO E INVERTIDO DE 5000 ELEMENTOS
tempo_inicial = (time.time())
mergeSort(vetor5000)
print('MergeSort com Partição Ordenado: ', vetor5000)
tempo_final = (time.time())
resultado = tempo_final - tempo_inicial
print(f'{resultado}', 'segundos')

tempo_inicial = (time.time())
mergeSort(vetor5000)
print('Invertido: ', vetor5000)
tempo_final = (time.time())
resultado = tempo_final - tempo_inicial
print(f'{resultado}', 'segundos')

#MERGESORT COM PARTIÇÃO ORDENADO E INVERTIDO DE 10000 ELEMENTOS
tempo_inicial = (time.time())
mergeSort(vetor10000)
print('MergeSort com Partição Ordenado: ', vetor10000)
tempo_final = (time.time())
resultado = tempo_final - tempo_inicial
print(f'{resultado}', 'segundos')

tempo_inicial = (time.time())
mergeSort(vetor10000)
print('Invertido: ', vetor10000)
tempo_final = (time.time())
resultado = tempo_final - tempo_inicial
print(f'{resultado}', 'segundos')