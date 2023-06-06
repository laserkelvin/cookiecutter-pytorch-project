from abc import ABC, abstractmethod 

from {{cookiecutter.package_name}}.common.classes import AbstractDataStructure
from {{cookiecutter.package_name}} import registry


class AbstractTransform(ABC):
    """
    Abstract transform class: basically lays out the
    recipe for transforms to take a data sample, a
    subclas of `AbstractDataStructure`, perform the
    modifications, then return the result.
    """
    @abstractmethod
    def __call__(self, sample: AbstractDataStructure) -> AbstractDataStructure:
        ...

