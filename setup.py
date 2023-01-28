from setuptools import setup, find_packages

with open("README.rst") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="MLP",
    version="2023.01.28",
    description="Medical Language Processing",
    long_description=readme,
    author="Michael Silva",
    author_email="mike.a.silva@gmail.com",
    url="https://github.com/mikeasilva/mlp",
    license=license,
    packages=find_packages(exclude=("tests", "docs", "data")),
)
