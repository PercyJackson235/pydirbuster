#!/usr/bin/python3
import setuptools

def reader(filename:str, lister:bool):
    text = ''
    with open(filename) as f:
        text = f.read()
        if lister:
            text = text.splitlines()
        return text

setuptools.setup(name="pybuster-PercyJackson235",
                 version="0.4",
                 author="Zachary Farquharson",
                 author_email="PercyJackson235@gmail.com",
                 description="Python Web Directory and File Brute Forcer",
                 long_description=reader('README.md', False),
                 long_description_content_type="text/markdown",
                 url="https://github.com/PercyJackson235/pybuster",
                 packages=setuptools.find_packages(),
                 classifiers=["Development Status :: 4 - Beta",
                              "Intended Audience :: Developers",
                              "Intended Audience :: Education",
                              "Intended Audience :: End Users/Desktop",
                              "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                              "Operating System :: OS Independent",
                              "Programming Language :: Python :: 3"],
                 python_requires=">=3",
                 install_requires=reader('requirements.txt', True),
                 scripts=['pybuster/pybuster'])