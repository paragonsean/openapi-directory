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
    description="WeGA API",
    author_email="",
    url="",
    keywords=["OpenAPI", "WeGA API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    ⚠️&lt;b&gt;DEPRECATION WARNING&lt;/b&gt;⚠️&lt;br/&gt;This version of the WeGA API specification is outdated and superseded by [version 1.1.0](https://weber-gesamtausgabe.de/api/v1/openapi.json).  &lt;br/&gt; &lt;br/&gt; For feedback or requests about this API please contact stadler@weber-gesamtausgabe.de or start the discussion at https://github.com/Edirom/WeGA-WebApp
    """
)

