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
    description="Netatmo",
    author_email="contact-api@netatmo.com",
    url="",
    keywords=["OpenAPI", "Netatmo"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;h3&gt;Welcome to the Netatmo swagger on-line documentation !&lt;/h3&gt; This site is a complement to the official &lt;a href&#x3D;\&quot;https://dev.netatmo.com/\&quot;&gt;Netatmo developper documentation&lt;/a&gt; using swagger to bring interactivity and easy testing of requests with the \&quot;try it\&quot; button (authenticate with the authorization code OAuth2 flow by clicking the authenticate button in the methods). You can find the source code for this site can be found in the project &lt;a href&#x3D;\&quot;https://github.com/cbornet/netatmo-swagger-ui\&quot;&gt;netatmo-swagger-ui&lt;/a&gt;. You can also use the online &lt;a href&#x3D;\&quot;./swagger.json\&quot;&gt;swagger declaration&lt;/a&gt; file to generate code or static documentation (see &lt;a href&#x3D;\&quot;https://github.com/cbornet/netatmo-swagger-api\&quot;&gt;netatmo-swagger-api&lt;/a&gt;). 
    """
)

