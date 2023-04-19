# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.

# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import find_packages, setup

__author__ = "Sam Powers"
__copyright__ = "2023, Meta"


setup(
    name="rlbench_continual",
    author="Sam Powers",
    author_email="snpowers@cs.cmu.edu",
    version="0.0.0",
    packages=find_packages(),
    install_requires=[
        "open3d<=0.16",  # Until https://github.com/isl-org/Open3D/issues/6009 is fixed
        "cchardet",
        "chardet",
    ],
)
