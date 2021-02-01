#!/usr/bin/env python
from setuptools import setup, find_packages

DISTNAME = 'clus-wasser'
DESCRIPTION = 'Clustering based on the Wasserstein distance, k-nearest neighbours and a union find algorithm'
MAINTAINER = 'Johannes Preisinger'
URL = 'https://github.com/barblin/clusterization-service'

classifiers = ['Programming Language :: Python :: 3.1']

if __name__ == "__main__":
    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          description=DESCRIPTION,
          packages=find_packages(exclude=[
              "tests"
          ]),
          url=URL,
          classifiers=classifiers,
          install_requires=[
              "numpy",
              "scipy",
              "sklearn"
          ])
