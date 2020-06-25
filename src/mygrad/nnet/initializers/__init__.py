from mygrad.tensor_creation.funcs import identity
from .constant import constant
from .glorot_normal import glorot_normal

__all__ = [
    "constant",
    "glorot_normal",
    "identity",
]
