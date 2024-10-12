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
    description="Amazon Personalize Events",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Personalize Events"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Amazon Personalize can consume real-time user event data, such as &lt;i&gt;stream&lt;/i&gt; or &lt;i&gt;click&lt;/i&gt; data, and use it for model training either alone or combined with historical data. For more information see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/personalize/latest/dg/recording-events.html\&quot;&gt;Recording Events&lt;/a&gt;.
    """
)

