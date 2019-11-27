import time
import statistics

import click

from hashtableanalysis.hashtable.hashtable import (
    Hashtable, HashtableViewer)
from hashtableanalysis.cleartext.cleartext import cleartext
from hashtableanalysis.wordgenerator.wordgenerator import wordgenerator
from . import __version__


def add_n_elemnts_from_word_generator_to_hashtable(number_of_words,
                                                   wordgenerator, hashtable):
    for __ in range(number_of_words):
        word = next(wordgenerator)
        hashtable.add(word)


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

    add_n_elemnts_from_word_generator_to_hashtable(number_of_words,
                                                   word_generator, hashtable)

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
    text = input.read()
    words = cleartext(text)
    word_generator = wordgenerator(words)
    
    number_of_words = initial_number_of_words
    mean_exec_time_for_problems = []
    for __ in range(number_of_problems):

        exec_times_for_problem = []
        for __ in range(number_of_instances):
            hashtable = Hashtable(10000)

            start_time = time.time()
            add_n_elemnts_from_word_generator_to_hashtable(number_of_words,
                                                           word_generator, hashtable)
            end_time = time.time()

            exec_time_for_instance = end_time - start_time
            exec_times_for_problem.append(exec_time_for_instance)
            
        mean_exec_time_for_problem = statistics.mean(exec_times_for_problem)
        mean_exec_time_for_problems.append(mean_exec_time_for_problem)
        number_of_words += step
    
    n_values = []
    number_of_words = initial_number_of_words
    for __ in range(number_of_problems):
        n_values.append(number_of_words)
        number_of_words += step

    # t_t(n) = O(n)
    median_index = number_of_problems // 2
    median_of_n_values = n_values[median_index]
    mean_exec_time_for_median = mean_exec_time_for_problems[median_index]
    # 1 = mean_exec_time_for_median / C * median_of_n_valus
    #       ||
    #       \/
    # C = mean_exec_time_for_median / median_of_n_valus
    C = mean_exec_time_for_median / median_of_n_values


    t_values = mean_exec_time_for_problems

    q_values = [None] * number_of_problems
    for index in range(number_of_problems):
        q_values[index] = t_values[index] / (C * n_values[index])


    print('n_values', n_values)
    print('t_values', t_values)
    print('q_values', q_values)

    
cli.add_command(io)
cli.add_command(generate)
cli.add_command(benchmark)


if __name__ == '__main__':
    cli()
