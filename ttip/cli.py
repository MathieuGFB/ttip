"""TTiP module for CLI"""
# ttip/cli.py

from typing import Optional

import typer, os

from ttip import (
    __app_name__,
    __version__,
    ttip
)

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()
    
@app.command()
def verify(
    path_to_tree: str,
    verbose: Optional[bool] = typer.Option(
        False,
        "--verbose",
        help = "Bring extra information during computation"
   )
) -> ttip.verify:
    """
    Check the validity of the trees stored in the provided file.
    """
    try:
        os.path.exists(path_to_tree)
    except:
        print(f"The provided path, {path_to_tree}, does not seems to be a valid one. Please, check it.")
    else:
        return ttip.verify(path_to_tree, verbose)

@app.command()
def merge(
    path_to_main_tree: str,
    path_to_subtree: str,
    keyword: str,
    verbose: Optional[bool] = typer.Option(
       None,
       "--verbose",
       help = "Bring extra information during computation"
   ),
    check: Optional[bool] = typer.Option(
       None,
       "--verify",
       help = "Check the validity of the trees before merging"
   )
) -> ttip.merge:
    """
    Replace the provided keyword in the main tree by the subtree.
    """
    try:
        os.path.exists(path_to_main_tree)
    except:
        print(f"The provided path, {path_to_main_tree}, does not seems to be a valid one. Please, check it.")
    else:
        try:
            os.path.exists(path_to_subtree)
        except:
            print(f"The provided path, {path_to_subtree}, does not seems to be a valid one. Please, check it.")
        else:
            return ttip.merge(path_to_main_tree, path_to_subtree, keyword, verbose)
        
@app.command()
def convert(
    path_to_tree: str,
    to_format: str,
    verbose: Optional[bool] = typer.Option(
        None,
        "--verbose",
        help = "Bring extra information during computation"
    ),
    check: Optional[bool] = typer.Option(
       None,
       "--verify",
       help = "Check the validity of the trees before merging"
   )
) -> ttip.convert:
    """
    Convert a file from a designated format to another format. (WIP)
    """
    try:
        os.path.exists(path_to_tree)
    except:
        print(f"The provided path, {path_to_tree}, does not seems to be a valid one. Please, check it.")
    else:
        return ttip.convert(path_to_tree, to_format, check, verbose)

@app.command()
def calibrate(
    path_to_tree: str,
    verbose: Optional[bool] = typer.Option(
        None,
        "--verbose",
        help = "Bring extra information during computation"
    )
) -> ttip.calibrate:
    """
    Calibrate the nodes of a phylogeny. (WIP)
    """
    try:
        os.path.exists(path_to_tree)
    except:
        print(f"The provided path, {path_to_tree}, does not seems to be a valid one. Please, check it.")
    else:
        return ttip.convert(path_to_tree, verbose)

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        help = "Show the application's version and exit",
        callback = _version_callback,
        is_eager = True
    )
) -> None:
    return