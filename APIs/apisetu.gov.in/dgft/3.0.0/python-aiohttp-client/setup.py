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
    description="Importer-Exporter Details API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Importer-Exporter Details API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Importer-Exporter Code (IEC), issued by Directorate General of Foreign Trade (DGFT), is a key business identification number which is mandatory for Exports or Imports. This API can be used to get details of a importer-exporter by importer-exporter code.
    """
)

