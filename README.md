# ordenacaoOtima-PYTHON-2023.1
# ESTRUTURA DE DADOS 
Código realizado para Busca no Vetor em Python, realizado em aula juntamente ao professor @marceloarantes19.

# Ordenação Ótima
*1. Merge Sort*
- Usa os algoritmos de intercalação. A cada interação, ele quebra a lista na metade, e como ele é recursivo, ele anda. A intercalação pega duas listas ordenadas e gera uma terceira lista ordenada.
-Complexidade de tempo no *PIOR CASO* Merge Sort = O(n lg n)
#
*2. Heap Sort*
- É uma árvore binária em que o valor do pai é SEMPRE MAIOR que os filhos. Ele monta um heap dentro do vetor e considera uma parte ordenada e outra desordenada, começando pelo fim. Para alcançar o índice filho à esquerda de um elemento a partir do seu índice (i) do vetor é necessário:

- fe = i * 2 + 1 (para calcular o filho à esquerda)
- fd = i * 2 + 2 (para calcular o filho à direita
  
- Complexidade de tempo no *PIOR CASO* Heap Sort = O(n lg n)
#
*3. Quick Sort*
- O quicksort (ordenação rápida) tenta selecionar um número qualquer, um elemento qualquer do vetor, e comparar com os outros valores do vetor, onde os menores ficam pra esquerda e os maiores pra direita, de maneira recursiva. Quando ele chega no final analisamos os valores, podemos comparar e dizer que todos os valores à esquerda são menores e todos os valores à direita são maiores, sendo a melhor opção prática para ordenação, devido a sua notável eficiência no caso médio com uma boa execução.
- Além disso, podemos dizer que o quicksort é uma estrutura não-estável, onde nada garante a ordem dos elementos repetido.
Existe diversas maneiras para realizarmos o quicksort, o mais comum seria pegar os elementos da ponta, ou começando pelo início ou pelo último elemento e começar a comparação. A ideia é trabalhar com 3 variáveis, dividido igual o Merge Sort e Heap Sort onde divide o vetor em duas partes, com o elemento ao centro. Um algoritmo é recursivo que irá realizar as quebras e o outro algoritmo vai determinar quem vai ser o pivô (o elemento que está sendo trabalhado). O j sempre cresce procurando valores maiores que o pivô e o i 
mapeia valor menor que o vetor.

- Complexidade de tempo no *PIOR CASO* Quick Sort = O(n²)  *ATENÇÃO: Podemos dizer que se o particionamento é não balanceado de modo máximo em cada nível recursivo do algoritmo, o tempo de execução é dado por O(n²). Por conseguinte, o tempo de execução do pior caso do quicksort não é melhor que o da ordenação por inserção.*
  
- Complexidade de tempo no *CASO MÉDIO* Quick Sort = O(n log n) *O tempo de execução do caso médio de quicksort é muito mais próximo do melhor caso que do pior caso. A chave para compreender por que isso poderia ser verdade é entender como o equilíbrio do particionamento   se reflete na recorrência que descreve o tempo de execução, com listas aleatórias ou parcialmente ordenadas.

**Apesar disso, há casos em que o quicksort não é tão eficiente quanto outros, sendo inferior até mesmo ao Bubble Sort, quando houver muitos valores iguais.**

# RESULTADO FINAL - COMPARAÇÃO 

*TIPO DE VETOR:* Vetor aleatório
- Vetor aleatório 1 de 5000 elementos: 0.016455650329589844 segundos
- Vetor aleatório 1 de 10000 elementos: 0.038897037506103516 segundos
  
- Vetor aleatório 2 de 5000 elementos: 0.01695728302001953 segundos
- Vetor aleatório 2 de 10000 elementos: 0.038898468017578125 segundos

*UTILIZANDO O QUICKSORT (OBTEVE O MELHOR RESULTADO)*
- Vetor ordenado de 5000 elementos no quickSort: 0.025907278060913086 segundos
- Vetor ordenado e invertido de 5000 elementos no quickSort: 0.024933815002441406 segundos

- Vetor ordenado de 10000 elementos no quickSort: 0.053856849670410156 segundos
- Vetor ordenado e invertido de 10000 elementos no quickSort: 0.051862239837646484 segundos

*UTILIZANDO O HEAPSORT*
- Vetor ordenado de 5000 elementos no heapSort: 0.034908294677734375 segundos
- Vetor ordenado e invertido de 5000 elementos no heapSort: 0.033875226974487305 segundos

- Vetor ordenado de 10000 elementos no heapSort: 0.0739753246307373 segundos
- Vetor ordenado e invertido de 10000 elementos no heapSort: 0.07380318641662598 segundos 

*UTILIZANDO O MERGESORT*
- Vetor ordenado de 5000 elementos no mergeSort: 0.02992105484008789 segundos
- Vetor ordenado e invertido de 5000 elementos no mergeSort: 0.02889394760131836 segundos 

- Vetor ordenado de 10000 elementos no mergeSort: 0.06482267379760742 segundos 
- Vetor ordenado e invertido de 10000 elementos no mergeSort:0.06283378601074219 segundos
