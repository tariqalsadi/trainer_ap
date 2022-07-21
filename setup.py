from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in trainer_app/__init__.py
from trainer_app import __version__ as version

setup(
	name="trainer_app",
	version=version,
	description="desc",
	author="pu",
	author_email="m@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
