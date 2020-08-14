import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graph-alchemy-brianmunson", # Replace with your own username
    version="0.0.1",
    author="Brian A. Munson",
    author_email="author@example.com",
    description="Graph package coding exercise",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/brianmunson/graph-alchemy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Public License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)