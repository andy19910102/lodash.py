import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lodash-py",
    version="0.0.4",
    author="Huang An Sheng",
    author_email="andy19910102@gmail.com",
    description="Lodash methods in Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andy19910102/lodash.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[]
)
