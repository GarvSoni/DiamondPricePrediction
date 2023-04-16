from setuptools import find_packages, setup
from typing import List

Hypen_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if Hypen_E_DOT in requirements:
            requirements.remove(Hypen_E_DOT)

    return requirements




setup(name='ResgressionProject',
      version='0.0.1',
      author="Garv",
      author_email="soni.garv719@gmail.com",
      install_requires=get_requirements('requirements.txt'),
      packages=find_packages())