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
    description="Amazon Macie",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Macie"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon Macie Classic&lt;/fullname&gt; &lt;p&gt;Amazon Macie Classic has been discontinued and is no longer available.&lt;/p&gt; &lt;p&gt;A new Amazon Macie is now available with significant design improvements and additional features, at a lower price and in most Amazon Web Services Regions. We encourage you to take advantage of the new and improved features, and benefit from the reduced cost. To learn about features and pricing for the new Macie, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/macie/\&quot;&gt;Amazon Macie&lt;/a&gt;. To learn how to use the new Macie, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html\&quot;&gt;Amazon Macie User Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

