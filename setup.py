import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfilter-rbs",
    version="0.0.1",
    author="RBS106",
    author_email="no@u.sus",
    description="Package to filt some text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rbs106/pyfilter",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
