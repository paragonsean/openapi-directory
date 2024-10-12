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
    description="FunTranslations API",
    author_email="",
    url="",
    keywords=["OpenAPI", "FunTranslations API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Funtranslations API gives access to the full set of translations available at funtranslations.com so that you can integrate them in your workflow or an app. [Click here to get details and subscribe](http://funtranslations.com/api) . Here are the individual API links:    ## Morse code API ##   Morse code conversion API on the cloud. Translate to and from Morse Code.[Click here to subscribe](http://funtranslations.com/api/morse)   ## Braille API ##   Braille conversion API on the cloud. Translate to Braille and get Braille results suitable for many display types.[Click here to subscribe](http://funtranslations.com/api/braille)        ## Starwars Translation API ##   Ever wonder how to talk like Yoda? Well, use our API and let your APP/webpage speak like Yoda too.[Click here to subscribe](http://funtranslations.com/api/yoda)        Sith Translator API. [Click here to subscribe](http://funtranslations.com/api/sith)       Cheunh Translator API. [Click here to subscribe](http://funtranslations.com/api/cheunh)       Huttese Translator API. [Click here to subscribe](http://funtranslations.com/api/huttese)      Mandalorian Translator API. [Click here to subscribe](http://funtranslations.com/api/mandalorian)      Gungan Translator API. [Click here to subscribe](http://funtranslations.com/api/gungan)      ## Pirate Speak Translation API ##   Ahoy, matey. Let&#39;s get those land lubbers speak our tounge too! Our evergreen pirate speak tranlsator API.[Click here to subscribe](http://funtranslations.com/api/pirate)    ## Valley Speak Translation API ##   Our throwback Valspeak translations API.[Click here to subscribe](http://funtranslations.com/api/valspeak)       ## Minion Speak Translation API ##   Our evil master following minion speak translations API.[Click here to subscribe](http://funtranslations.com/api/minion)      
    """
)

