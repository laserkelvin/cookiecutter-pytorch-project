from __future__ import annotations
from typing import Type, Union
from functools import lru_cache

from torch import nn


"""
This implements a registry pattern, which provides a singular interface
to access classes defined all over the package.
"""


class Registry:

    _LAYERS = {}
    _MODELS = {}
    _TASKS = {}
    _DATA = {}
    _TRANSFORMS = {}

    # add all of nn into _LAYERS for easy access
    for key in dir(nn):
        ref = getattr(nn, key)
        if isinstance(ref, Type) and issubclass(ref, nn.Module):
            _LAYERS[key] = ref

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

    @classmethod
    def register_transform(cls: Type[Registry], name: str):
        def wrapper(_class: Type) -> Type:
            cls._TRANSFORMS[name] = _class
            return _class

        return wrapper

    @lru_cache()
    def get(self, name: str) -> Union[Type, None]:
        for category in [
            self._LAYERS,
            self._MODELS,
            self._TASKS,
            self._DATA,
            self._TRANSFORMS,
        ]:
            for key, value in category.items():
                if name == key:
                    return value
        raise KeyError(f"{name} was requested from the registry, but cannot be found.")


# instantiate registry object to track everything
registry = Registry()
