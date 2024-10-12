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
    description="DigitalNZ API",
    author_email="develop@digitalnz.org",
    url="",
    keywords=["OpenAPI", "DigitalNZ API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    OpenAPI specification of DigitalNZ&#39;s Record API.   For more information about the API see [digitalnz.org/developers](https://digitalnz.org/developers).   To learn more about the metadata/fields used in the API see the [Metadata Dictionary](https://docs.google.com/document/pub?id&#x3D;1Z3I_ckQWjnQQ4SzpORbClcIXUheO-Jd4jt-oZFuMcoQ).   To get a sense of what content is available via the API take a look at the search feature on the [DigitalNZ website](https://digitalnz.org/records?text&#x3D;all%20sorts&amp;tab&#x3D;Images).   The [terms of use](https://digitalnz.org/about/terms-of-use/developer-api-terms-of-use) specify how developers can use the DigitalNZ API. 
    """
)

