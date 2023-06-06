"""
data.py


This module is intended for dataset abstractions,
comprising data generation, I/O, and `DataModule`
and `Dataset` definitions.
"""
from abc import abstractmethod, abstractstaticmethod
from os import environ
from typing import Iterable, List, Optional, Type, Union

import pytorch_lightning as pl
import torch
from torch.utils.data import DataLoader, Dataset, random_split

from {{cookiecutter.package_name}}.pipeline import transforms as t
from {{cookiecutter.package_name}}.common.classes import AbstractDataStructure


class AbstractDataset(Dataset):
    """
    Provides a template for dataset abstraction.
    """

    def __init__(self, transforms: Optional[List[t.AbstractTransform]] = None) -> None:
        super().__init__()
        self._transforms = transforms

    __return_type__ = AbstractDataStructure

    @abstractmethod
    def __len__(self) -> int:
        ...

    @abstractmethod
    def __getitem__(self, index: int) -> AbstractDataStructure:
        ...

    def __index__(self, index: int) -> AbstractDataStructure:
        return self.__getitem__(index)

    @abstractstaticmethod
    def collate_fn(*args, **kwargs):
        ...

    @property
    def multiindex(self) -> List[Iterable[int]]:
        ...

    @multiindex.setter
    @abstractmethod
    def multiindex(self) -> None:
        ...


class AbstractDataModule(pl.LightningDataModule):
    """
    Creates a boilerplate data module. Usage would be to
    create your own data module, inheriting off this class.
    This mostly sets up the random splitting of train,
    validation, and test datasets.

    A concise reminder of what the different datasets represent:
    - Training is used to fit the model.
    - Validation is used for hyperparameter tuning.
    - Test is used for evaluating generalization with tuned models.

    For this reason, the `test_size` argument is required, but
    `val_size` is optional; you might not tune hyperparameters
    but you better test your model!

    The split is controlled either by PyTorch Lightning's
    `seed_everything` function, which in turn sets an environment
    variable that is referenced in the `random_split` call, or
    a default seed value.
    """

    def __init__(
        self,
        dataset: Dataset,
        batch_size: int,
        test_size: float,
        val_size: float = 0.0,
        num_workers: int = 0,
    ):
        super().__init__()
        self._dataset = dataset
        self.val_size = val_size
        self.test_size = test_size
        self.batch_size = batch_size
        self.num_workers = num_workers
        self.save_hyperparameters()

    @property
    def test_size(self) -> float:
        return self._test_size

    @test_size.setter
    def test_size(self, value: float) -> None:
        assert 0.0 <= value + self.val_size <= 1.0
        self._test_size = value

    @property
    def val_size(self) -> float:
        return self._val_size

    @val_size.setter
    def val_size(self, value: float) -> None:
        assert 0.0 <= value + self.test_size <= 1.0
        self._val_size = value

    @property
    def batch_size(self) -> int:
        return self._batch_size

    @batch_size.setter
    def batch_size(self, value: int) -> None:
        assert 1 <= value
        self._batch_size = value

    def setup(self, stage: Union[str, None] = None) -> None:
        # we'll use the PyTorch Lightning seed if `seed_everything` is used
        seed = int(environ.get("PL_GLOBAL_SEED", 42))
        train_size = len(self._dataset) - (self.test_size + self.val_size)
        sizes = [train_size, self.test_size, self.val_size]
        sets = random_split(self._dataset, sizes, torch.Generator().manual_seed(seed))
        # store the splits as dictionaries
        self.data_splits = {
            name: data for name, data in zip(["train", "test", "val"], sets)
        }

    def train_dataloader(self) -> Type[DataLoader]:
        split = self.data_splits.get("train")
        return DataLoader(
            split,
            batch_size=self.batch_size,
            shuffle=True,
            num_workers=self.num_workers,
        )

    def test_dataloader(self) -> Type[DataLoader]:
        split = self.data_splits.get("test")
        return DataLoader(
            split,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
            shuffle=False,
        )

    def val_dataloader(self) -> Type[DataLoader]:
        split = self.data_splits.get("val")
        return DataLoader(
            split,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
            shuffle=False,
        )

    def predict_dataloader(self) -> DataLoader:
        return DataLoader(
            self._dataset,
            batch_size=self.batch_size,
            num_worers=self.num_workers,
            shuffle=False,
        )
