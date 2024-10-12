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
    description="NeoWs - (Near Earth Object Web Service)",
    author_email="",
    url="",
    keywords=["OpenAPI", "NeoWs - (Near Earth Object Web Service)"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    A web service for near earth objects. All the data is from the &lt;a href&#x3D;\&quot;http://neo.jpl.nasa.gov/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;NASA JPL Asteroid team&lt;/a&gt;.      NeoWs is proud to power AsteroidTracker on &lt;a href&#x3D;\&quot;https://itunes.apple.com/us/app/asteroid-tracker/id689684901?mt&#x3D;8\&quot; target&#x3D;\&quot;_blank\&quot;&gt;iOS&lt;/a&gt; and &lt;a href&#x3D;\&quot;https://play.google.com/store/apps/details?id&#x3D;com.vitruviussoftware.bunifish.asteroidtracker&amp;feature\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Android&lt;/a&gt; as well as related apps.    Follow us on &lt;a href&#x3D;\&quot;https://twitter.com/AsteroidTracker\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Twitter&lt;/a&gt;
    """
)

