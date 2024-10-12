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
    description="Perspective Comment Analyzer API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Perspective Comment Analyzer API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Perspective Comment Analyzer API provides information about the potential impact of a comment on a conversation (e.g. it can provide a score for the \&quot;toxicity\&quot; of a comment). Users can leverage the \&quot;SuggestCommentScore\&quot; method to submit corrections to improve Perspective over time. Users can set the \&quot;doNotStore\&quot; flag to ensure that all submitted comments are automatically deleted after scores are returned.
    """
)

