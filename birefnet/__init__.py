"""
BIREFNET: Bilateral Reference for High-Resolution Dichotomous Image Segmentation

This package provides a complete implementation of BiRefNet, including:
- Neural network models and architectures
- Configuration management
- Utility functions for training and inference
"""

# Import everything from subpackages
from birefnet.birefnet_models import *
from birefnet.birefnet_utils import *
from birefnet.birefnet_config import *

# Version information
__version__ = '0.1.1'

# Package description
__description__ = "Bilateral Reference for High-Resolution Dichotomous Image Segmentation"
__author__ = "Peng Zheng, Dehong Gao, Deng-Ping Fan, Li Liu, Jorma Laaksonen, Wanli Ouyang, Nicu Sebe"
__license__ = "Apache-2.0" 