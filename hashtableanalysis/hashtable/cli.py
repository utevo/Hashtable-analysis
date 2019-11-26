import click

from hashtableanalysis.hashtable.hashtable import (
    Hashtable, HashtableViewer)
from hashtableanalysis.cleartext.cleartext import cleartext
from hashtableanalysis.wordgenerator.wordgenerator import wordgenerator
from . import __version__


@click.group()
@click.version_option(version=__version__)
def cli():
    pass


@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
def io(input, output):
    """Pobiera słowa z INPUT. Potem dodaje je wszystkie do tablicy
    mieszającej. Następnie na OUTPUT zostaje wygenerowany wewnętrzny
    stan tablicy mieszającej.

    \b
    Pobiera słowa z pliku foo.txt i zwraca wynik programu do pliku bar.txt:
        hashtable io foo.txt bar.txt
    """
    text = input.read()
    words = text.split('\n')
    hashtable = Hashtable()

    for word in words:
        hashtable.add(word)

    viewer = HashtableViewer(hashtable)
    df = viewer.low_level()
    print(df.to_string(), file=output)


@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
@click.argument('number_of_words', type=click.INT)
def generate(input, output, number_of_words):
    """Generuje NUMBER_OF_WORDS słow na podstawie INPUT. Potem dodaje je
    wszystkie do tablicy mieszającej. Następnie na OUTPUT zostaje 
    wygenerowany wewnętrzny stan tablicy mieszającej.
    """
    text = input.read()
    words = cleartext(text)
    word_generator = wordgenerator(words)
    hashtable = Hashtable()

    for __ in range(number_of_words):
        new_word = next(word_generator)
        hashtable.add(new_word)

    viewer = HashtableViewer(hashtable)
    df = viewer.low_level()
    print(df.to_string(), file=output)


@click.command()
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
@click.argument('initial_number_of_words', type=click.INT)
@click.argument('step', type=click.INT)
@click.argument('number_of_problems', type=click.INT)
@click.argument('number_of_instances', type=click.INT)
def benchmark(input, output, initial_number_of_words, step,
              number_of_problems, number_of_instances):
    """Wykonuje funckję generate z pomiarem czasu dla rosnącej wartości 
    NUMBER_OF_WORDS. Przeprowadza porównanie ze słożonością teoretyczną.

    Args:
        input (file): Plik na podstawie którego będą generowane dane.
        output (file): Plik do którego zostanie przekazany wynik.
        initial_number_of_words (int): Początkowa wartość NUMBER_OF_WORDS.
        step (int): Krok o ile będzie zwiększana wartość NUMBER_OF_WORDS.
        number_of_problems (int): Ilość rozwiązywanych problemów.
        number_of_insances (int): Ilość instancji problemu.
    """
    pass


cli.add_command(io)
cli.add_command(generate)
cli.add_command(benchmark)


if __name__ == '__main__':
    cli()
