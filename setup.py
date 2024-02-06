from setuptools import setup, find_packages

# Configure the package setup for the Python project.
setup(
    name='progeny-genialis-assignment', # The name of the distribution package.
    version='1.0.0', # The current version of the package.
    packages=find_packages(), # Automatically find and include all packages in the package directory.
    install_requires=[
        'resdk', # Resolwe SDK for Python, required for data analysis on the Genialis platform.
        'decoupler', # A library for decoupling analysis of biological networks, used for calculating PROGENy scores.
        'omnipath' # A library for comprehensive pathway information, required for PROGENy scores.
    ],
    entry_points={
        'console_scripts': [
            'progeny=progeny.cli:main', # Defines a console script "progeny" that calls the main function in the progeny.cli module.
        ],
    },
)
