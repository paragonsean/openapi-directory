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
    description="Semantic API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Semantic API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Semantic API complements the Articles API. With the Semantic API, you get access to the long list of people, places, organizations and other locations, entities and descriptors that make up the controlled vocabulary used as metadata by The New York Times (sometimes referred to as Times Tags and used for Times Topics pages).  The Semantic API uses concepts which are, by definition, terms in The New York Times controlled vocabulary. Like the way facets are used in the Articles API, concepts are a good way to uncover articles of interest in The New York Times archive, and at the same time, limit the scope and number of those articles. The Semantic API maps to external semantic data resources, in a fashion consistent with the idea of linked data. The Semantic API also provides combination and relationship information to other, similar concepts in The New York Times controlled vocabulary. 
    """
)

