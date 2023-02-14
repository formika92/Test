import click
import uvicorn


@click.group()
def cli() -> None:
    pass


@cli.command(name="runserver", help="Run server via uvicorn")  # noqa: WPS211, WPS216
@click.option("-h", "--host", type=str, default="127.0.0.1", help="Server host")
@click.option("-p", "--port", type=int, default=8000, help="Listening port")
@click.option("-r", "--reload/--no-reload", type=bool, default=False, help="Reload server when saving")
def run_server(  # noqa: WPS211, WPS216
    host: str,
    port: int,
    reload: bool,
) -> None:
    app = "app:app"
    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=reload,
        timeout_keep_alive=20
    )
