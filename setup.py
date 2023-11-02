from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
  '''
  This returns the list of the required libraries
  '''
  requirements=[]
  with open(file_path) as file:
    requirements=file.readlines()
    requirements=[libraries.replace("\n","") for libraries in requirements]

    if HYPEN_E_DOT in requirements:
      requirements.remove(HYPEN_E_DOT)
  return requirements

  

setup(

  name='sleepdocker',
  version='0.0.1',
  author='Sarath',
  author_email='sarathkumards07@gmail.com',
  packages=find_packages(),
  install_requires= get_requirements('requirements.txt')
)