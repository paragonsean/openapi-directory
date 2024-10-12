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
    description="VA Facilities",
    author_email="",
    url="",
    keywords=["OpenAPI", "VA Facilities"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    ## Background  The VA Facilities API version 0 (v0) provides information about VA facilities, including locations, addresses, phone numbers, hours of operation, and available services.  This API gives information about several types of VA facilities: - Health facilities (vha) - Benefits facilities (vba) - Cemeteries (nca) - Vet Centers (vc)  ## Technical overview  For in-depth details on data sources for the Facilities API, [read our Facilities GitHub documentation](https://github.com/department-of-veterans-affairs/lighthouse-facilities#readme).  Health service and service availability data for v0 of this API are based on historical data.  - Historical data is returned for the previous 30 days. - Data is based on both pending and completed appointments for a service at a given facility.   ### Authentication and Authorization  VA Facilities is an open data API. Open data API requests are authorized through a symmetric API token that&#39;s provided in an HTTP header with the name &#39;apikey&#39;.  ### Test data  Test data for the sandbox environment is only for testing the API and is not guaranteed to be up-to-date. After testing this API in sandbox, you can start the process of moving to production.  ### Facility ID formats  A facility ID has the format prefix_stationNumber. The prefix is nca, vc, vba, or vha. Cemeteries may be VA national cemeteries or non-national; non-national cemeteries have the station number prefixed with an s. There are no other constraints on the format. Some facility ID examples are: - Health: &#x60;vha_402GA&#x60; - Benefits: &#x60;vba_539GB&#x60; - National cemetery: &#x60;nca_063&#x60; - Non-national cemetery: &#x60;nca_s1082&#x60; - Vet Center: &#x60;vc_0872MVC&#x60;   ### Mobile facilities  The mobile health facilities move regularly within a region. If a facility comes back from this API with \&quot;mobile\&quot;: \&quot;true\&quot;, the latitude/longitude and address could be inaccurate. To get the exact current location, please call the mobile facility number listed.
    """
)

