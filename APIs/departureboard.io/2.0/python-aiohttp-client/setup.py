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
    description="departureboard.io API",
    author_email="",
    url="",
    keywords=["OpenAPI", "departureboard.io API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The departureboard.io is a high performance API written in Golang. Its goal is to provide to main functions:&lt;br&gt;&lt;br&gt; (1): A JSON API interface to the legacy National Rail SOAP API: Giving developers the ability to pull live information on departures, arrivals, and services from National Rail, without having to use the legacy SOAP API provided by National Rail. Information is still pulled directly from National Rail in the background, providing the same level of real-time data without the additional complexity of having to interact with SOAP. &lt;br&gt;&lt;br&gt;(2): A JSON API interface for additional National Rail information: Giving developers the ability to pull a range of information about the Rail Network, via a JSON API interface. This is not an offering that National Rail currently provide, and is custom developed. Data is sourced from periodically updated XML documents, parsed, and provided for consumption via the departureboard.io API.&lt;br&gt;&lt;br&gt;This API is completely free to use for non-commercial purposes. You can explore the various sections of the documentation using the links below.&lt;br&gt;&lt;br&gt; For more information please see &lt;a href&#x3D;\&quot;https://api.departureboard.io\&quot;&gt;https://api.departureboard.io&lt;/a&gt;
    """
)

