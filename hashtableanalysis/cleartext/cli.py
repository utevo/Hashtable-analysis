import sys

import click

from hashtableanalysis.cleartext.cleartext import cleartext
from . import __version__


@click.command(name='cleartext')
@click.version_option(version=__version__)
def main():
    input = sys.stdin.read()
    output = cleartext(input)
    click.echo(output)


if __name__ == '__main__':
    main()
