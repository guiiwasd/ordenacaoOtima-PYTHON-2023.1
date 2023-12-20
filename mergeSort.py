def intercala1 (vet, inicio, meio, fim): #as duas metadas já tem que estar ordenadas
    x = vet[inicio:meio]
    y = vet[meio:fim]
    indX = 0
    indY = 0
    i = inicio
    while i < fim:
        if x[indX] < y[indY]:
            vet[i] = x[indX]    #compara o x e o y
            indX = indX + 1
        else:
            vet[i] = y[indY]    #compara o x e o y
            indY = indY + 1
        i = i + 1
        if indX == len(x):
            vet[i:fim] = y[indY:len(y)] #se já acabou o x, insere o y no vetor
            break
        if indY == len(y):
            vet[i:fim] = x[indX:len(x)] #se já acabou o y, insere o x no vetor
            break

def merge(vet, inicio, fim):
    if fim - inicio > 1:
        meio = (inicio + fim) // 2
        merge(vet, inicio, meio)
        merge(vet, meio, fim)
        intercala1(vet, inicio, meio, fim)

def mergeSort(vet):
    merge(vet, 0, len(vet))

y = [9, 8, 5, 6, 7, 3, 10, 2, 0, 4, 1]
mergeSort(y)
print(y)