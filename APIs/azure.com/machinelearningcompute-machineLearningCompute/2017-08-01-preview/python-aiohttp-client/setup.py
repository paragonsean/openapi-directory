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
    description="Machine Learning Compute Management Client",
    author_email="",
    url="",
    keywords=["OpenAPI", "Machine Learning Compute Management Client"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    These APIs allow end users to operate on Azure Machine Learning Compute resources. They support the following operations:&lt;ul&gt;&lt;li&gt;Create or update a cluster&lt;/li&gt;&lt;li&gt;Get a cluster&lt;/li&gt;&lt;li&gt;Patch a cluster&lt;/li&gt;&lt;li&gt;Delete a cluster&lt;/li&gt;&lt;li&gt;Get keys for a cluster&lt;/li&gt;&lt;li&gt;Check if updates are available for system services in a cluster&lt;/li&gt;&lt;li&gt;Update system services in a cluster&lt;/li&gt;&lt;li&gt;Get all clusters in a resource group&lt;/li&gt;&lt;li&gt;Get all clusters in a subscription&lt;/li&gt;&lt;/ul&gt;
    """
)

