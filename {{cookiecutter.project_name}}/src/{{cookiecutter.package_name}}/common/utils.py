from typing import Dict, Mapping, Optional, Type, Union, Any
from pathlib import Path
from inspect import signature

from torch import nn

from {{cookiecutter.package_name}} import registry
from {{cookiecutter.package_name}}.common.types import OptionalLayer


src_path = Path(__file__)
top = src_path.parents[1].absolute()


def get_paths() -> Dict[str, Path]:
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
        "scripts": top.joinpath("scripts"),
    }
    for subfolder in ["raw", "interim", "external", "processed"]:
        paths[subfolder] = paths.get("data").joinpath(subfolder)
    return paths


def instantiate_class_from_args(
    ref: Union[str, nn.Module, Type[nn.Module]],
    ref_kwargs: Optional[Mapping[str, Any]] = None,
) -> nn.Module:
    """
    Construct a PyTorch module, given either a string, class type, or an object as is.

    If `ref` is provided as a string, we search for the class type within the registry.
    With the type at hand, we attempt to construct it, passing valid kwargs after
    inspecting the type.

    Parameters
    ----------
    ref : Union[str, nn.Module, Type[nn.Module]]
        Either a string, a class type, or an instance of a subclass of `nn.Module`.
    ref_kwargs : Optional[Mapping[str, Any]] = None
        Keyword arguments to pass into object creation

    Returns
    -------
    nn.Module
        Instance of the target class
    """
    if isinstance(ref, str):
        ref = registry.get(ref)
    if isinstance(ref, Type):
        if ref_kwargs:
            sig = signature(ref)
            for key in ref_kwargs:
                if key not in sig.parameters and "kwargs" not in sig.parameters:
                    raise KeyError(
                        f"Tried to pass {key} into {ref}, which does not accept this argument and/or kwargs."
                    )
            obj = ref(**ref_kwargs)
        else:
            obj = ref()
    if isinstance(ref, nn.Module):
        obj = ref
    else:
        raise NotImplementedError(
            f"{ref} is not recognized and could not be instantiated."
        )
    return obj
