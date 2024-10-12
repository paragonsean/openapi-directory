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
    description="Starwars Translations API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Starwars Translations API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Funtranslations Starwars API gives access to the full set of starwars language translations available at funtranslations.com so that you can integrate them in your workflow or an app. [Click here to get details and subscribe](http://funtranslations.com/api/starwars) .          You can also subscribe to individual translators. Here are the details.      Ever wonder how to talk like Yoda? Well, use our API and let your APP/webpage speak like Yoda too.[Click here to subscribe](http://funtranslations.com/api/yoda)        Sith Translator API. [Click here to subscribe](http://funtranslations.com/api/sith)       Cheunh Translator API. [Click here to subscribe](http://funtranslations.com/api/cheunh)       Huttese Translator API. [Click here to subscribe](http://funtranslations.com/api/huttese)      Mandalorian Translator API. [Click here to subscribe](http://funtranslations.com/api/mandalorian)      Gungan Translator API. [Click here to subscribe](http://funtranslations.com/api/gungan) 
    """
)

