from __future__ import annotations
from typing import Type


"""
This implements a registry pattern, which provides a singular interface
to access classes defined all over the package.
"""

class Registry:

    _LAYERS = {}
    _MODELS = {}
    _TASKS = {}
    _DATA = {}

    @classmethod
    def register_model(cls: Type[Registry], name: str):
        def wrapper(_class: Type) -> Type:
            cls._MODELS[name] = _class
            return _class
        return wrapper

    @classmethod
    def register_layer(cls: Type[Registry], name: str):
        def wrapper(_class: Type) -> Type:
            cls._LAYERS[name] = _class
            return _class
        return wrapper

    @classmethod
    def register_task(cls: Type[Registry], name: str):
        def wrapper(_class: Type) -> Type:
            cls._TASKS[name] = _class
            return _class
        return wrapper

    @classmethod
    def register_data(cls: Type[Registry], name: str):
        def wrapper(_class: Type) -> Type:
            cls._DATA[name] = _class
            return _class
        return wrapper


# instantiate registry object to track everything
registry = Registry()
