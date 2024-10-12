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
    description="ThreatJammer.com User API",
    author_email="support@threatjammer.com",
    url="",
    keywords=["OpenAPI", "ThreatJammer.com User API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
     The public API open to the users. [Read the docs and learn more.](https://threatjammer.com/docs).  ## General information  ### Description Threat Jammer supports two end-user REST APIs: the User API and the Report API. The end-user uses the User API to interact with the different databases, heuristics, and machine learning processes. Devices use the Report API to interact with Threat Jammer. This document will explain how to use the User API and interact with the different services, create a token, interpret the quota information, and create the HTTP request to interact with the User API.  ### Authentication The API is protected by a **Bearer authentication** schema. **Bearer authentication** (also called **token authentication**) is an HTTP authentication scheme that involves security tokens called bearer tokens. It is used to authenticate the user. All the different endpoints expect a &#x60;Bearer&#x60; token in the &#x60;Authorization&#x60; header.  Example:  &#x60;&#x60;&#x60; curl -X &#39;GET&#39;   &#39;https://dublin.api.threatjammer.com/test&#39;   -H &#39;accept: application/json&#39;   -H &#39;Authorization: Bearer YOUR_API_KEY&#39; &#x60;&#x60;&#x60;  You can obtain a token after registering on the [ThreatJammer.com](https://threatjammer.com) website for free.   ### Region specific tokens All the &#x60;Bearer&#x60; tokens contain information about the authorized region. The developers have to use a token created for the region they want to use. A token used in a different region will return a &#x60;401 Unauthorized&#x60; error.  ### Global errors  The API will return the following permanent errors: - a &#x60;401 Unauthorized&#x60; error if the token is not valid, or does not belong to the region. - a &#x60;401 Unauthorized&#x60; error if the token does not exist. - a &#x60;401 Unauthorized&#x60; error if the token is malformed. - a &#x60;403 Forbidden&#x60; error if the subscription level is not enough. Some endpoints are only available for paid subscription levels.  And these temporary errors: - a &#x60;429 Too Many Requests&#x60; error if the quota is exceeded (see below).  ### Quota limits  **Every request to the User API will consume one (1) quota point.**  The API has two rate limiting processes: - a quota limit of **5000** requests per month for the &#x60;FREE&#x60; account. The limit is reset every month. - a quota limit of **10** requests per minute for the &#x60;FREE&#x60; account. The limit is reset every minute and implements a sliding window mechanism.  
    """
)

