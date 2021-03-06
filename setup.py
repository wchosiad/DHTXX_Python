from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="dhtxx",
    version="0.1.1",
    author="Bill Chosiad (forked from Zoltán Szarvas)",
    author_email="",
    description="Pure Python library for reading DHT11 or DHT22 sensors on Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wchosiad/DHT11_Python",
    packages=setuptools.find_packages(),
    install_requires=["RPi.GPIO"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
