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
    description="U.S. EPA Enforcement and Compliance History Online (ECHO) - Enforcement Case Search",
    author_email="",
    url="",
    keywords=["OpenAPI", "U.S. EPA Enforcement and Compliance History Online (ECHO) - Enforcement Case Search"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Enforcement and Compliance History Online (ECHO) is a tool developed and maintained by EPA&#39;s Office of Enforcement and Compliance Assurance for public use. ECHO provides integrated compliance and enforcement information for over 1 million regulated facilities nationwide.  CASE Rest Services provide multiple service endpoints, each with specific capabilities, to search and retrieve data on civil cases entered into the  Integrated Compliance Information System (ICIS) and criminal cases entered into the Summary of Criminal Prosecutions database.   See Enforcement Case Search Help (https://echo.epa.gov/help/enforcement-case-search-help) for additional information on searching civil and criminal cases.  \\ The get_cases, get_map, get_qid, and get_download end points are meant to be used together, while the enhanced get_case_info end point is self contained..    The recommended use scenario for get_cases, get_qid, get_map, and get_downoad is: \\  &lt;b&gt;1)&lt;/b&gt;  Use get_cases to validate passed query parameters, obtain summary statistics and to obtain a query_id (QID).  QIDs are time sensitive and will be valid for approximately 30 minutes.  &lt;b&gt;2)&lt;/b&gt;  Use get_qid, with the returned QID, to paginate through arrays of case results.  &lt;b&gt;3)&lt;/b&gt;  Use get_map, with the returned QID, to zoom in/out and pan on the clustered and individual facility coordinates, related to the returned cases, that meet the QID query criteria.  &lt;b&gt;4)&lt;/b&gt;  Use get_download, with the returned QID, to generate a Comma Separated Value (CSV) file of facility information that meets the QID query criteria. \\ In addition to the service endpoints listed above there are two detailed case report services, one for civil cases (get_case_report) and one for criminal cases (get_crcase_report).  See the Civil Enforcement Case Report Help (https://echo.epa.gov/help/reports/enforcement-case-report-help) and the Criminal Case Report Help (https://echo.epa.gov/help/reports/criminal-case-report-help) for additional information  on then data returned from these two services.    \\ Additional ECHO Resources:   &lt;a href&#x3D;\&quot;https://echo.epa.gov/tools/web-services\&quot;&gt;Web Services&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://echo.epa.gov/resources/echo-data/about-the-data\&quot;&gt;About ECHO&#39;s Data&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://echo.epa.gov/tools/data-downloads\&quot;&gt;Data Downloads&lt;/a&gt;  
    """
)

