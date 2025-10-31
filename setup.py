# ...existing code...
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    Return list of requirements from file, ignoring editable marker '-e .'
    """
    requirements: List[str] = []
    with open(file_path) as file:
        requirements = [req.strip() for req in file.readlines() if req.strip()]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="MLProjectS",
    version="0.0.1",
    author="Anusha",
    description="Please, I hope I will complete this crash course",
    author_email="anushayaramala31@hgmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
# ...existing code...