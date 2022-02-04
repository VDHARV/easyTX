import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="data_xchg",
    version="1.5",
    description="Module to exchange data in any form (video or string) from one PC to another.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/VDHARV/data_xchg",
    author="VDHARV",
    author_email="vdharv4bharat.@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["data_xchg"],
    include_package_data=True,
    install_requires=["opencv-python", "numpy"],
)