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
    description="SearchLy API v1",
    author_email="hi@asuarez.dev",
    url="",
    keywords=["OpenAPI", "SearchLy API v1"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    # Introduction The SearchLy API provides similarity searching based on song lyrics.  # Operations The API allows for the &#x60;/similarity/by_song&#x60; operation, which allows clients to search the similarity for an existing song in the database. Also, the API has an additional &#x60;/similarity/by_content&#x60; endpoint which allows clients to search similarity given a free String input through a JSON request body. Additional &#x60;/song/search&#x60; operation is available for searching songs given a query String.  # Endpoint The API endpoint for the SearchLy API v1 is as follows: &#x60;&#x60;&#x60; https://searchly.asuarez.dev/api/v1 &#x60;&#x60;&#x60;  # Motivation This project was built in order to create an API for searching similarities based on song lyrics. There are a lot of songs in the industry and most of them are talking about the same topic. What I wanted to prove with SearchLy was to estimate how similar are two songs between them based on the meaning of their lyrics.  SearchLy is using a database of 100k songs from AZLyrics, using [this scraper](https://github.com/AlbertSuarez/azlyrics-scraper), which is being updated periodically. Then, using word2vec and NMSLIB, it was possible to create an index where you can search similarities using the k-nearest neighbors (KNN) algorithm.  &gt; **Note**: I am currently using a micro-instance from DigitalOcean where the API is deployed, so you should expect a bad performance. However, if this API becomes popular I will deploy it in a bigger instance. 
    """
)

