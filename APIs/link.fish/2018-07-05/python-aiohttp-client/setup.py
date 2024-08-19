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
    description="link.fish API",
    author_email="api@link.fish",
    url="",
    keywords=["OpenAPI", "link.fish API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    API to easily extract data from websites.   # Base URL   All URLs referenced in the documentation have the following base:   &#x60;&#x60;&#x60; https://api.link.fish &#x60;&#x60;&#x60;   The REST API is only served over HTTPS. To ensure data privacy, unencrypted HTTP is not supported.   # Authentication HTTP requests to the REST API are protected with [HTTP Basic authentication](https://en.wikipedia.org/wiki/Basic_access_authentication). You will use the email address of your link.fish account as the username and your API access token as the password for HTTP Basic authentication.  If you do not have an account yet, go to [https://link.fish/api](https://link.fish/api) and create one first.  You will receive the API access token automatically via email after you signed up. To generate a new token and invalidate the current one log into your link.fish  account at [https://app.link.fish](https://app.link.fish) and go to: \&quot;Plugins\&quot; -&gt; \&quot;API Dashboard\&quot;  There you can also see how many credits you used already.   # Errors The API uses standard HTTP status codes to indicate the success or failure of the API call. The body of the response will be JSON in the following format: &#x60;&#x60;&#x60; {    \&quot;status\&quot;: {HTTP STATUS CODE}   \&quot;message\&quot;: \&quot;{ERROR MESSAGE}\&quot; } &#x60;&#x60;&#x60; Like for example when the authorization is not provided or wrong: &#x60;&#x60;&#x60; {    \&quot;status\&quot;: 401   \&quot;message\&quot;: \&quot;Unauthorized\&quot; } &#x60;&#x60;&#x60;  # Request IDs  Each API request has an associated request identifier. You can find it in the response headers, under X-LF-Request-Id. In case you have problems please provide this identifier that we can help you as good and fast as possible.   Example: &#x60;&#x60;&#x60; X-LF-Request-Id: f7f0036f-5277-421a-b143-f7a151571d18 &#x60;&#x60;&#x60;   # Item format  The data is by default deeply nested. So if it should be checked if there is an offer with a price, the whole tree has to be checked. To make that simpler, it is also possible to return the data \&quot;flat\&quot;. If selected it will flatten the tree by copying all the data to the main level under a property with the name of its type and link the data internally.  Information: We created a node module which allows converting between the two formats. It did not get open sourced yet. If you are in need, simply contact us via api@link.fish.   # Response Content Type By default, all data gets returned as JSON. If the data should be returned as XML add the following header:  &#x60;&#x60;&#x60; Accept: application/xml &#x60;&#x60;&#x60;  # Credits  Depending on the request made a different amount of credits get charged. How many which request costs can be found on the [API pricing page](http://link.fish/api/#pricing). Additionally, does a  header named \&quot;X-LF-Credits-Charged\&quot; get added to each successful response with information about the credits.  Example: &#x60;&#x60;&#x60; X-LF-Credits-Charged: 1 # Credits used for current requests X-LF-Credits-Subscription-Max: 1000 # Total credits available in subscription X-LF-Credits-Subscription-Used: 512 # Credits still left in current month &#x60;&#x60;&#x60; You can check anytime how many credits you did use already by logging into your link.fish  account at [https://app.link.fish](https://app.link.fish) and checking under:  \&quot;Plugins\&quot; -&gt; \&quot;API Dashboard\&quot;   If you have problems, questions or improvement advice please send us an email to api@link.fish 
    """
)

