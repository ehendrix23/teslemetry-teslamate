#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Define publication options."""

# Note: To use the 'upload' functionality of this file, you must:
#   $ pip install twine

import io
import os
from shutil import rmtree
import sys

from setuptools import Command, find_packages, setup  # type: ignore

# Package meta-data.
NAME = "teslemetry-teslamate"
DESCRIPTION = (
    ""Sync Teslamate from Teslemetry"
)
URL = "https://github.com/ehendrix23/teslemetry-teslamate"
EMAIL = "hendrix_erik@hotmail.com"
AUTHOR = "Erik Hendrix"
REQUIRES_PYTHON = ">=3.8"
VERSION = None

# What packages are required for this module to be executed?
REQUIRED = []

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for
# that!

HERE = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.rst' is present in your MANIFEST.in file!
with io.open(os.path.join(HERE, "README.rst"), encoding="utf-8") as f:
    LONG_DESC = "\n" + f.read()

# Load the package's __version__.py module as a dictionary.
ABOUT = {}  # type: ignore
if not VERSION:
    with open(os.path.join(HERE, NAME, "__version__.py")) as f:
        exec(f.read(), ABOUT)  # pylint: disable=exec-used
else:
    ABOUT["__version__"] = VERSION

if len(REQUIRED) == 0 and os.path.isfile(os.path.join(HERE, "requirements.txt")):
  requirements = os.path.join(HERE, "requirements.txt").read_text().splitlines().strip()
  for requirement in requirements:
    if requirement[0] == "-":
      continue
    requirement = requirement.split('=')[0]
    requirement = requirement.split('>')[0]
    requirement = requirement.split('<')[0]
    REQUIRED.append(requirement)

class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []  # type: ignore

    @staticmethod
    def status(string):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(string))

    def initialize_options(self):
        """Add options for initialization."""
        pass

    def finalize_options(self):
        """Add options for finalization."""
        pass

    def run(self):
        """Run."""
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(HERE, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPi via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(ABOUT["__version__"]))
        os.system("git push --tags")

        sys.exit()


# Where the magic happens:
setup(
    name=NAME,
    version=ABOUT["__version__"],
    description=DESCRIPTION,
    long_description=LONG_DESC,
    long_description_content_type="text/x-rst",
    author=AUTHOR,
    # author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['aioharmony'],
    entry_points={
        "console_scripts": ["aioharmony=aioharmony.__main__:main"],
    },
    install_requires=REQUIRED,
    include_package_data=True,
    license="Apache License 2.0",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Framework :: AsyncIO",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    # $ setup.py publish support.
    cmdclass={
        "upload": UploadCommand,
    },
)
