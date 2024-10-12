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
    description="AWS Elastic Beanstalk",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Elastic Beanstalk"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;AWS Elastic Beanstalk&lt;/fullname&gt; &lt;p&gt;AWS Elastic Beanstalk makes it easy for you to create, deploy, and manage scalable, fault-tolerant applications running on the Amazon Web Services cloud.&lt;/p&gt; &lt;p&gt;For more information about this product, go to the &lt;a href&#x3D;\&quot;http://aws.amazon.com/elasticbeanstalk/\&quot;&gt;AWS Elastic Beanstalk&lt;/a&gt; details page. The location of the latest AWS Elastic Beanstalk WSDL is &lt;a href&#x3D;\&quot;https://elasticbeanstalk.s3.amazonaws.com/doc/2010-12-01/AWSElasticBeanstalk.wsdl\&quot;&gt;https://elasticbeanstalk.s3.amazonaws.com/doc/2010-12-01/AWSElasticBeanstalk.wsdl&lt;/a&gt;. To install the Software Development Kits (SDKs), Integrated Development Environment (IDE) Toolkits, and command line tools that enable you to access the API, go to &lt;a href&#x3D;\&quot;http://aws.amazon.com/tools/\&quot;&gt;Tools for Amazon Web Services&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Endpoints&lt;/b&gt; &lt;/p&gt; &lt;p&gt;For a list of region-specific endpoints that AWS Elastic Beanstalk supports, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/rande.html#elasticbeanstalk_region\&quot;&gt;Regions and Endpoints&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Glossary&lt;/i&gt;.&lt;/p&gt;
    """
)

