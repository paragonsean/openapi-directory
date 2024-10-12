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
    description="Data2CRM.API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Data2CRM.API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Make use of our in-depth documentation to get more information about the various functions of the service. Those willing to explore the mechanics of Data2CRM.API can test it in live regime using the short code samples.&lt;/p&gt;&lt;p&gt;Select CRM: &lt;span id&#x3D;\&quot;docs-select-crm\&quot; style&#x3D;\&quot;font-weight: bold\&quot;&gt;Loading... please wait&lt;/span&gt;&lt;/p&gt;&lt;p&gt;Here are the API access keys:&lt;br&gt;&lt;b&gt;X-API2CRM-USER-KEY&lt;/b&gt;: &lt;span id&#x3D;\&quot;docs-user-key\&quot;&gt;e2a6379ab878ae7e58119d4ec842bf9c&lt;/span&gt;&lt;br&gt;&lt;b&gt;X-API2CRM-APPLICATION-KEY&lt;/b&gt;: &lt;span id&#x3D;\&quot;docs-crm-key\&quot;&gt;7ae5b17008fb414d84981191cf3b66a476ef8bef&lt;/span&gt;&lt;/p&gt;&lt;p id&#x3D;\&quot;docs-crm-access\&quot;&gt;The CRM access details are:&lt;br&gt;&lt;b&gt;URL&lt;/b&gt;: &lt;a id&#x3D;\&quot;docs-crm-url\&quot; href&#x3D;\&quot;https://login.salesforce.com/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;https://login.salesforce.com/&lt;/a&gt;&lt;br&gt;&lt;b&gt;E-mail / Username&lt;/b&gt;: &lt;span id&#x3D;\&quot;docs-crm-username\&quot;&gt;developers.data2crm.api+1@magneticone.com&lt;/span&gt;&lt;br&gt;&lt;b&gt;Password&lt;/b&gt;: &lt;span id&#x3D;\&quot;docs-crm-password\&quot;&gt;data2crmapi123&lt;/span&gt;&lt;/p&gt;
    """
)

