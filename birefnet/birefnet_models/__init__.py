"""
birefnet_models package for BiRefNet neural network models.

This package contains the main BiRefNet model architecture, backbone networks,
decoder modules, and refinement components for high-resolution dichotomous image segmentation.
"""

from birefnet.birefnet_models.birefnet_pipeline import BiRefNet, BiRefNetC2F, Decoder, SimpleConvs
from birefnet.birefnet_models.backbones.build_backbone import build_backbone, load_weights

__all__ = [
    'BiRefNet',
    'BiRefNetC2F', 
    'Decoder',
    'SimpleConvs',
    'build_backbone',
    'load_weights'
]
__version__ = '0.1.1' 