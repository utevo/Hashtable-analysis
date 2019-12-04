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

Tworzy tablicę mieszającą posiadającą ROWS wierszy oraz
COLUMNS column.

**Args:**

- rows (int): Ilość wierszy tablicy mieszającej.
- columns (int): Ilość kolumn tablicy mieszającej.

Komendy:
--------

IO:
"""
.. code-block:: bash

  hashtable [OPTIONS] ROWS COLUMNS io [OPTIONS] INPUT OUTPUT

Pobiera słowa z INPUT. Potem dodaje je wszystkie do tablicy mieszającej.
Następnie na OUTPUT zostaje wygenerowany wewnętrzny stan tablicy
mieszającej.

**Args:**

- input (file): Plik na podstawie którego będą generowane dane.
- output (file): Plik do którego zostanie przekazany wynik.


GENERATE:
"""""""""
.. code-block:: bash

  hashtable [OPTIONS] ROWS COLUMNS generate [OPTIONS] INPUT OUTPUT NUMBER_OF_WORDS

Generuje NUMBER_OF_WORDS słow na podstawie INPUT. Potem dodaje je
wszystkie do tablicy mieszającej. Następnie na OUTPUT zostaje
wygenerowany wewnętrzny stan tablicy mieszającej.

**Args:**

- input (file): Plik na podstawie którego będą generowane dane.
- output (file): Plik do którego zostanie przekazany wynik.
- number_of_words (int): Liczba generowanych słów.


BENCHMARK:
"""""""""
.. code-block:: bash

  hashtable [OPTIONS] ROWS COLUMNS benchmark [OPTIONS] INPUT OUTPUT INITIAL_NUMBER_OF_WORDS STEP NUMBER_OF_PROBLEMS NUMBER_OF_INSTANCES

Wykonuje funckję generate z pomiarem czasu dla rosnącej wartości
NUMBER_OF_WORDS. Przeprowadza porównanie ze słożonością teoretyczną.

**Args:**

- input (file): Plik na podstawie którego będą generowane dane.
- output (file): Plik do którego zostanie przekazany wynik.
- initial_number_of_words (int): Początkowa wartość NUMBER_OF_WORDS.
- step (int): Krok o ile będzie zwiększana wartość NUMBER_OF_WORDS.
- number_of_problems (int): Ilość rozwiązywanych problemów.
- number_of_insances (int): Ilość instancji problemu.

