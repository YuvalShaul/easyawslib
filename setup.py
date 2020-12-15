import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-yuval-shaul",
    version="0.0.1",
    author="Yuval Shaul",
    author_email="yuval.shaul@gmail.com",
    description="Classes to make your aws code easier.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YuvalShaul/easyawslib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)