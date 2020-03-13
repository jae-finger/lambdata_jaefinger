# setup.py file
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_jaefinger",
    version="2.0",
    author="JAE Finger",
    author_email="jaefinger@gmail.com",
    description="LS DS Unit 3 Assignment 1-1",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/jae-finger/lambdata-jae-finger",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)