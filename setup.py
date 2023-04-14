from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requriments
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='ml-project',
version='0.01',
author='Manohar',
author_email='manoharkmr70@gamil.com',
packages=find_packages(),
#install_requires=['pandas','numpy','seaborn']
install_requires=get_requirements('requirements.txt')

)