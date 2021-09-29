
"""
models.py

This module is intended for *composed* models; i.e.
ready to training/usage, based off of layers defined in
either `torch`, other packages, or in `{{cookiecutter.package_name}}.layers`.
"""

import torch
from torch import Tensor      # this is used for type annotations
from torch import nn
import wandb
import pytorch_lightning as pl

from {{cookiecutter.package_name}} import layers
