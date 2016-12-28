Intro
======
Questo lavoro è frutto dello studio teorico/pratico a fini di tesi magistrale in Matematica della Dott.ssa Alessandra Pedullà.
Io sono mi sono limitato ad aiutarla nell'implementazione dell'algortomo in Python.

Il programma fornisce a partire da una G-decomposizione degli spigoli di un grafo completo su n vertici (K_n) tutte le eventuali G-fattorizzazioni.
In matematichese: ripartisce i blocchi del G-disegno in classi di parallelismo detti G-fattori e accorpa un opportuno numero di G-fattori tra loro per formare una G-fattorizzazione.

Requisiti
=========
L'algoritmo è stato scritto nel linguaggio di programmazione Python pertanto, per funzionare dovete installare sul vostro computer  l'interprete Python.

Di seguito la guida esplicativa:


[Link alla guida](http://bit.ly/2iEv9e9)

Struttura del progetto
======================

- **main.py** File principale del progetto.
- **algoritmo1.py** contiene l'algoritmo utilizzato quando le condizioni necessarie sono verificate.
- **algoritmo2.py** contiene l'algoritmo utilizzato quando le condizioni necessarie non sono verificate.
- **utilty.py** contiene delle funzioni di supporto

Il progetto viene corredato da file di input di esempio per testare il programma:
-	1fattK6FM.txt
-	P3 cn nf.txt
-	S2-4-16-FS.txt
-	STS13-NF.txt
-	STS7.txt

Uso
===
Aprire il terminale:
* su **MAC** : Applicazioni -> Utility -> Terminale.app
* su **Windows** : Start -> Esegui -> poi digitate "cmd" senza virgolette

recatevi nella cartella dove avete salvato il file e digitate


 `python main.py matrice-di-input `

 Esempio

 `python main.py 1fattK6FM.txt`

 La matrice di input che abbiamo preso in esempio ( che potrete trovare all'interno del file 1fattK6FM.txt) ha una forma del genere:

		1,2
		1,3
		1,4
		1,5
		1,6
		2,3
		2,4
		2,5
		2,6
		3,4
		3,5
		3,6
		4,5
		4,6
		5,6


Sullo schermo vi verrà chiesto di inserire l'ordine del grafo, la cardinalità dei blocchi e il numero dei blocchi.
Se non ci sono errori, vi verrà stampata la soluzione a schermo e salvata anche in un file chiamato "risultato.txt"

Esempio 2

Potete anche inserire a mano la matrice in input semplice avviando il programmando con il comando

`python main.py`


Note
====

Per matrici troppo grandi il tempo di esecuzione del programma risulta troppo lungo per un computer domestico. Si consiglia per tanto la prova all'interno del centro di calcolo universitario.
Il motivo è dettato dal numero di calcoli, imposti dall'algoritmo matematico.


Contatti
========
Per info o problemi vari

Email: info[chiocciola]gianlucabarranca[punto]it
