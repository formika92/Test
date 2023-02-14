import click

from app.management import command_sources  # isort:skip


@click.command(cls=click.CommandCollection, sources=command_sources)
def main(*_args, **_kwargs) -> None:
    pass


if __name__ == "__main__":
    main()
