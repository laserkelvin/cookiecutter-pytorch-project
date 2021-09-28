
"""
data.py


This module is intended for dataset abstractions,
comprising data generation, I/O, and `DataModule`
and `Dataset` definitions.
"""
from abc import abstractmethod
from typing import Union
from os import environ

from torch.utils.data import DataLoader, Dataset, random_split
import pytorch_lightning as pl

from {{cookiecutter.package_name}} import get_paths


class AbstractDataset(Dataset):
    def __len__(self) -> int:
        raise NotImplementedError()


class AbstractDataModule(pl.LightningDataModule):
    def __init__(self, dataset: Type[Dataset], batch_size: int, test_size: float, num_workers: int = 1):
        super().__init__()
        self.dataset = dataset
        self.test_size = test_size
        self.batch_size = batch_size
        self.num_workers = num_workers

    @property
    def test_size(self) -> float:
        return self._test_size

    @test_size.setter
    def test_size(self, value: float) -> None:
        assert 0. <= value <= 1.
        self._test_size = value

    @property
    def batch_size(self) -> int:
        return self._batch_size

    @batch_size.setter
    def batch_size(self, value: int) -> None:
        assert 1 <= value
        self._batch_size = value

    def setup(self, stage: Union[str, None] = None) -> None:
        # we'll use the PyTorch Lightning seed if `seed_everything`
        # is used
        seed = environ.get("PL_GLOBAL_SEED", 42)
        self.train_set, self.val_set = random_split(
            self.dataset,
            [len(self.dataset) - self.test_size, test_size],
            torch.Generator().manual_seed(seed)
            )

    def train_dataloader(self):
        return DataLoader(self.train_set,
            batch_size=self.batch_size,
            shuffle=True,
            num_workers=self.num_workers
            )
