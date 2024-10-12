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
    description="GiftCard Hub API",
    author_email="",
    url="",
    keywords=["OpenAPI", "GiftCard Hub API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &gt;ℹ️ Check the new [Payments onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/payments-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Payments and is organized by focusing on the developer&#39;s journey.    The Gift Card Hub API allows interactions with all Gift Card providers registered to a store from a single point.    Gift Card providers are systems capable of providing cards to be used in the buying process.    The following is the sequence diagram that represents calls in the purchase closing process.  ![](https://cdn.jsdelivr.net/gh/vtexdocs/dev-portal-content@main/images/giftcard-hub-api-overview-0.png)    **Checkout + Gateway**: Systems responsible for the sale and for processing orders and payments.    **Gift Card Hub**: System responsible for managing multiple registered Gift Card providers for a store.    **Gift Card Provider**: System responsible for providing the Gift Cards available to the user not closing a purchase. This system can be implemented by third parties.
    """
)

