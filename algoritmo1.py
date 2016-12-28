from itertools import combinations

import numpy as np
import utility


# input:
# - vet = vettore che contiene una delle tante soluzioni
# restituite dal passo precedente
# - n = ordine del grafo
# - vet_uni = vettore unitario
# output:
# - vettore in ingresso ovvero la riga contenente la soluzione
def scarto(vet, vet_uni):
    vet = np.array(vet)  # trasformo il vettore in input in un array
    # somma vettori sulla stessa riga salvo il risultato in un array temporaneo
    tmp = vet.sum(axis=0)
    if (tmp.all() == vet_uni.all()):  # se tmp e' uguale all'array unitario
        return list(vet)  # ritorno la riga in input altrimenti ritorna None


def somma(vet, n, k, h, vet_uni):
    for i in xrange(0, h):
        for j in xrange(0, k):
            for y in xrange(1, h):
                if (y > i):
                    for z in xrange(0, k):
                        tmp = utility.somma_vet(vet[i][j], vet[y][z]) - vet_uni
                        # se il min del valore assoluto e'
                        if (min([abs(x) for x in tmp]) != 0):
                            return  # diverso da zero esci dalla funzione
                        # altrimenti continua
                        else:
                            pass
    return 1  # alla fine di tutto il ciclo tieni la riga


def sol1(vet_in, vet1, n, k, h):
    # faccio la combinazione
    vet2 = combinations(vet1, int(k))  # vettore passo 2
    # faccio lo scarto
    vet3 = []  # vettore passo 3
    vet_uni = np.ones(n, int)  # vettore unitario
    for riga in vet2:  # ciclo su ogni riga
        tmp = scarto(riga, vet_uni)
        # aggiungi il valore solo quando la funzione "scarto" non ritorna None
        if (tmp is not None):
            vet3.append(tmp)

    # faccio la seconda combinazione
    vet4 = combinations(vet3, int(h))  # vettore passo 4
    # ultimo scarto
    vet5 = []
    for riga in vet4:
        if (somma(riga, n, int(k), int(h), vet_uni) is not None):
            vet5.append(utility.bin_to_int(vet_in, vet1, riga, int(k), int(h)))  # converto da binario ad intero
    return vet5
