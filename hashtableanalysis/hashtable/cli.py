import click

from . import __version__


@click.group()
def cli():
    pass


@click.command()
@click.version_option(version=__version__)
def io(input, n):
    pass


@click.command()
@click.version_option(version=__version__)
def generate(input, n):
    pass


@click.command()
@click.version_option(version=__version__)
def benchmark(input, n):
    pass


cli.add_command(io)
cli.add_command(generate)
cli.add_command(benchmark)


if __name__ == '__main__':
    cli()
