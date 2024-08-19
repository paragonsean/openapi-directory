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
    description="Jokes One API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Jokes One API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
     Jokes One API offers a complete feature rich REST API access to its jokes platform.  This is the documentation for the world famous [jokes API](https://jokes.one/api/joke/).  If you are a subscriber and you are trying this from a console add &#39;X-JokesOne-Api-Secret&#39; header and add your api key as the header value. You can test and play with the API right here on this web page. For using the private end points and subscribing to the API please visit https://jokes.one/api/joke/.
    """
)

