
from typing import Dict, Type
from pathlib import Path


src_path = Path(__file__)
top = src_path.parents[1].absolute()


def get_paths() -> Dict[str, Type[Path]]:
    """
    Retrieve a dictionary containing the absolute paths
    for this project. This provides a simple method for
    traversing and referencing files outside the current
    working directory, particularly for scripts and notebooks.
    """
    paths = {
        "data": top.joinpath("data"),
        "models": top.joinpath("models"),
        "notebooks": top.joinpath("notebooks"),
        "scripts": top.joinpath("scripts")
    }
    for subfolder in ["raw", "interim", "external", "processed"]:
        paths[subfolder] = paths.get("data").joinpath(subfolder)
    return paths

