from typing import Optional
import typer
from snoodle_test import __app_name__, __version__, runner


app = typer.Typer()


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.command()
def test(path=typer.Argument()):
    """
    Will run the test runner for the passed in directory path.
    :parameter path Directory path for your test files
    """
    runner.Runner(path)


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
