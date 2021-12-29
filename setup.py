import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
    PROJECT_NAME = "PyTron"
    USER_NAME= "Randrita"

setuptools.setup(
    name=f"{PROJECT_NAME}-{USER_NAME}",
    version="0.0.2",
    author=USER_NAME,
    author_email="randritas@gmail.com",
    description="Small implementation of perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Randrita/PyTron",
    project_urls={
        "Bug Tracker": "https://github.com/Randrita/PyTron/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "tqdm"
    ]
)