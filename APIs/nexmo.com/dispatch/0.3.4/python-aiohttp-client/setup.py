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
    description="Dispatch API",
    author_email="devrel@vonage.com",
    url="",
    keywords=["OpenAPI", "Dispatch API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Dispatch API enables the developer to specify a multiple message workflow. A workflow follows a template. The first one we are adding is the failover template. The failover template instructs the Messages API to first send a message to the specified channel. If that message fails immediately or if the condition_status is not reached within the given time period the next message is sent. The developer will also receive status webhooks from the messages resource for each delivery and read event. This API is currently in Beta.
    """
)

