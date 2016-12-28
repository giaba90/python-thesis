from __future__ import division

import math
import sys

from algoritmo1 import sol1
from algoritmo2 import sol2
from utility import int_to_bin

if __name__ == "__main__":

    ###########################
    # Dichiarazione variabili #
    ###########################

    vet_in = []  # vettore di input
    n = input("Inserisci l'ordine del grafo: ")
    card = input("Inserisci la cardinalita' dei blocchi: ")
    nVet = input("Inserisci il numero dei blocchi: ")
    k = (n / card)  # indice k
    h = (nVet / k)  # indice h
    vet1 = []  # vettore passo 1
    soluzione = []  # vettore soluzione

    ###################
    # Prendo in input #
    # la matrice      #
    ###################

    # se non do il nome del file da riga di comando
    # prendilo da tastiera
    if (len(sys.argv) < 2):
        # Ciclo per inserire nella matrice le liste corrispondenti alle righe
        for i in xrange(nVet):
            vet_in.append([])
        # Inserisco gli elementi riga per riga (un ciclo dentro a un altro ciclo)
        for i in xrange(nVet):
            for j in xrange(card):
                a = input("Inserisci elemento di riga [" + str(i) + "] e colonna [" + str(j) + "] : ")
                vet_in[i].append(a)
    else:
        f = open(sys.argv[1], "r")  # apro il file il cui nome lo do da console

        while 1:  # ciclo finche' non trovo una istruzione esci
            riga = f.readline()  # leggo una riga alla volta
            if riga == "":  # se trovo una riga vuota
                break  # esco dal ciclo while
            riga = riga.replace("\r\n", " ").split(",", card)  # tolgo la virgola ed i caratteri \r\n
            vet_in.append([int(x) for x in riga])  # converto da str ad int ogni elemento della riga

        f.close()

    # converto da intero a binario
    for i in xrange(len(vet_in)):  # converto l'input in un vettre di array binari
        vet1.append(int_to_bin(vet_in[i], n))

    ####################
    # Inizio algoritmo #
    ####################

    if ((nVet % k) == 0) and ((n % card) == 0):
        print "\nLe condizioni necessarie sono verificate.\n"
        soluzione = sol1(vet_in, vet1, n, k, h)

        # caso speciale
        # vettore in uscita e' uguale a zero
        if (not soluzione):
            indice = int(math.floor(k))
            soluzione = sol2(vet1, indice, vet_in)
            print "\nNonstante cio' la decomposizioni non e' fattorizzabile; " \
                  "le classi massimali di parallelismo li trovi nel file soluzione.txt. \n"
        else:
            print "\nLa decomposizioni e' fattorizzabile.\nLe fattorizzazioni le trovi nel file soluzione.txt. \n"

        # salvo nel file il risultato
        out_file = open("soluzione.txt", "w")
        for i in xrange(len(soluzione)):
            out_file.write(str(soluzione[i]) + str("\r\n"))
            print str(soluzione[i]) + str("\r\n")
        out_file.close()

    else:
        print "\nLe condizioni necessarie non sono verificate, la decomposizioni non e' fattorizzabile " \
              "e le classi massimali di parallelismo li trovi nel file soluzione2.txt. \n"
        indice = int(math.floor(k))
        soluzione = sol2(vet1, indice, vet_in)

        # salvo nel file il risultato
        f_out = open("soluzione2.txt", "w")
        for riga in soluzione:
            f_out.write(str(riga) + str("\r\n"))
            print str(riga) + str("\r\n")
        f_out.close()
