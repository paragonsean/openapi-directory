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
    description="BC Route Planner REST API",
    author_email="",
    url="",
    keywords=["OpenAPI", "BC Route Planner REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Finds shortest/fastest route between a start point and one or more stop points on British Columbia&#39;s public road network. The BC Route planner [webpage](https://www2.gov.bc.ca/gov/content?id&#x3D;9D99E684CCD042CD88FADC51E079B4B5) provides additional information.  Here are some geocoded addresses to play with:&lt;br&gt;18 Douglas St,Victoria -123.36962,48.40892&lt;br&gt;1002 Johnson St, Victoria -123.355745,48.426206&lt;br&gt;543 Johnson St, Victoria, BC -123.36907,48.42770 &lt;br&gt;14 Centennial Sq, Victoria, BC -123.36564,48.42863&lt;br&gt;1105 Royal Ave,New Westminster  -122.92009,49.20063&lt;br&gt;808 Jackson Cres, New Westminster -122.90762,49.22558&lt;br&gt;10810 McDonald Rd, Chilliwack -121.93808,49.19859&lt;br&gt;3950 June Springs Rd, Kelowna -119.40751,49.83960&lt;br&gt;1201 Riondel Rd, Kootenay Bay -116.85402,49.74448&lt;br&gt;1201 Riondel Rd, Kootenay Bay -116.832759,49.730500 (parcelPoint)&lt;br&gt;2499 Walbran Pl, Courtenay -124.97295,49.71518&lt;br&gt;2013 Smoke Bluff Rd, Squamish -123.13946,49.70401&lt;br&gt;235 Kelvin Grove Way, Lions Bay -123.23524,49.45035&lt;br&gt;   Please see our &lt;a href&#x3D;https://github.com/bcgov/api-specs/blob/master/COLLECTION_NOTICE.md#collection-notice target&#x3D;\&quot;_blank\&quot;&gt;data collection notice&lt;/a&gt;.   Please note that you may experience issues when submitting requests to the delivery or test environment if using this [OpenAPI specification](https://github.com/bcgov/api-specs) in other API console viewers.   [API keys](https://api.gov.bc.ca/devportal/api-directory/740) are unique and can be acquired with a GitHub or IDIR account.   
    """
)

