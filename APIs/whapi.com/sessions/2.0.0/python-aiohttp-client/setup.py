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
    description="Sessions API",
    author_email="platform@williamhill.com",
    url="",
    keywords=["OpenAPI", "Sessions API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The William Hill Sessions API uses a central authentication service (CAS*) on all resources that require access to a customer’s account or betting functionality. To authenticate, you’ll need to supply a sportsbook username and password, in return you will be given an authentication ticket, which you can use on the majority of requests found within our services. &lt;br /&gt;&lt;br /&gt;&lt;br /&gt; The Sessions API should be used whenever you want to login a customer and:&lt;br /&gt;&lt;br /&gt; &lt;ul&gt; &lt;li&gt;continue to use the William Hill API for that customer’s transactions&lt;/li&gt; &lt;li&gt;use other CAS-enabled William Hill services outside the suite of APIs&lt;/li&gt; &lt;/ul&gt; &lt;br /&gt; CAS is an enterprise Single Sign-On solution for web services (see https://wiki.jasig.org/display/CAS/Home). It is used by many William Hill services. &lt;br /&gt; Note: all requests must be executed over HTTPS and include an API key and secret.&lt;br /&gt;&lt;br /&gt;&lt;br /&gt; &lt;b&gt;Authentication Ticket Expiration Times&lt;/b&gt;&lt;br /&gt;&lt;br /&gt; When a customer is logged in using the Sessions API, they are given an Authentication Ticket; using this ticket on subsequent API requests gives you access to account activities (such as placing a bet, deposits, etc). However, this ticket is only valid for a given period of time depending on how it is used. If the ticket is used and then has a period of inactivity longer than 7,200 seconds (2 hours), then the ticket will expire and further requests using the ticket will be denied - in effect, a customer has been logged out and will need to authenticate again. &lt;br /&gt;&lt;br /&gt;&lt;br /&gt; Normally, any ticket issued only has a maximum life expectancy of 28,000 seconds (8 hours) after which it can no longer be used, even if it has been used regularly. The customer again will be effectively logged out and will need to authenticate again. If you wish to avoid this, you need to set the query parameter extended to Y, which will enable your application to generate a ticket valid for 60 days without expiring due to inactivity. &lt;br /&gt;
    """
)

