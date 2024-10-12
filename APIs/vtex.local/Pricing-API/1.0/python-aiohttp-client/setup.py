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
    description="Pricing API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Pricing API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
      &gt; Check the new [Pricing onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/pricing-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Pricing and is organized by focusing on the developer&#39;s journey.    Pricing is the VTEX module responsible for the SKU&#39;s price list. At this module we have the base price of each SKU, some optional fixed prices by trade policy, and some rules that can be applied to generate dynamically different final prices according to the purchase context and the trade policy. The variables used in this collection are:      * **{{accountName}}** &#x3D; You VTEX account name.    * **{{tradePolicyId}}** &#x3D; Current Trade Policy ID.    * **{{itemId}}** &#x3D; SKU ID.    * **{{X-VTEX-API-AppKey}}** and **{{X-VTEX-API-AppToken}}** &#x3D; Credentials.    You can get more information about how to use this module and its business logic at [VTEX Help](http://help.vtex.com).    ## Rate Limits    ### Limits per route    - &#x60;GET&#x60;:  routes are not rate limited at the moment  - &#x60;PUT or POST&#x60;: &#x60;40 requests/second/account&#x60; in any **price insert/update route** with 1000 *Burst Credits*  - &#x60;DELETE&#x60;: &#x60;16 requests/second/account&#x60; in any **price deletion route**, with 300 *Burst Credits*.    ### What are Burst Credits?    In case the account exceeds the limit frequency for a  &#x60;Rate Limiter&#x60; (for instance, when one account makes &#x60;41 requests/second&#x60; in any &#x60;price insert/update route&#x60;), we decrease from the *Burst Credit* count the exceeding (in this example, *1 Credit*).    In the event of the *Burst Credits* reaching **0 (zero)**, the request is blocked with a &#x60;Status 429&#x60; response.    The credits fill up over time when the route is not being used, in the same rate as the route&#39;s &#x60;Rate Limiter&#x60;. In our example, for each second not sending a **PUT or POST request**, we increase *40 Burst Credits* to this &#x60;Rate Limiter&#x60;    ### New Response Headers    In the response headers of any request to Pricing v2 there are some new headers indicating the current status of the Rate Limiting.  This information may be useful to evaluate the ideal frequency to send requests to a route, and when to send a new request in the event of reaching a Rate Limit.    - &#x60;Ratelimit-Limit&#x60; - Total *Burst Credits* offered to a route  - &#x60;Ratelimit-Remaining&#x60; - How many *Burst Credits* are still available to use  - &#x60;Ratelimit-Reset&#x60; - How long (in seconds) it will take to the *Burst Credits* to fill up completely (It will fill up to the &#x60;Ratelimit-Limit&#x60;)  - &#x60;Retry-After&#x60; - Indicates how many seconds you will need to wait until the &#x60;Rate Limiter&#x60; accepts a new request to this route again. If this header response exists, this means your current request has been rate limited and has not been processed.    ### How to integrate with Pricing v2 considering our Rate Limits    Integrate considering the limits of **requests/route/account** specified in the [*Limits per route*](#rate-limits) section, avoiding to surpass this frequency.    If you happen to be Rate Limited, wait the time in seconds specified in &#x60;Retry-After&#x60; before making another request to the service, and reduce the rate of requests per second that your integration is making.
    """
)

