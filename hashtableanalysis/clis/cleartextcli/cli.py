import sys

import click

from hashtableanalysis.cleartext import cleartext


@click.command
def main():
    input = sys.stdin.read()
    output = cleartext(input)
    return output


if __name__ == '__main__':
    main()