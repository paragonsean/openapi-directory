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
    description="VTEX Headless CMS",
    author_email="",
    url="",
    keywords=["OpenAPI", "VTEX Headless CMS"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
     The VTEX Headless CMS is a no-code management system for storefront content.  That means you can store your content as structured data in a layer decoupled from the frontend and  use the VTEX Headless CMS to access and deliver your content to your storefront project.  Notice that the VTEX Headless CMS typically works with **FastStore** projects only. In this case, you can use this API to fetch data using SSR (NextJS and Gatsby v4+) or SSG (NextJS).  **Servers** - &#x60;https://{account}.myvtex.com/&#x60; - &#x60;https://{workspace}--{account}.myvtex.com/&#x60;  **Server variables** - &#x60;accountName&#x60;: Name of your VTEX account. - &#x60;workspace&#x60;: Name of your VTEX workspace. 
    """
)

