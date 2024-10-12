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
    description="Spinitron v2 API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Spinitron v2 API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    ## Notes  **Tutorial demo** using this API is at [https://spinitron.com/v2-api-demo/](https://spinitron.com/v2-api-demo/). For web integration using iframes and/or JavaScript instead of an API, see [https://spinitron.github.io/v2-web-integration/](https://spinitron.github.io/v2-web-integration/).  **Your API key** is found in the Spinitron web app. Log in to Spinitron and go to *Automation &amp; API* in the *Admin* menu.  **Authenticate** by presenting your API key using either HTTP Bearer Authorization (preferred)      curl -H &#39;Authorization: Bearer YOURAPIKEY&#39; &#39;https://spinitron.com/api/spins&#39;  or in the query parameter &#x60;access-token&#x60; (less secure owing to webserver log files)      curl &#39;https://spinitron.com/api/spins?access-token&#x3D;YOURAPIKEY&#39;  **Limit** per page of results is 20 by default and miximally 200.  **Try it out** below works to generate example cURL requests but not to get responses from Spinitron. We do not accept queries sent from web browsers. Copy-paste the cURL commands and run them from your computer.  **Cache** the data you get from the API if you are using it in web or mobile integration. It&#39;s not ok to query the API on *every* page request you serve. The [demo](https://spinitron.com/v2-api-demo/) shows how easy it can be to implement a file cache.  An extension to this API with access to all stations for partner applications is available. Contact us. 
    """
)

