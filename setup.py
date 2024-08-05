from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        '''
        what will be the problem here?
        -> \n will create a problem.
           so we replace it with just a blank space. 
        '''
        requirements= [req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup(
name='E2EMLP',
version='0.0.1',
author='Anshul Jethani',
author_email='anshuljethani777@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')



)
