"""
Refinement modules for BiRefNet.

This package contains refinement components including the main refiner,
stem layer, and various refinement architectures for improving segmentation quality.
"""

from .refiner import Refiner, RefinerPVTInChannels4, RefUNet
from .stem_layer import StemLayer

__all__ = [
    'Refiner',
    'RefinerPVTInChannels4',
    'RefUNet',
    'StemLayer'
] 