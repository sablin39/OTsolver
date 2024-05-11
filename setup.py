from setuptools import setup,find_packages,extension
import os


setup(
    name="otmodule",
    version="0.0.1",
    
    packages=["robot"],
    install_requires=[
        # Parse requirements from requirements.txt file
        requirement.strip()
        for requirement in open(os.path.join(os.path.dirname(os.path.abspath(__file__)))+'/robot/requirements.txt').readlines()
    ]+["pointnet2@file://"+os.path.join(os.path.dirname(os.path.abspath(__file__)))+"/pointnet2/lib"],
    # scripts=[os.path.join(os.path.dirname(os.path.abspath(__file__)))+"/pointnet2/lib/setup.py"]
)
