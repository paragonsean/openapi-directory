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
    description="Europeana Search &amp; Record API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Europeana Search &amp; Record API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This Swagger API console provides an overview of the Europeana Search &amp; Record API. You can build and test anything from the simplest search to a complex query using facetList such as dates, geotags and permissions. For more help and information, head to our comprehensive &lt;a href&#x3D;\&quot;https://pro.europeana.eu/page/intro\&quot;&gt;online documentation&lt;/a&gt;.
    """
)

