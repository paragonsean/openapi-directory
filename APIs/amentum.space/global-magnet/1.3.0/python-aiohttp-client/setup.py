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
    description="Geomag API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Geomag API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
     The World Magnetic Model calculates the intensity and direction of the Earth&#39;s magnetic field on a specific date-time, geodetic altitude, latitude, and longitude. It is relied upon throughout the world for navigation, mineral exploration, atmospheric and space science, and is installed on billions of devices.  &lt;br&gt;&lt;br&gt; A comprehensive description of the World Magnetic Model, including its  limitations, can be found &lt;a href&#x3D;&#39;https://www.ngdc.noaa.gov/geomag/WMM/&#39;&gt;here&lt;/a&gt;.  &lt;br&gt;&lt;br&gt; We provide a RESTful API to access the out-of-cycle  World Magnetic Model (WMM2015v2) valid for years 2015.0 - 2020.0 and WMM2020 valid for years 2020.0 - 2025.0&lt;br&gt;&lt;br&gt; API requests must contain a key \&quot;API-Key\&quot; in the header (see code samples). Obtain a key from  &lt;a href&#x3D;&#39;https://developer.amentum.io&#39;&gt;here&lt;/a&gt;. &lt;br&gt;&lt;br&gt;  Amentum Pty Ltd is not responsible nor liable for any loss or damage of any sort incurred as a result of using the API. &lt;br&gt;&lt;br&gt; Help us improve the quality of our web APIs by completing our 2 minute survey &lt;a href&#x3D;\&quot;https://www.surveymonkey.com/r/CTDTRBN\&quot;&gt;here&lt;/a&gt;.&lt;br&gt;&lt;br&gt; Copyright &lt;a href&#x3D;&#39;https://amentum.space&#39;&gt;Amentum Pty Ltd&lt;/a&gt; 2021. 
    """
)

