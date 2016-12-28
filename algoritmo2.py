from itertools import combinations

import numpy as np
import utility

def sol2(vet1, indice, vet_in):
    out = []
    while indice >= 1:
        # converto in lista la combinations
        vet2 = list(combinations(vet1, indice))
        for riga in vet2:
            # trasformo il vettore in input in un array
            tmp = np.array(riga)
            # somma vet sulla stessa riga e salvo il risultato in temp
            tmp = tmp.sum(axis=0)
            if (all(x < 2 for x in tmp)):
                # converto da binario ad interno
                out.append(utility.bin_to_int2(vet_in, vet1, riga, len(vet2[0])))
        if (not out):
            indice = indice - 1
        else:
            break
    return out