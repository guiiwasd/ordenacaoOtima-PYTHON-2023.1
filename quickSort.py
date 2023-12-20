def quickSort(vet, inicio = 0, fim = None):
    fim = fim if fim != None else len(vet) - 1
    if inicio < fim:
        pivo = particao(vet, inicio, fim)
        quickSort(vet, inicio, pivo - 1)
        quickSort(vet, pivo + 1, fim)

def particao(vet, inicio, fim):
    pivo = vet[fim]
    i = inicio
    for j in range(inicio, fim):
        if vet[j] <= pivo:
            vet[i], vet[j] = vet[j], vet[i]
            i = i + 1
    vet[i], vet[fim] = vet[fim], vet[i]
    return i

y = [9, 8, 5, 6, 7, 3, 10, 2, 0, 4, 1]
quickSort(y)
print(y)
