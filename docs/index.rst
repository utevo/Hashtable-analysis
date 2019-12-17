.. HashtableAnalysis documentation master file, created by
   sphinx-quickstart on Sun Nov 10 19:48:15 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

HashtableAnalysis dokumentacja
=============================================

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


**************************
Opis implementacji:
**************************

###################
Oczyszczacz tekstu:
###################
**Algorytm:**

1. Podziel tekst na pojedyńcze słowa
2. Dla każdego słowa
    1. Usuń znaki które nie są literami z początku słowa
    2. Usuń znaki które nie są literami z końca słowa
3. Zwróć słowa składające się tylko ze znaków

###############
Generator słów:
###############
Na podstawie danej listy słów generator zwraca z jednakowyn rozkładem
każde ze słów.

###################
Funkcja mieszająca:
###################
Zastosowana została tak zwana "wielomianowa mieszająca funkcja krocząca" (ang. polynomial rolling hash function).
::

  hash(s) = s[0] + s[1] * p + s[2] * p^2 + ... + s[n-1] * p^(n-1) mod m

- s - napis dla którego chcemy wyliczyć wartość skrótu
- n - długość napisu s
- m - duża stała
- p - duża stała

###################
Tablica mieszająca:
###################
Tablica mieszająca przechowuje napisy i ich hash'e w tablicy dwuwymiarowej.
Elementy kolidujące zapisywane są w lokalizacjach H[k,0], H[k,1], itd.
Przekroczenie przez drugi indeks rozmiaru tablicy odrzuca element.


**************************
Analiza złożoności:
**************************

###################
Funkcja mieszająca:
###################
Wyliczanie wartości funkcji mieszającej polega na iteracji po wszystkich literach słowa.
Pojedyńczy krok wymaga stałą ilość operacji.

Obliczenia: 1 * n = n
Złożoność: O(n)

- n - długość słowa

###################
Tablica mieszająca:
###################

Założenia:

- Napisy mają z góry określoną maksymalną długość
- Wartość współczynnika załadowania (ilość elementów tablicy / ilość wierszy tablicy) jest mniejsza od 1


**Dodawanie elementu:**

Żeby dodwać dany element najpierw musi wyznaczyć wartość funkcji skrótu dla tego słowa. Jako że napisy
posiadają ograniczenie na długość to złożoność liczenia wartości funckji mieszającej wynosi O(1).
Z wyliczonej wartości okreśmamy wiersz w którym ma znaleść się nasz napis. Ta operacja ma złożoność 0(1).
Teraz musimy znaleść pierwszą wolną komórkę tablicy. Jako że współczynnik załadowania jest mnieszy od 1 to
średni numer pierwszej wolnej komórki jest mniejszy od 1, a z tego wynika że koszt tej operacji wynosi średnio O(1).

Obliczenia: 1 * 1 * 1 = 1
Średnia złożoność: O(1)


Istnieje też możliwość że wszystkie napisy zostały dodane do tego samego wiersza. Wtedy znalezienie pierwszej wolnej
komórki może wymagać n (ilość elementów w tablicy) operacji. Takie zdażenie jest wielce nieprawdopodobne

Pesymistyczna złożoność: O(n)


**Usuwanie elementu:**

Żeby usunąć dany element najpierw musi wyznaczyć wartość funkcji skrótu dla tego słowa. Jako że napisy
posiadają ograniczenie na długość to złożoność liczenia wartości funckji mieszającej wynosi O(1).
Z wyliczonej wartości okreśmamy wiersz w którym ma znaleść się nasz napis. Ta operacja ma złożoność 0(1).
Teraz musimy znaleść pierwszą komórkę tablicy w której znajude się dany napis. Złożoność sprawdzenia czy
napisy są równe wynosi O(1) (z powodu oganiczonej długości). Jako że wartość współczynnika załadowania
jest mniejsza od 1 to średnia wartość wiersza szukanangeo napisu też jest mniejsza od 1.

Obliczenia: 1 * 1 * 1 * 1 = 1
Średnia złożoność: O(1)


Istnieje też możliwość że wszystkie napisy zostały dodane do tego samego wiersza. Wtedy znalezienie komórki w której 
znajduje się usuwany napis może wymagać n (ilość elementów w tablicy) operacji.  Takie zdażenie jest wielce nieprawdopodobne

Pesymistyczna złożoność: O(n)

