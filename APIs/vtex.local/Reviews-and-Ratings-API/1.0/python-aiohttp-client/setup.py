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
    description="Reviews and Ratings API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Reviews and Ratings API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
      Reviews &amp; Ratings is a [VTEX IO native solution](https://developers.vtex.com/vtex-developer-docs/docs/vtex-reviews-and-ratings) that allows shoppers to submit reviews and ratings for products, as well as see them while navigating the store.    ## Rating    - [Get Product Rating](https://developers.vtex.com/vtex-rest-api/reference/getproductrating)    ## Review    - [Get Review by Review ID](https://developers.vtex.com/vtex-rest-api/reference/getreviewbyreviewid)  - [Delete Review](https://developers.vtex.com/vtex-rest-api/reference/deletereview)  - [Update a Review](https://developers.vtex.com/vtex-rest-api/reference/editreview)  - [Get a list of Reviews](https://developers.vtex.com/vtex-rest-api/reference/getalistofreviews)  - [Create Multiple Reviews](https://developers.vtex.com/vtex-rest-api/reference/savemultiplereviews)  - [Delete Multiple Reviews](https://developers.vtex.com/vtex-rest-api/reference/deletemultiplereviews)  - [Create a Review](https://developers.vtex.com/vtex-rest-api/reference/savereview)
    """
)

