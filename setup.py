from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as  file_obj:
        requigitrements=file_obj.readlines()
        requirements= [req.replace("/n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements



setup(
    name="thyroid disease prediction",
    version="0.01",
    author="varnit",
    author_email="varnit2406@gmail",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()


)