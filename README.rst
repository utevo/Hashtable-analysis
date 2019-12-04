##################
Hashtable Analysis
##################

******
Autor:
******
Michał Kowieski 293130

**************
Treść zadania:
**************
Przedmiotem analizy jest tablica mieszająca: tablica przechowuje rekordy zawierające napisy. Długość
tablicy jest ograniczona arbitralnie przez pewną stałą K. Dla danego napisu s obliczamy k=M(s) i
umieszczamy strukturę reprezentującą napis w tablicy mieszającej: H[k]. W przypadku kolizji funkcji
mieszającej (H[k] zajęte) reprezentujące napis s struktury danych zapisywane są w sposób
alternatywny zobacz warianty). Przedmiotem implementacji powinno być: dodanie i usunięcie
elementów w H[]. Wybór funkcji mieszającej M(s) do decyzji projektanta - ale patrz wariant 3


**W13:**
tablica H[k,n] (gdzie n=0...N) jest dwuwymiarowe, elementy kolidujące zapisywane są w lokalizacjach H[k,0], H[k,1], itd. (Oczywiście, przekroczenie przez drugi indeks rozmiaru tablicy będzie powodować odrzucenie elementu)

**W21:**
Testy przeprowadzić dla: listy słów języka polskiego wygenerowanych z zadanych tekstów. Generator należy wykonać samodzielnie.

**W31:**
Zastosować jedną funkcję mieszającą; dodatkowo przeprowadzić analizę dla enumeracji tablicy (wydobycia wszystkich elementów).

*******************
Działanie programu:
*******************

Na wejście program dostaje ciąg napisów. Najpierw dodaje je wszystkie do tablicy. Następnie generuje wewnętrzny stan tablicy mieszającej (jakie napisy się tam znajdują oraz w których są "kubełkach"). Ten stan zwraca użytkownikowi.

************************
Korzystanie z  programu:
************************

Program główny:
===============

.. code-block:: bash

  hashtable [OPTIONS] ROWS COLUMNS COMMAND [ARGS]


Argumenty:
----------

- ROWS - ilość wierszy w tablicy mieszającej
- COLUMNS - ilość kolumn w tablicy mieszającej
- COMMAND - konretne komenda aplikacji

Komendy:
--------

IO:
^^^
.. code-block:: bash

  hashtable [OPTIONS] ROWS COLUMNS io [OPTIONS] INPUT OUTPUT

Pobiera słowa z INPUT. Potem dodaje je wszystkie do tablicy mieszającej.
Następnie na OUTPUT zostaje wygenerowany wewnętrzny stan tablicy
mieszającej.

Pobiera słowa z pliku foo.txt i zwraca wynik programu do pliku bar.txt:
hashtable io foo.txt bar.txt







