import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="filecrypt",
    version="1.0.0",
    author="Tami",
    author_email="tammyshead@tuta.io",
    description="Wrapper for FileCrypt.cc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TA40/FileCryptcc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)