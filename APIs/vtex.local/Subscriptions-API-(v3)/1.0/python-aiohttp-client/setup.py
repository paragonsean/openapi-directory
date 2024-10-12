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
    description="Subscriptions API (v3)",
    author_email="",
    url="",
    keywords=["OpenAPI", "Subscriptions API (v3)"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
      A **Subscription** is a list of items (SKUs) tied to certain recurring purchase settings:    - User profile  - Address  - Payment method  - Frequency  - Cycle    Once you have [configured subscriptions](https://help.vtex.com/tutorial/how-to-configure-subscriptions%20--1FA9dfE7vJqxBna9Nft5Sj) in your store, the Subscriptions API allows you to create, manage and monitor your customers&#39; subscriptions.    ![image](https://user-images.githubusercontent.com/77292838/213024675-9407863b-0c55-4282-9442-306352716abe.png)    To read more about the Subscriptions feature, check our article [How Subscription works](https://help.vtex.com/tutorial/how-subscriptions-work--frequentlyAskedQuestions_4453).
    """
)

