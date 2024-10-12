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
    description="U.S. EPA Enforcement and Compliance History Online (ECHO) - Detailed Facility Report (DFR)",
    author_email="",
    url="",
    keywords=["OpenAPI", "U.S. EPA Enforcement and Compliance History Online (ECHO) - Detailed Facility Report (DFR)"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Enforcement and Compliance History Online (ECHO) is a tool developed and maintained by EPA&#39;s Office of Enforcement and Compliance Assurance for public use. ECHO provides integrated compliance and enforcement information for over 1 million regulated facilities nationwide.  DFR Rest Services provide multiple service endpoints, to retrieve detailed facility location, enforcement, compliance monitoring, and pollutant information for any single facility.  See the Detailed Facility Report (DFR) Help Page (https://echo.epa.gov/help/reports/detailed-facility-report-help) for additional information on the DFR.  Additionally, a Data Dictionary (https://echo.epa.gov/help/reports/dfr-data-dictionary) is also available.  There is one primary service end point, get_dfr, that provides all available DFR data.  All other service end points that are exposed, will return data on a single section of the DFR.     \\ Additional ECHO Resources:   &lt;a href&#x3D;\&quot;https://echo.epa.gov/tools/web-services\&quot;&gt;Web Services&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://echo.epa.gov/resources/echo-data/about-the-data\&quot;&gt;About ECHO&#39;s Data&lt;/a&gt;, &lt;a href&#x3D;\&quot;https://echo.epa.gov/tools/data-downloads\&quot;&gt;Data Downloads&lt;/a&gt;  
    """
)

