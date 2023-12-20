def geraHeap(vet, i, n):
    indM = i
    indFE = i * 2 + 1
    indFD = i * 2 + 2
    if indFE < n and vet[indFE] > vet[indM]:
        indM = indFE
    if indFD < n and vet[indFD] > vet[indM]:
        indM = indFD
    if indM != i:
        vet[i], vet[indM] = vet[indM], vet[i]
        geraHeap(vet, indM, n)

def heapSort(vet):
    n = len(vet)
    for i in range(n//2 - 1, -1, -1):
        geraHeap(vet, i, n)

    for i in range(n - 1, 0, -1):
        vet[i], vet[0] = vet[0], vet[i]
        geraHeap(vet, 0, i)

y = [9, 8, 5, 6, 7, 3, 10, 2, 0, 4, 1]
heapSort(y)
print(y)