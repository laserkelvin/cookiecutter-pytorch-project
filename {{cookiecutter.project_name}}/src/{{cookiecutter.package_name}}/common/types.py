
from typing import Union, Dict

from torch import Tensor

# addes convenient types for annotation
DataType = Union[float, int, Tensor]
InputType = Union[Dict[str, DataType], DataType]
