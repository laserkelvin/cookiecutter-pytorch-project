from __future__ import annotations
from typing import Optional, Union, Dict, List, Any

import torch
from torch import Tensor
import numpy as np

from {{cookiecutter.package_name}}.common.types import DataType


class DataStructure(object):
    def __init__(
        self,
        inputs: Optional[Dict[str, DataType]] = None,
        targets: Optional[Dict[str, DataType]] = None,
        **kwargs,
    ) -> None:
        self.inputs = inputs
        self.targets = targets
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.keys = list(sorted(kwargs.keys()))

    @property
    def inputs(self) -> Dict[str, DataType]:
        return self._inputs

    @inputs.setter
    def inputs(self, data: Union[None, Dict[str, DataType]]) -> None:
        if not data:
            data = {}
        self._inputs = data

    @property
    def targets(self) -> Dict[str, DataType]:
        return self._targets

    @targets.setter
    def targets(self, data: Union[None, Dict[str, DataType]]) -> None:
        if not data:
            data = {}
        self._targets = data


def collate_nested_data(data: List[Any]) -> Union[Tensor, List[str], Dict[str, Tensor]]:
    """
    Converts arrays of structs to a struct of arrays.

    Basically aggregates elements within a list of data into packed
    data structures, preferably `torch.Tensor`s. Currently, the
    function can operate on dictionaries (recursively), tensors,

    Parameters
    ----------
    data : List[Any]
        List of data to collate

    Returns
    -------
    Union[Tensor, List[str], Dict[str, Tensor]]
    """
    sample = data[0]
    # for data contained in dictionaries, this function is applied recursively
    if isinstance(sample, dict):
        result = {}
        for key in sample.keys():
            result[key] = collate_nested_data([s[key] for s in data])
    # for tensors, try and stack them together if they have the same shapes
    elif isinstance(sample, Tensor):
        # assumes batch first
        assert (
            len(set([d.shape for d in data])) == 1
        ), f"Tensor shapes are irregular and cannot be stacked; please implement a padding function."
        result = torch.vstack(data)
    elif isinstance(sample, np.ndarray):
        assert (
            len(set([d.shape for d in data])) == 1
        ), f"NDArray shapes are irregular and cannot be stacked; please implement a padding function."
        result = torch.from_numpy(np.vstack(data))
    elif isinstance(sample, (float, int)):
        # check if every entry is an integer, and if so, we make sure tensor is cast appropriately
        all_ints = all([float(d).is_integer() for d in data])
        result = torch.tensor(data)
        if all_ints:
            result = result.long()
    # just copy over strings
    elif isinstance(sample, str):
        result = data
    else:
        raise NotImplementedError(
            f"Trying to collate data of unsupported type: {type(sample)}, value {sample}"
        )
    return result
