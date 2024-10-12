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
    description="Amazon SageMaker Feature Store Runtime",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon SageMaker Feature Store Runtime"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Contains all data plane API operations and data types for the Amazon SageMaker Feature Store. Use this API to put, delete, and retrieve (get) features from a feature store.&lt;/p&gt; &lt;p&gt;Use the following operations to configure your &lt;code&gt;OnlineStore&lt;/code&gt; and &lt;code&gt;OfflineStore&lt;/code&gt; features, and to create and manage feature groups:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateFeatureGroup.html\&quot;&gt;CreateFeatureGroup&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteFeatureGroup.html\&quot;&gt;DeleteFeatureGroup&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeFeatureGroup.html\&quot;&gt;DescribeFeatureGroup&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListFeatureGroups.html\&quot;&gt;ListFeatureGroups&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

