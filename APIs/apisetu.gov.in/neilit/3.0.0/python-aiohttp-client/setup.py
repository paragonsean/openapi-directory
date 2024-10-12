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
    description="National Institute of Electronics and Information Technology",
    author_email="",
    url="",
    keywords=["OpenAPI", "National Institute of Electronics and Information Technology"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    NIELIT, under Ministry of Electronics &amp; IT (http://www.nielit.gov.in/) provides education and training in the area of Information, Electronics &amp; Communication Technology. Certificates issued by NIELIT are made available in students&#39; DigiLocker accounts.
    """
)

