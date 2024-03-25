from setuptools import find_packages, setup
from typing import List


def get_reguirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        return requirements

setup(
    name="Diamond Price Prediction",
    version="0.0.1",
    author="Hasnain Narsandawala",
    author_email="hasnain.narsandawala@gmail.com",
    install_requires =get_reguirements('requirements.txt'),
    package = find_packages(),
)