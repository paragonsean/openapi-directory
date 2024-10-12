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
    description="GoToTraining",
    author_email="developer-support@logmein.com",
    url="",
    keywords=["OpenAPI", "GoToTraining"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The GoToTraining API enables developers to use the stable and robust GoToTraining functionality as the basis for online trainings in a proprietary learning management system. The GoToTraining APIs provide the ability to access the scheduling, registration, management, and reporting functions of GoToTraining from external applications. With the ability to tightly integrate GoToTraining into your learning infrastructure, you can offer your learners a seamless user experience and provide them with a market leading virtual classroom environment.
    """
)

