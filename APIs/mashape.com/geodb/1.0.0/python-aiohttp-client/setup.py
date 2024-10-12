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
    description="GeoDB Cities API",
    author_email="",
    url="",
    keywords=["OpenAPI", "GeoDB Cities API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The GeoDB API focuses on getting global city and region data. Easily obtain country, region, and city data for use in your apps!  &lt;ul&gt;   &lt;li&gt;Filter cities by name prefix, country, location, time-zone, and even minimum population.&lt;/li&gt;   &lt;li&gt;Sort cities by name, country code, elevation, and population - or any combination of these.&lt;/li&gt;    &lt;li&gt;Get all country regions.&lt;/li&gt; &lt;li&gt;Get all cities in a given region.&lt;/li&gt;   &lt;li&gt;     Display results in multiple languages.&lt;/li&gt; &lt;li&gt;RESTful API adheres to industry best-practices, including     HATEOAS-style links to facilitate paging results.   &lt;/li&gt;    &lt;li&gt;Backed by cloud-based load-balanced infrastructure for resiliency and performance!&lt;/li&gt;   &lt;li&gt;Data is periodically refreshed from GeoNames and WikiData.&lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Notes: &lt;ul&gt;   &lt;li&gt;     Since the database is periodically updated, this may &lt;strong&gt;very rarely&lt;/strong&gt; result in certain cities     being marked deleted (e.g., duplicates removed). By default, endpoints returning city data will exclude     cities marked deleted. However, in the unlikely event that this occurs while your app is paging through a set     of affected results - and you care about the paged results suddenly changing underneath - specify      &lt;tt&gt;includeDeleted&#x3D;SINCE_YESTERDAY&lt;/tt&gt; (or &lt;tt&gt;SINCE_LAST_WEEK&lt;/tt&gt; if you&#39;re really paranoid!).   &lt;/li&gt; &lt;/ul&gt; &lt;hr/&gt; &lt;h3&gt;Useful Resources&lt;/h3&gt; &lt;ul&gt;   &lt;li&gt;     SDKs     &lt;ul&gt;       &lt;li&gt;         &lt;a href&#x3D;&#39;https://www.npmjs.com/package/wft-geodb-angular-client&#39;&gt;Angular&lt;/a&gt;,          &lt;a href&#x3D;&#39;https://github.com/wirefreethought/geodb-sample-angular-app&#39;&gt;Sample App&lt;/a&gt;       &lt;/li&gt;       &lt;li&gt;&lt;a href&#x3D;&#39;https://github.com/wirefreethought/geodb-java-client&#39;&gt;Java&lt;/a&gt;&lt;/li&gt;       &lt;li&gt;&lt;a href&#x3D;&#39;https://www.npmjs.com/package/wft-geodb-js-client&#39;&gt;JavaScript&lt;/a&gt;&lt;/li&gt;     &lt;/ul&gt;     &lt;li&gt;&lt;a href&#x3D;&#39;swagger.json&#39;&gt;Swagger Docs&lt;/a&gt;&lt;/li&gt;     &lt;li&gt;&lt;a href&#x3D;&#39;http://creativecommons.org/licenses/by/3.0/&#39;&gt;Usage License&lt;/a&gt;&lt;/li&gt;   &lt;/li&gt;       &lt;/ul&gt; 
    """
)

