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
    description="HHS Media Services API",
    author_email="syndicationadmin@hhs.gov",
    url="",
    keywords=["OpenAPI", "HHS Media Services API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;div class&#x3D;\&quot;swagger-ui-wrap extraFooter\&quot;&gt;&lt;h3&gt;Common Features / Behaviors&lt;/h3&gt; &lt;div class&#x3D;\&quot;features\&quot;&gt; &lt;ul&gt; &lt;li&gt;&lt;strong&gt;* \&quot;sort\&quot; param:&lt;/strong&gt; supports multi column sorting through the use of commas as delimiters, and a hyphen to denote descending order. &lt;br/&gt; &lt;strong&gt;&lt;span&gt;Examples:&lt;/span&gt;&lt;/strong&gt; &lt;ul&gt; &lt;li&gt;&lt;span class&#x3D;\&quot;example\&quot;&gt;name&lt;/span&gt;&lt;span class&#x3D;\&quot;description\&quot;&gt;sort results by name ascending&lt;/span&gt;&lt;/li&gt; &lt;li&gt;&lt;span class&#x3D;\&quot;example\&quot;&gt;-name&lt;/span&gt;&lt;span class&#x3D;\&quot;description\&quot;&gt;sort results by name descending&lt;/span&gt;&lt;/li&gt; &lt;li&gt;&lt;span class&#x3D;\&quot;example\&quot;&gt;-name,id&lt;/span&gt;&lt;span class&#x3D;\&quot;description\&quot;&gt;sort results by name descending and then by id ascending&lt;/span&gt;&lt;/li&gt; &lt;li&gt;&lt;span class&#x3D;\&quot;example\&quot;&gt;id,-dateContentAuthored&lt;/span&gt;&lt;span class&#x3D;\&quot;description\&quot;&gt;sort results by id ascending and then date descending&lt;/span&gt;&lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt;&lt;strong&gt;Date formats:&lt;/strong&gt; Date input format is expected to be based on &lt;a href&#x3D;\&quot;http://www.ietf.org/rfc/rfc3339.txt\&quot;&gt;RFC 3339&lt;/a&gt;. &lt;br/&gt; &lt;span&gt;&lt;strong&gt;Example:&lt;/strong&gt;&lt;/span&gt; &lt;ul&gt;&lt;li&gt;2013-11-18T18:43:01Z&lt;/li&gt;&lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/div&gt; &lt;/div&gt;
    """
)

