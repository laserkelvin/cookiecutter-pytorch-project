
from typing import Union, Dict, Optional, Type

from torch import Tensor, nn

# addes convenient types for annotation
DataType = Union[float, int, Tensor]
InputType = Union[Dict[str, DataType], DataType]

# types that are optional types/modules
OptionalLayer = Optional[Union[nn.Module, Type[nn.Module]]]
