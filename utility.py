# Funzione per convertire un vettore da intero
# a binario
#
# input:
# - vet = vettore di interi
# - n = ordine del grafo
# output:
# - risultato = vettore di valori 0 ed 1
def int_to_bin(vet, n):
    # dichiaro ed inizializzo un vettore con n zeri
    risultato = [0] * n
    for j in xrange(len(vet)):
        indice = vet[j] - 1
        risultato[indice] = 1
    return risultato


# Funzione per convertire un vettore da binario
# ad intero
#
# input:
# - vet_in = vettore di partenza dell'algoritmo
# - vet_bin = vettore in binario
# - vet_sol = vettore da convertire
# - k = indice k
# - h = indice h
# output:
# - risultato = vettore di interi
def bin_to_int(vet_in, vet_bin, vet_sol, k, h):
    vet_sol = list(vet_sol)  # lo trasformo in lista
    risultato = []
    for i in xrange(h):
        for j in xrange(k):
            tmp = list(vet_sol[i][j])
            if tmp in vet_bin:
                index = vet_bin.index(tmp)
                risultato.append(vet_in[index])
    return risultato


def bin_to_int2(vet_in, vet_bin, vet_sol, h):
    vet_sol = list(vet_sol)  # lo trasformo in lista
    risultato = []
    for i in xrange(h):
        tmp = list(vet_sol[i])
        if tmp in vet_bin:
            index = vet_bin.index(tmp)
            risultato.append(vet_in[index])
    return risultato

# Funziona per la somma di vettori
#
# input:
# - vet1 = primo vettore
# - vet2 = secondo vettore
# output:
# - vettore somma
def somma_vet(vet1, vet2):
    somma = []
    for i in range(len(vet1)):
        somma.append(vet1[i] + vet2[i])
    return somma
