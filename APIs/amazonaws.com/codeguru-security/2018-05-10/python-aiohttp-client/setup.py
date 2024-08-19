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
    description="Amazon CodeGuru Security",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon CodeGuru Security"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;note&gt; &lt;p&gt;Amazon CodeGuru Security is in preview release and is subject to change.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This section provides documentation for the Amazon CodeGuru Security API operations. CodeGuru Security is a service that uses program analysis and machine learning to detect security policy violations and vulnerabilities, and recommends ways to address these security risks.&lt;/p&gt; &lt;p&gt;By proactively detecting and providing recommendations for addressing security risks, CodeGuru Security improves the overall security of your application code. For more information about CodeGuru Security, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/security-ug/what-is-codeguru-security.html\&quot;&gt;Amazon CodeGuru Security User Guide&lt;/a&gt;. &lt;/p&gt;
    """
)

