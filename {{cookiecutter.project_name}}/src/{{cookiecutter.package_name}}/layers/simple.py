from typing import Any, Dict, Optional

import torch
from torch import nn

from {{cookiecutter.package_name}} import registry
from {{cookiecutter.package_name}}.common.types import OptionalLayer
from {{cookiecutter.package_name}}.common import instantiate_class_from_args


@registry.register_layer("MLPBlock")
class MLPBlock(nn.Module):
    def __init__(
        self,
        input_dim: int,
        output_dim: int,
        norm: OptionalLayer = None,
        norm_kwargs: Optional[Dict[str, Any]] = None,
        activation: OptionalLayer = None,
        act_kwargs: Optional[Dict[str, Any]] = None,
        residual: bool = True,
    ) -> None:
        super().__init__()
        if residual:
            assert (
                input_dim == output_dim
            ), f"Residual connection requested, but input_dim != output_dim."
        self.residual = residual
        if norm:
            norm = instantiate_class_from_args(norm, norm_kwargs)
        else:
            norm = nn.Identity()
        self.norm = norm
        if activation:
            activation = instantiate_class_from_args(activation, act_kwargs)
        else:
            activation = nn.Identity()
        self.activation = activation
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, data: torch.Tensor) -> torch.Tensor:
        out = self.linear(data)
        out = self.activation(out)
        out = self.norm(out)
        if self.residual:
            out += data
        return out
