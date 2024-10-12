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
    description="SIGNL4 API",
    author_email="",
    url="",
    keywords=["OpenAPI", "SIGNL4 API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Use our API for systems integration or to build your own use cases. Sample scenarios include but are not limited to:&lt;/p&gt;&lt;ul&gt;&lt;li&gt;2-way integration: Triggering of Signls and updates in the third party systems when alert state changes occur&lt;/li&gt;&lt;li&gt;Retrieving alarms for logging purposes&lt;/li&gt;&lt;li&gt;Calendar integrations: Creation and management of on-call duties&lt;/li&gt;&lt;li&gt;Punch users in and out based on external calendars&lt;/li&gt;&lt;li&gt;etc.&lt;/li&gt;&lt;/ul&gt;&lt;p&gt;AUTHENTICATION&lt;br&gt;Using the API requires an API key, which you can generate in the SIGNL4 portal under &#39;Developers&#39;.&lt;br&gt;This key must then be specified in a special header in every HTTP request.&lt;br&gt;This header is called &lt;b style&#x3D;&#39;color:#F8B41F&#39;&gt;X-S4-Api-Key&lt;/b&gt;.&lt;br&gt;&lt;br&gt;The base URL of the API is &lt;a rel&#x3D;&#39;noopener noreferrer&#39; target&#x3D;&#39;_blank&#39; href&#x3D;&#39;https://connect.signl4.com/api/&#39;&gt;https://connect.signl4.com/api/&lt;/a&gt;.&lt;br&gt;Copyright © Derdack GmbH&lt;br&gt;&lt;/p&gt;
    """
)

