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
    description="Cisco PSIRT openVuln API",
    author_email="os@cisco.com",
    url="",
    keywords=["OpenAPI", "Cisco PSIRT openVuln API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Cisco Product Security Incident Response Team (PSIRT) openVuln API is a RESTful API that allows customers to obtain Cisco Security Vulnerability information in different machine-consumable formats. APIs are important for customers because they allow their technical staff and programmers to build tools that help them do their job more effectively (in this case, to keep up with security vulnerability information). For more information about the Cisco PSIRT openVuln API visit https://developer.cisco.com/site/PSIRT/discover/overview  For detail steps on how to use the API go to:https://developer.cisco.com/site/PSIRT/get-started/getting-started.gsp  This is a beta release of a swagger YAML for the Cisco PSIRT openVuln API  To access the API sign in with your Cisco CCO account at http://apiconsole.cisco.com and register an application to recieve a client_id and a client_secret  You can then get your token using curl or any other method you prefer.  &#39;curl -s -k -H \&quot;Content-Type: application/x-www-form-urlencoded\&quot; -X POST -d \&quot;client_id&#x3D;&lt;your_client_id&gt;\&quot; -d \&quot;client_secret&#x3D;&lt;your_client_secret&gt;\&quot; -d \&quot;grant_type&#x3D;client_credentials\&quot; https://cloudsso.cisco.com/as/token.oauth2&#39;  You will receive an access token as demonstrated in the following example:  &#39;{\&quot;access_token\&quot;:\&quot;I7omWtBDAieSiUX3shOxNJfuy4J6\&quot;,\&quot;token_type\&quot;:\&quot;Bearer\&quot;,\&quot;expires_in\&quot;:3599}&#39;  In Swagger, click on Change Authentication  enter the text \&quot;I7omWtBDAieSiUX3shOxNJfuy4J6\&quot; (which is the token you received)  then click on \&quot;Try this operation\&quot; 
    """
)

