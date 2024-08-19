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
    description="Atmosphere API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Atmosphere API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Instantly access empirical models of atmospheric density and  composition that are recommended by the Committee on Space Research (COSPAR) for  satellite drag calculations. &lt;br&gt;&lt;br&gt; API requests must contain a key \&quot;API-Key\&quot; in the header (see code samples). Obtain a key from  &lt;a href&#x3D;&#39;https://developer.amentum.io&#39;&gt;here&lt;/a&gt;. &lt;br&gt;&lt;br&gt;  Help us improve the quality of our web APIs by completing our 2 minute survey &lt;a href&#x3D;\&quot;https://www.surveymonkey.com/r/CTDTRBN\&quot;&gt;here&lt;/a&gt;.&lt;br&gt;&lt;br&gt; Amentum Pty Ltd is not responsible nor liable for any loss or damage of any sort incurred as a result of using the API. &lt;br&gt;&lt;br&gt; Copyright &lt;a href&#x3D;&#39;https://amentum.space&#39;&gt;Amentum Pty Ltd&lt;/a&gt; 2021. 
    """
)

