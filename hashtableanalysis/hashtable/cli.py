import click

from hashtableanalysis.hashtable.hashtable import (
    Hashtable, HashtableViewer)
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
    pass


@click.command()
def generate(input, n):
    pass


@click.command()
def benchmark(input, n):
    pass


cli.add_command(io)
cli.add_command(generate)
cli.add_command(benchmark)


if __name__ == '__main__':
    cli()
