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
    description="Carbone API",
    author_email="support@carbone.io",
    url="",
    keywords=["OpenAPI", "Carbone API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Carbone Cloud/On-premise Open API reference.  For requesting: - Carbone Cloud API: find your API key on your [Carbone account](https://account.carbone.io). Home page &gt; Copy the &#x60;production&#x60; or &#x60;testing&#x60; API key. - Carbone On-premise: Update the &#x60;Server URL&#x60; on the Open API specification.  Useful links: - [API Flow](https://carbone.io/api-reference.html#quickstart-api-flow) - [Integration / SDKs](https://carbone.io/api-reference.html#api-integration) - [Generated document storage](https://carbone.io/api-reference.html#report-storage) - [Request timeout](https://carbone.io/api-reference.html#api-timeout)
    """
)

