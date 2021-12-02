##### Markdownipy setup #######

from setuptools import setup,find_packages
import os

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

p = os.path.join(".","src")
p = os.path.join(p,"markdownipy")
p = os.path.join(p,"markdownipy.py")
with open(p, "r", encoding="utf-8") as f:
	exec(f.readline()) # First line is version, so get it and execute it
	version = __version__  # Get the version


setup(
    name="Markdownipy",
    version=version,
    author="fbgencer",
	author_email="fbgencer8@gmail.com",
    url="https://github.com/fbgencer/markdownipy",
    description="Markdownipy, python markdown generator library",
    long_description=long_description,
	long_description_content_type="text/markdown",
	license="MIT",
	python_requires=">=3.6",
	package_dir={"": "src"},
    packages=find_packages(where="src"),
	setup_requires=[
		"setuptools>=42",
		"wheel",
	]
)
