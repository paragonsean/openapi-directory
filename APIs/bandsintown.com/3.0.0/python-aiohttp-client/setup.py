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
    description="Bandsintown API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Bandsintown API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    # What is the Bandsintown API? The Bandsintown API is designed for artists and enterprises representing artists.  It offers read-only access to artist info and artist events: - artist info: returns the link to the Bandsintown artist page, the link to the artist photo, the current number of trackers and more - artist events: returns the list of events including their date and time, venue name and location, ticket links, lineup, description and the link to the Bandsintown event page  Note you can specify if you only want to return upcoming events, past events, all events, or events within a given date range.  # Getting Started - In order to use the Bandsintown API, you must read and accept our Terms and Conditions below and you must have written consent from Bandsintown Inc. Any other use of the Bandsintown API is prohibited. [Contact Bandsintown](http://help.bandsintown.com/) to tell us what you plan to do and request your personal application ID. - Find out about the API methods available and the format of the API responses below. Select the method you wish to use and try it out online with the app ID provided to you. - Call our Bandsintown API with the app ID provided straight from your website or back-end platform and choose which element of the API response you wish to display. Scroll to the bottom of this page to find out about the Models used. 
    """
)

