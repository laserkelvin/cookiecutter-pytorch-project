from __future__ import annotations

from abc import ABC, abstractproperty, abstractstaticmethod
from dataclasses import dataclass
from typing import Any, Iterable, Optional

from torch import Tensor


@dataclass
class AbstractDataStructure(ABC):
    """
    Implements an abstract data structure, which is intended to
    be used to form a schema for expected key/data maps, with
    scalability from single samples to batches.

    This is intended to be used for everything from batched
    data to predictions.

    When you have concrete data, implement a subclass that
    inherits from `AbstractDataStructure` that includes all
    the key/data values you would expect.
    """

    def __getitem__(self, key: str, default: Optional[Any] = None) -> Any:
        return getattr(self, key, default)

    def __setitem__(self, key: str, value: Any):
        setattr(self, key, value)


    def get(self, key: str, default: Optional[Any] = None) -> Any:
        """
        User facing method for retrieving data, mimicking how dictionaries
        function.

        Parameters
        ----------
        key : str
            Key to retrieve from the structure.
        default : Optional[Any]
            Optional value to set as the default, if the key
            exists but doesn't contain data.

        Returns
        -------
        Any
            Data to be retrieved

        Raises
        ------
        KeyError:
            If `key` is not an attribute of this data structure.
        """
        if key not in dir(self):
            raise KeyError(f"{key} is not found in {self.__class__.__name__}.")
        return self.__getitem__(key, default)

    @property
    def is_batched(self) -> bool:
        return self.batch_size > 1

    @abstractstaticmethod
    def collate_fn(batch: Iterable[AbstractDataStructure]) -> AbstractDataStructure:
        """
        Function to collate samples together into a batch.

        Parameters
        ----------
        batch
            A collection of individual samples that will
            be collated together.

        Returns
        -------
        AbstractBatch

        """
        ...

    @abstractproperty
    def batch_size(self) -> int:
        """
        Return the batch size.

        Returns
        -------
        int
            Number of samples within the batch.
        """
        ...

    @property
    def is_not_finite(self) -> bool:
        """
        Convenient property to check if any tensors
        contained within this data structure has inf
        and/or nans.

        Returns
        -------
        bool
            True if there are any elements within the 
            structure that is not finite, else False.
        """
        for key in dir(self):
            attr = self.get(key)
            if isinstance(attr, Tensor):
                has_na = ~attr.isfinite().any()
                if has_na:
                    return True
        return False
