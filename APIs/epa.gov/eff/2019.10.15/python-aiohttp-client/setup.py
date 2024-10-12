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
    description="U.S. EPA Enforcement and Compliance History Online (ECHO) - Effluent Charting and Reporting",
    author_email="",
    url="",
    keywords=["OpenAPI", "U.S. EPA Enforcement and Compliance History Online (ECHO) - Effluent Charting and Reporting"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Enforcement and Compliance History Online (ECHO) is a tool developed and maintained by EPA&#39;s Office of Enforcement and Compliance Assurance for public use.   ECHO provides integrated compliance and enforcement information for over 1 million regulated facilities nationwide.    EFF Rest Services provides the data for ECHO&#39;s Effluent Charts, a set of dynamic charts and tables of permitted effluent limits, releases, and violations over time for Clean Water Act (CWA) wastewater discharge permits issued under the National Pollutant Discharge Elimination System (NPDES).    See Effluent Charts Help (https://echo.epa.gov/help/reports/effluent-charts-help) for additional information. \\ The are 3 service end points for Effluent Charts:  get_summary_chart, get_effluent_chart, and download_effluent_chart. \\  &lt;b&gt;1)&lt;/b&gt;  Use get_summary_chart to retrieve a summary matrix of effluent parameters by effluent outfall and an overall violation status for a provided NPDES Permit and date range.  &lt;b&gt;2)&lt;/b&gt;  Use get_effluent_chart to retrieve detailed Discharge Limit, DMR and NPDES Violation information for a provided NPDES Permit, date range, effluent parameter, or outfall.  &lt;b&gt;3)&lt;/b&gt;  Use download_effluent_chart to generate a Comma Separated Value (CSV) file of the detailed data provided with get_effluent chart, for a provided NPDES Permit, date range, effluent parameter, or outfall. \\ Additional ECHO Resources:   &lt;a href&#x3D;\&quot;https://echo.epa.gov/tools/web-services\&quot;&gt;Web Services&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://echo.epa.gov/resources/echo-data/about-the-data\&quot;&gt;About ECHO&#39;s Data&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://echo.epa.gov/tools/data-downloads\&quot;&gt;Data Downloads&lt;/a&gt;  
    """
)

