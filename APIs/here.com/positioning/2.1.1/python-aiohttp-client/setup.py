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
    description="HERE Network Positioning API v2",
    author_email="",
    url="",
    keywords=["OpenAPI", "HERE Network Positioning API v2"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Positioning API accepts requests with radio network measurements and replies with corresponding location estimate. For more details and examples, see [Developer&#39;s Guide](https://developer.here.com/documentation/positioning). Cellular measurements are given in terms defined in 3GPP and 3GGP2 specifications, see the corresponsing documentation at http://www.3gpp.org.  Breaking changes from v1:   - JSON fields     &#x60;altaccuracy&#x60;, &#x60;baselat&#x60;, &#x60;baselng&#x60;, &#x60;cellparams&#x60;, &#x60;pilotpower&#x60;, &#x60;pnoffset&#x60;, &#x60;powrx&#x60;, &#x60;rxlevel&#x60;,     have been deprecated and replaced with     &#x60;altAccuracy&#x60;, &#x60;baseLat&#x60;, &#x60;baseLng&#x60;, &#x60;cellParams&#x60;, &#x60;pilotPower&#x60;, &#x60;pnOffset&#x60;, &#x60;rss&#x60;, &#x60;rxLevel&#x60;     respectively.   - Dependent parameters combined as a subobject.     - CDMA, GSM, WCDMA, TD-SCDMA and LTE local identification parameters for serving cell moved under &#x60;localId&#x60; property.     - GSM neighbor global ID: &#x60;lac&#x60; and &#x60;cid&#x60; for neighbor cell moved under &#x60;globalIdentity&#x60; property. 
    """
)

