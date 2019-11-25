import sys

import click

from hashtableanalysis.cleartext.cleartext import cleartext
from hashtableanalysis.wordgenerator.wordgenerator import wordgenerator
from . import __version__


@click.command()
@click.version_option(version=__version__)
@click.argument('input', type=click.File('r'))
@click.argument('output', type=click.File('w'))
@click.argument('number_of_words', type=click.INT)
def cli(input, output, number_of_words):
    """
    \b
    Geberate 10 words based on the stdin to stdout:
        wordgenerator - - 10
    \b
    Geberate 30 words based on the file foo.txt to stdout:
        wordgenerator foo.txt - 30
    \b
    Geberate 50 words based on the file stdin into the file bar.txt
        wordgenerator - bar.txt 50
    """
    text = input.read()
    words = cleartext(text)

    if not words:
        raise ValueError("In input there aren't any words.")

    word_generator = wordgenerator(words)

    for __ in range(number_of_words):
        word = next(word_generator)
        output.write(word + '\n')


if __name__ == '__main__':
    cli()