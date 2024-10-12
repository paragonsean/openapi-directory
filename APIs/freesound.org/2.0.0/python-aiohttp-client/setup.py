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
    description="Freesound",
    author_email="",
    url="",
    keywords=["OpenAPI", "Freesound"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    With the Freesound APIv2 you can browse, search, and retrieve information about Freesound users, packs, and the sounds themselves of course. You can find similar sounds to a given target (based on content analysis) and retrieve automatically extracted features from audio files, as well as perform advanced queries combining content analysis features and other metadata (tags, etc...). With the Freesound APIv2, you can also upload, comment, rate and bookmark sounds!
    """
)

