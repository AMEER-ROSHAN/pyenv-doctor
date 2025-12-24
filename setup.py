from setuptools import setup, find_packages

setup(
    name="pyenv-doctor",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pydoctor=pydoctor.cli:main",
        ]
    },
)
