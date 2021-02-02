#!/usr/bin/env python
from setuptools import setup, find_packages

DISTNAME = 'cluster-wasser'
DESCRIPTION = 'Clustering based on the Wasserstein distance, k-nearest neighbours and a union find algorithm'
MAINTAINER = 'Johannes Preisinger'
URL = 'https://github.com/barblin/clus-wasser'

classifiers = ['Programming Language :: Python :: 3.1']

if __name__ == "__main__":
    setup(name=DISTNAME,
          maintainer=MAINTAINER,
          author=MAINTAINER,
          description=DESCRIPTION,
          version="1.0.0",
          license="MIT",
          packages=find_packages(exclude=[
              "tests",
              "assets"
          ], ),
          url=URL,
          classifiers=classifiers,
          python_requires='>=3.8',
          install_requires=[
              "numpy",
              "scipy",
              "sklearn"
          ])
