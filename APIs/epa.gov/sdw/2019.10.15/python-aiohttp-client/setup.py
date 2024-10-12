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
    description="U.S. EPA Enforcement and Compliance History Online (ECHO) - Safe Drinking Water Act",
    author_email="",
    url="",
    keywords=["OpenAPI", "U.S. EPA Enforcement and Compliance History Online (ECHO) - Safe Drinking Water Act"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Enforcement and Compliance History Online (ECHO) is a tool developed and maintained by EPA&#39;s Office of Enforcement and Compliance Assurance for public use. ECHO provides integrated compliance and enforcement information for over 1 million regulated facilities nationwide.    SDW Rest Services provides multiple service endpoints, each with specific capabilities, to search and retrieve data on public water systems regulated under the Safe Drinking Water Act (SDWA).  The returned results reflect data drawn from EPA&#39;s Federal Safe Drinking Water Information System (SDWIS) database. \\ The get_systems, get_qid, and get_download end points are meant to be used together. \\ The recommended use scenario for get_systems, get_qid, and get_downoad is: \\  &lt;b&gt;1)&lt;/b&gt;  Use get_systems to validate passed query parameters, obtain summary statistics and to obtain a query_id (QID).  QIDs are time sensitive and will be valid for approximately 30 minutes.  &lt;b&gt;2)&lt;/b&gt;  Use get_qid, with the returned QID, to paginate through arrays of water system results.  &lt;b&gt;3)&lt;/b&gt;  Use get_download, with the returned QID, to generate a Comma Separated Value (CSV) file of water system information that meets the QID query criteria. \\ \\ Use the qcolumns parameter to customize your search results.  Use the Metadata service endpoint for a list of available output objects, their Column Ids, and their definitions to help you build your customized output.  \\ Additional ECHO Resources:   &lt;a href&#x3D;\&quot;https://echo.epa.gov/tools/web-services\&quot;&gt;Web Services&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://echo.epa.gov/resources/echo-data/about-the-data\&quot;&gt;About ECHO&#39;s Data&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://echo.epa.gov/tools/data-downloads\&quot;&gt;Data Downloads&lt;/a&gt;  
    """
)

