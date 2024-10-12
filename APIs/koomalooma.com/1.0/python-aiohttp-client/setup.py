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
    description="koomalooma Partner API",
    author_email="support@koomalooma.com",
    url="",
    keywords=["OpenAPI", "koomalooma Partner API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This is the koomalooma Partner API. koomalooma is the first Loyalty BPaaS (Business Process as a Service) for mobile and web companies. With koomalooma merchants issue points for actions their customers / users make on your mobile or web store, for example a purchase or a referral. koomalooma takes care of all the rest, from signing up users, keeping track of points and delivering rewards in over 80 countries. koomalooma offers an easy to integrate API and web backend to configure loyalty campaigns and track performance. You can find more at http://support.koomalooma.com
    """
)

