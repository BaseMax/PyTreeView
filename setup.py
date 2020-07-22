# pytree
# TODO
import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE/"README.md").read_text()

setup(
   name="PyTreeView", 
   version="1.0.0", 
   descp=" PyTreeView is a python class and library to display Tree (Tree View) from array, object, or JSON.", 
   long_descp=README,
   long_descp_content="text/markdown", 
   URL="https://github.com/basemax/PyTreeView", 
   author="Max Base", 
   authoremail="maxbasecode@gmail.com", 
   license="MIT",
   classifiers=[ 
        "License :: OSI Approved :: MIT License", 
        "Programming Language :: Python :: 3", 
        "Programming Language :: Python :: 3.7", 
   ], 
   packages=["PyTreeView"], 
   includepackagedata=True, 
   installrequires=[], 
   entrypoints={ 
       "console_scripts":[ 
           "realpython=pytree", #TODO 
       ] 
   }, 
 )
