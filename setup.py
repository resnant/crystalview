from setuptools import setup, find_packages

setup(
    name='crystalview',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'nglview',
        'pymatgen',
        'numpy',
    ],
)
