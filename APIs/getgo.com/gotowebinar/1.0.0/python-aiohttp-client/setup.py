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
    description="GoToWebinar",
    author_email="developer-support@logmein.com",
    url="",
    keywords=["OpenAPI", "GoToWebinar"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The GoToWebinar API provides seamless integration of webinar registrant and attendee data into your existing infrastructure or third-party applications. The ability to register participants, as well as pull lists of registrants and attendees for a webinar, allows organizers to manage the flow of information between their primary applications without manual intervention.
    """
)

