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
    description="PAC Control REST API",
    author_email="developer@opto22.com",
    url="",
    keywords=["OpenAPI", "PAC Control REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    #### Revised: 6/15/2018  ### Overview This API provides secure access to a SNAP-PAC-R or -S series controller&#39;s variable and I/O tags. Confidentiality for API transactions is provided by HTTPS. Authentication uses HTTP Basic Authentication with an API key. An API key ID is submitted in the Basic Authentication userid field and API key value in the password field.  **For more information visit:** [developer.opto22.com](http://developer.opto22.com)  ### Examples  **Read an array** of all the integer32 variables defined in the PAC&#39;s strategy. For example, on your SNAP-PAC-R or -S series controller at IP address 1.2.3.4, you would use the URL:   &#x60;&#x60;&#x60; https://1.2.3.4/api/v1/device/strategy/vars/int32s &#x60;&#x60;&#x60; and provide appropriate authentication. The GET response will be a JSON array of name-value  pairs such as:  &#x60;&#x60;&#x60;json [ { \&quot;nMyVeryFavoriteNumber\&quot;: 22 },   { \&quot;nWidgetsProducedToday\&quot;: 22222 },   { \&quot;DELAY_LOOP_TIME_IN_MSECS\&quot;  : 200 } ] &#x60;&#x60;&#x60; **Read the engineering units** (EU) of an analog input point configured in the PAC&#39;s strategy. For an analog input (I/O point) named aiTemperatureInDegreesF, use   &#x60;https://1.2.3.4/api/v1/device/strategy/ios/analogInputs/aiTemperatureInDegreesF/eu&#x60;  The GET response will be a single JSON name-value pair such as: &#x60;&#x60;&#x60;json { \&quot;value\&quot;: 72.22 } &#x60;&#x60;&#x60;      ### Note on packet sizes: When doing POSTs or GETs, the JSON payload in the body should not exceed 3k (3072 bytes). 
    """
)

