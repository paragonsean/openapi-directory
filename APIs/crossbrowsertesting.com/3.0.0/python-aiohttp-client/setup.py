# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="Crossbrowsertesting.com Screenshot Comparisons API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Crossbrowsertesting.com Screenshot Comparisons API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    What&#39;s in this version:   1. Compare two screenshots for layout differences   2. Compare a full screenshot test of browsers to a single baseline browser for layout differences.   3. Compare a screenshot test version to another test version - good for regression tests.   4. Get links to the Comparison UI for visual representation of layout differences
    """
)

