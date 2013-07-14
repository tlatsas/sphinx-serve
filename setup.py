from setuptools import setup 
import sphinx_serve

setup(
    name="sphinx-serve",
    version=sphinx_serve.__version__,
    description=sphinx_serve.__doc__.strip(),
    long_description="",
    url="https://github.com/tlatsas/sphinx-serve",
    author="Tasos Latsas",
    author_email="tlatsas@gmx.com",
    license="MIT",
    packages=["sphinx_serve"],
    entry_points = {
        "console_scripts": [
            "sphinx-serve = sphinx_serve.__main__:main",
        ],
    },
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Topic :: Documentation",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License"
    ],
)
