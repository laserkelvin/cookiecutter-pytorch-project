from __future__ import annotations

from abc import ABC, abstractproperty, abstractstaticmethod
from dataclasses import dataclass
from typing import Any, Iterable


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

    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)

    def __setitem__(self, key: str, value: Any):
        setattr(self, key, value)

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
