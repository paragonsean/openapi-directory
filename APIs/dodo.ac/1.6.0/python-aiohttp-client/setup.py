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
    description="Nookipedia",
    author_email="",
    url="",
    keywords=["OpenAPI", "Nookipedia"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Nookipedia API provides endpoints for retrieving *Animal Crossing* data pulled from the [Nookipedia wiki](https://nookipedia.com/wiki/Main_Page). A couple of the key benefits of using the Nookipedia API is access to data spanning the entire *Animal Crossing* series, as well as information that is constantly updated and expanding as editors work on the wiki.&lt;br&gt;&lt;br&gt;Access to the Nookipedia API requires obtaining a key. This is so we can manage our scale and provide better support for our users. To request access to the API, please fill out [this form](https://forms.gle/wLwtXLerKhfDrRLY8).
    """
)

