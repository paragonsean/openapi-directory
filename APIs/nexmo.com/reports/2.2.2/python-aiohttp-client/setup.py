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
    description="Reports API",
    author_email="devrel@vonage.com",
    url="",
    keywords=["OpenAPI", "Reports API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The [Reports API](/reports/overview) enables you to request a report of activity for your Vonage account.  Depending on your query pattern, you can choose from one of the two versions of the Reports API: asynchronous and synchronous. The asynchronous version is optimized for infrequent and large data queries (from several records to tens of millions). The synchronous version is optimized for frequent and periodic retrievals of small batches of data records (from one record to tens of thousand per query).  Only synchronous version supports retrival of data records by message/record ID.  Vonage recommends that you limit asynchronous queries to a maximum of 20 million records, by setting the start and end dates accordingly. On average, the asynchronous Reports API takes 5 - 10 minutes to generate 1 million records. 
    """
)

