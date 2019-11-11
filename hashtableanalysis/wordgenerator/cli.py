import sys

import click

from hashtableanalysis.cleartext.cleartext import cleartext
from hashtableanalysis.wordgenerator.wordgenerator import wordgenerator
from . import __version__


@click.command()
@click.version_option(version=__version__)
@click.argument('input', type=click.File('r'))
@click.argument('n', type=click.INT)
def main(input, n):
    text = input.read()
    words = cleartext(text)

    word_generator = wordgenerator(words)

    for __ in range(n):
        word = next(word_generator)
        click.echo(word)


if __name__ == '__main__':
    main()