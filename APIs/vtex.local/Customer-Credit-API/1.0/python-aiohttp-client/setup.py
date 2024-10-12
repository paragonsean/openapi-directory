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
    description="Customer Credit API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Customer Credit API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    With Customer Credit your store can enable **credit payments** through the checkout. You can also control **invoices** and the **credit limits** of your clients.    Learn more about Customer Credit in our [Help Center article](https://help.vtex.com/en/tracks/customer-credit-getting-started--1hCRg21lXYy2seOKgqQ2CC/36grlQ69NK6OCuioeekyCs).    All requests need the **authorization header**.    Additionally, you can find more information on installment payments for an order in the &#x60;customData&#x60;  field found in the [Get Order](https://developers.vtex.com/docs/api-reference/orders-api#get-/api/oms/pvt/orders/-orderId-) endpoint of the Orders API. This includes the number of installments, amount and due dates.    This API allows two kinds of authorization:  1. Authorization header containing the VTEX ID authentication token.  2. VTEX Appkey and Apptoken headers.
    """
)

