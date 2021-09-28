
"""
models.py

This module is intended for *composed* models; i.e.
ready to training/usage, based off of layers defined in
either `torch`, other packages, or in `{{cookiecutter.package_name}}.layers`.
"""

from torch import nn
import wandb
import pytorch_lightning as pl

