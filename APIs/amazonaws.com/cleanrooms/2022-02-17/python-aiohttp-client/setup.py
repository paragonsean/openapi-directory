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
    description="AWS Clean Rooms Service",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Clean Rooms Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Welcome to the &lt;i&gt;Clean Rooms API Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Clean Rooms is an Amazon Web Services service that helps multiple parties to join their data together in a secure collaboration workspace. In the collaboration, members who can query and receive results can get insights into the collective datasets without either party getting access to the other party&#39;s raw data.&lt;/p&gt; &lt;p&gt;To learn more about Clean Rooms concepts, procedures, and best practices, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clean-rooms/latest/userguide/what-is.html\&quot;&gt;Clean Rooms User Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

