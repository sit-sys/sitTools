# coding: utf-8
import pathlib
from setuptools import setup, find_packages

def read_requirements(file):
    with open(file) as f:
        return f.read().splitlines()
    
def read_file(file):
    with open(file) as f:
        return f.read()

HOME = pathlib.Path(__file__).parent.resolve()

PACKAGE_NAME = "sitTools"
AUTHOR = "Andy Yang"
AUTHOR_EMAIL = "andy.yang@twsit.com"
URL = "https://github.com/sit-sys/cTools"
DOWNLOAD_URL = "https://pypi.org/project/cTools/"

LICENSE = "MIT"
VERSION = read_file("VERSION")
DESCRIPTION = "Useful tools for S.I.T. project use"
LONG_DESCRIPTION = (HOME / "docs" / "README.md").read_text(encoding="utf8")
LONG_DESC_TYPE = "text/markdown"

requirements = (HOME / "requirements.txt").read_text(encoding="utf8")
INSTALL_REQUIRES = [s.strip() for s in requirements.split("\n")]

dev_requirements = (HOME / "dev_requirements.txt").read_text(encoding="utf8")
EXTRAS_REQUIRE = {"dev": [s.strip() for s in dev_requirements.split("\n")]}

CLASSIFIERS = [f"Programming Language :: Python :: 3.{str(v)}" for v in range(7, 12)]
PYTHON_REQUIRES = ">=3.8"

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    license=LICENSE,
    author_email=AUTHOR_EMAIL,
    url=URL,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    packages=find_packages(),
    classifiers=CLASSIFIERS,
)

