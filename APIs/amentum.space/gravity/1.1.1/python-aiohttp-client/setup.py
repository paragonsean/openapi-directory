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
    description="Gravity API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Gravity API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The gravitational field of the earth is non-uniform.  The &lt;a href&#x3D;&#39;https://en.wikipedia.org/wiki/Geoid&#39;&gt;geoid&lt;/a&gt; is the shape the  ocean surface would take if only gravity and the rotation of the Earth   were considered. The geoid is the surface that defines zero elevation.&lt;br&gt;&lt;br&gt;  The geoid height is the difference between an ideal reference ellipsoid  and the geoid.&lt;br&gt;&lt;br&gt; The gravity anomaly is the difference between the acceleration due to gravity on the Earth&#39;s surface and the value calculated assuming the reference ellipsoid.&lt;br&gt;&lt;br&gt; The official Earth Gravitational Model &lt;a href&#x3D;https://en.wikipedia.org/wiki/Earth_Gravitational_Model#EGM2008/&gt;EGM2008&lt;/a&gt; was developed and  released to the public by the National Geospatial-Intelligence Agency (NGA).&lt;br&gt;&lt;br&gt; Our EGM2008 API provides on-demand access to the EGM2008 model, as implemented by the open-source GeographicLib  &lt;a href&#x3D;https://geographiclib.sourceforge.io/html/gravity.html&gt;Gravity&lt;/a&gt; library.&lt;br&gt;&lt;br&gt; API requests must contain a key \&quot;API-Key\&quot; in the header (see code samples). Obtain a key from  &lt;a href&#x3D;&#39;https://developer.amentum.io&#39;&gt;here&lt;/a&gt;. &lt;br&gt;&lt;br&gt;  Amentum Pty Ltd is not responsible nor liable for any loss or damage of any sort incurred as a result of using the API. &lt;br&gt;&lt;br&gt; Copyright &lt;a href&#x3D;&#39;https://amentum.space&#39;&gt;Amentum Pty Ltd&lt;/a&gt; 2021. 
    """
)

