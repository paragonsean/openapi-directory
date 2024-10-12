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
    description="brainbi",
    author_email="",
    url="",
    keywords=["OpenAPI", "brainbi"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Welcome to the official API of the brainbi platform. Using this API you can freely integrate our analytics platform with any other solution.  Please refer to the following documentation and in case of any issues, please contact us at service@brainbi.net.  Please note: for this API you will use your email and password from the brainbi.net platform to gather a Bearer Token for any API calls (use Login and get token). Once you are finished with your calls, please do a logout to remove your token and keep your account safe (use logout).
    """
)

