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
    description="vs API",
    author_email="ab.techwriter@gmail.com",
    url="",
    keywords=["OpenAPI", "vs API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    # Introduction This API returns data regarding almost all nouns in vedic literature. The results are JSON objects that contain the word transliterated to the Roman script, the word in the Nagari script, the meaning of the word, and the category the word belongs to. Proper nouns are not included (yet).  The API uses the Swagger 2.0 specification.  # Authentication This is an open API.  # Try it out This sandbox can be used to get data for only one kind of resource, that is, to fetch data for a string contained in the meaning of any of the words.  The remaining resources work a similar fashion. For details, see the reference documentation. 
    """
)

