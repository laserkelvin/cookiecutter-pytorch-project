
"""
data.py


This module is intended for dataset abstractions,
comprising data generation, I/O, and `DataModule`
and `Dataset` definitions.
"""
from abc import abstractmethod
from typing import Union, Type
from os import environ
from warnings import warn

import torch
from torch.utils.data import DataLoader, Dataset, random_split
import pytorch_lightning as pl

from {{cookiecutter.package_name}} import get_paths


class AbstractDataset(Dataset):
    def __len__(self) -> int:
        raise NotImplementedError()


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
        dataset: Type[Dataset], 
        batch_size: int, 
        test_size: float,
        val_size: float = 0.,
        num_workers: int = 1
        ):
        super().__init__()
        self.dataset = dataset
        self.val_size = val_size
        self.test_size = test_size
        self.batch_size = batch_size
        self.num_workers = num_workers

    @property
    def test_size(self) -> float:
        return self._test_size

    @test_size.setter
    def test_size(self, value: float) -> None:
        assert 0. <= value + self.val_size <= 1.
        self._test_size = value

    @property
    def val_size(self) -> float:
        return self._val_size

    @val_size.setter
    def val_size(self, value: float) -> None:
        assert 0. <= value + self.test_size <= 1.
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
        seed = environ.get("PL_GLOBAL_SEED", 42)
        train_size = len(self.dataset) - (self.test_size + self.val_size)
        sizes = [train_size, self.test_size]
        # sometimes we don't always use a test set
        if self.val_size > 0.:
            sizes.append(self.val_size)
        sets = random_split(self.dataset, sizes, torch.Generator().manual_seed(seed))
        # store the splits as dictionaries
        self.data_splits = {name: data for name, data in zip(["train", "test", "val"], sets)}

    def train_dataloader(self) -> Type[DataLoader]:
        split = self.data_splits.get("train")
        return DataLoader(split,
            batch_size=self.batch_size,
            shuffle=True,
            num_workers=self.num_workers
            )

    def test_dataloader(self) -> Type[DataLoader]:
        split = self.data_splits.get("test")
        return DataLoader(split,
            batch_size=self.batch_size,
            num_workers=self.num_workers
            )

    def val_dataloader(self) -> Type[DataLoader]:
        # if the test set is not used, return the parent method
        if self.val_size == 0.:
            warn(f"Validation set size is zero!")
            return super().val_dataloader()
        split = self.data_splits.get("val")
        return DataLoader(split,
            batch_size=self.batch_size,
            num_workers=self.num_workers
            )
