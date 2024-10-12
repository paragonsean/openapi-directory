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
    description="My Business Business Calls API",
    author_email="",
    url="",
    keywords=["OpenAPI", "My Business Business Calls API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The My Business Business Calls API manages business calls information of a location on Google and collect insights like the number of missed calls to their location. Additional information about Business calls can be found at https://support.google.com/business/answer/9688285?p&#x3D;call_history. If the Google Business Profile links to a Google Ads account and call history is turned on, calls that last longer than a specific time, and that can be attributed to an ad interaction, will show in the linked Google Ads account under the \&quot;Calls from Ads\&quot; conversion. If smart bidding and call conversions are used in the optimization strategy, there could be a change in ad spend. Learn more about smart bidding. To view and perform actions on a location&#39;s calls, you need to be a &#x60;OWNER&#x60;, &#x60;CO_OWNER&#x60; or &#x60;MANAGER&#x60; of the location. Note - If you have a quota of 0 after enabling the API, please request for GBP API access.
    """
)

