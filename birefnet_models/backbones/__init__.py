"""
Backbone networks for BiRefNet.

This package contains various backbone architectures including PVT, Swin Transformer,
VGG, and ResNet variants for feature extraction.
"""

from .build_backbone import build_backbone, load_weights
from .pvt_v2 import pvt_v2_b0, pvt_v2_b1, pvt_v2_b2, pvt_v2_b5
from .swin_v1 import swin_v1_t, swin_v1_s, swin_v1_b, swin_v1_l

__all__ = [
    'build_backbone',
    'load_weights',
    'pvt_v2_b0',
    'pvt_v2_b1', 
    'pvt_v2_b2',
    'pvt_v2_b5',
    'swin_v1_t',
    'swin_v1_s',
    'swin_v1_b',
    'swin_v1_l'
] 