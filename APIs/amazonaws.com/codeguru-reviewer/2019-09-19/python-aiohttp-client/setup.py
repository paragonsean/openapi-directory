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
    description="Amazon CodeGuru Reviewer",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon CodeGuru Reviewer"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;This section provides documentation for the Amazon CodeGuru Reviewer API operations. CodeGuru Reviewer is a service that uses program analysis and machine learning to detect potential defects that are difficult for developers to find and recommends fixes in your Java and Python code.&lt;/p&gt; &lt;p&gt;By proactively detecting and providing recommendations for addressing code defects and implementing best practices, CodeGuru Reviewer improves the overall quality and maintainability of your code base during the code review stage. For more information about CodeGuru Reviewer, see the &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html\&quot;&gt;Amazon CodeGuru Reviewer User Guide&lt;/a&gt;.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;To improve the security of your CodeGuru Reviewer API calls, you can establish a private connection between your VPC and CodeGuru Reviewer by creating an &lt;i&gt;interface VPC endpoint&lt;/i&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/vpc-interface-endpoints.html\&quot;&gt;CodeGuru Reviewer and interface VPC endpoints (Amazon Web Services PrivateLink)&lt;/a&gt; in the &lt;i&gt;Amazon CodeGuru Reviewer User Guide&lt;/i&gt;.&lt;/p&gt;
    """
)

