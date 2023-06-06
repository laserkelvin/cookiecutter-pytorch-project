
from {{cookiecutter.package_name}}.data.abstract_classes import AbstractDataset
from {{cookiecutter.package_name}} import registry


@registry.register_data("ConcreteDataset")
class ConcreteDataset(AbstractDataset):
    ...
