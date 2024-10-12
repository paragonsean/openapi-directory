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
    description="Veteran Confirmation",
    author_email="",
    url="",
    keywords=["OpenAPI", "Veteran Confirmation"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Deprecated Veteran Confirmation API allows you to confirm Veteran status for a given person. This can be useful for offering Veterans discounts or other benefits.  The API will only return “Confirmed” or “Not Confirmed”.  ## Quickstart Guide ### 1. Get Access Credentials Get started by filling out the form on the [Apply for VA Lighthouse Developer Access](https://developer.va.gov/apply) page.  After submitting a request, you will receive your credentials for using the API in the Development environment, which allows you to try it out with mock data before moving to the Production environment.  ### 2. Test the API In the endpoint documentation below, we&#39;ve provided a curl command builder for trying out the API before implementation with your app. Use [Test User](https://github.com/department-of-veterans-affairs/vets-api-clients/blob/master/test_accounts/confirmation_test_accounts.md) attributes to populate the request body.  ### 3. Build your app The base URI for the Veteran Confirmation API in the Sandbox environment is:  https://sandbox-api.va.gov/services/veteran_confirmation/v0  In this environment, use attributes from the list of [Test Users](https://github.com/department-of-veterans-affairs/vets-api-clients/blob/master/test_accounts/confirmation_test_accounts.md). Only Test Users can return a &#x60;\&quot;confirmed\&quot;&#x60; response.  Check out some of our [sample apps](https://github.com/department-of-veterans-affairs/vets-api-clients). Please visit our VA Lighthouse [Support portal](https://developer.va.gov/support) should you need further assistance.  ### 4. Show us a demo and get access to the Production environment After building your app, we ask that you give us a demo before we set you up with production credentials. Please see the [Path to Production](https://developer.va.gov/go-live) page for more details.  ## Authorization This API requires an API key in combination with identifiable information for the person being confirmed listed below. API requests are authorized through a symmetric API token provided in an HTTP header with name &#x60;apikey&#x60;. Including more information has a better chance of making a match and returning a Confirmed status. ### Required information: * First Name * Last Name * Date of Birth * Social Security Number  ### Optional information: * Middle Name * Gender  ## Reference ### Sandbox vs. Production Data APIs accessed via the Sandbox environment are using the same underlying logic as VA’s production APIs; only the underlying data store is different.  ### Master Veteran Index (MVI) The Master Veteran Index confirms a user&#39;s identity. In Production, several factors are considered to confirm identity. These include: a user’s first name, last name, date of birth and Social Security number. The MVI is mocked in the Sandbox environment. In this environment, the only factor used to confirm identity is the Social Security number.  ### Rate Limiting We implemented basic rate limiting of 60 requests per minute. If you exceed this quota, your request will return a 429 status code. You may petition for increased rate limits by emailing and requests will be decided on a case by case basis.  ### Raw Open API Spec https://api.va.gov/services/veteran_confirmation/docs/v0/api 
    """
)

