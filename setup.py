#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="dummypackage",
    version="0.0.1",
    description="PyTorch Lightning Project Setup",
    author="",
    author_email="",
    url="https://github.com/Shreyans92/ELMO_session_4",
    install_requires=["lightning", "hydra-core"],
    packages=find_packages(),
    # use this to customize global commands available in the terminal after installing the package
    entry_points={
        "console_scripts": [
            "dummy_train = dummypackage.train:main",
            "dummy_eval = dummypackage.eval:main",
        ]
    },
)