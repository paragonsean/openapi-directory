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
    description="Spotify Web API with fixes and improvements from sonallux",
    author_email="",
    url="",
    keywords=["OpenAPI", "Spotify Web API with fixes and improvements from sonallux"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    You can use Spotify&#39;s Web API to discover music and podcasts, manage your Spotify library, control audio playback, and much more. Browse our available Web API endpoints using the sidebar at left, or via the navigation bar on top of this page on smaller screens.  In order to make successful Web API requests your app will need a valid access token. One can be obtained through &lt;a href&#x3D;\&quot;https://developer.spotify.com/documentation/general/guides/authorization-guide/\&quot;&gt;OAuth 2.0&lt;/a&gt;.  The base URI for all Web API requests is &#x60;https://api.spotify.com/v1&#x60;.  Need help? See our &lt;a href&#x3D;\&quot;https://developer.spotify.com/documentation/web-api/guides/\&quot;&gt;Web API guides&lt;/a&gt; for more information, or visit the &lt;a href&#x3D;\&quot;https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer\&quot;&gt;Spotify for Developers community forum&lt;/a&gt; to ask questions and connect with other developers. 
    """
)

