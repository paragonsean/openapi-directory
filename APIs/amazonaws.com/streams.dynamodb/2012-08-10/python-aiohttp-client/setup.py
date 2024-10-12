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
    description="Amazon DynamoDB Streams",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon DynamoDB Streams"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon DynamoDB&lt;/fullname&gt; &lt;p&gt;Amazon DynamoDB Streams provides API actions for accessing streams and processing stream records. To learn more about application development with Streams, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html\&quot;&gt;Capturing Table Activity with DynamoDB Streams&lt;/a&gt; in the Amazon DynamoDB Developer Guide.&lt;/p&gt;
    """
)

