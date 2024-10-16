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
    description="CORE API v2",
    author_email="",
    url="",
    keywords=["OpenAPI", "CORE API v2"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p style&#x3D;\&quot;text-align: justify;\&quot;&gt;You can use the CORE API to access the      resources harvested and enriched by CORE. If you encounter any problems with the API, please &lt;a href&#x3D;\&quot;/contact\&quot;&gt;report them to us&lt;/a&gt;.&lt;/p&gt;  &lt;h2&gt;Overview&lt;/h2&gt; &lt;p style&#x3D;\&quot;text-align: justify;\&quot;&gt;The API is organised by resource type. The resources are &lt;b&gt;articles&lt;/b&gt;,      &lt;b&gt;journals&lt;/b&gt; and &lt;b&gt;repositories&lt;/b&gt; and are represented using JSON data format. Furthermore,      each resource has a list of methods. The API also provides two global methods for accessing all resources at once.&lt;/p&gt;  &lt;h2&gt;Response format&lt;/h2&gt; &lt;p style&#x3D;\&quot;text-align: justify;\&quot;&gt;Response for each query contains two fields: &lt;b&gt;status&lt;/b&gt; and &lt;b&gt;data&lt;/b&gt;.     In case of an error status, the data field is empty. The data field contains a single object     in case the request is for a specific identifier (e.g. CORE ID, CORE repository ID, etc.), or       contains a list of objects, for example for search queries. In case of batch requests, the response     is an array of objects, each of which contains its own &lt;b&gt;status&lt;/b&gt; and &lt;b&gt;data&lt;/b&gt; fields.     For search queries the response contains an additional field &lt;b&gt;totalHits&lt;/b&gt;, which is the      total number of items which match the search criteria.&lt;/p&gt;  &lt;h2&gt;Search query syntax&lt;/h2&gt;  &lt;p style&#x3D;\&quot;text-align: justify\&quot;&gt;Complex search queries can be used in all of the API search methods.     The query can be a simple string or it can be built using terms and operators described in Elasticsearch     &lt;a href&#x3D;\&quot;http://www.elastic.co/guide/en/elasticsearch/reference/1.4/query-dsl-query-string-query.html#query-string-syntax\&quot;&gt;documentation&lt;/a&gt;.     The usable field names are &lt;strong&gt;title&lt;/strong&gt;, &lt;strong&gt;description&lt;/strong&gt;, &lt;strong&gt;fullText&lt;/strong&gt;,      &lt;strong&gt;authors&lt;/strong&gt;, &lt;strong&gt;publisher&lt;/strong&gt;, &lt;strong&gt;repositories.id&lt;/strong&gt;, &lt;strong&gt;repositories.name&lt;/strong&gt;,      &lt;strong&gt;doi&lt;/strong&gt;, &lt;strong&gt;oai&lt;/strong&gt;, &lt;strong&gt;identifiers&lt;/strong&gt; (which is a list of article identifiers including OAI, URL, etc.), &lt;strong&gt;language.name&lt;/strong&gt;      and &lt;strong&gt;year&lt;/strong&gt;. Some example queries: &lt;/p&gt;  &lt;ul style&#x3D;\&quot;margin-left: 30px;\&quot;&gt;     &lt;li&gt;&lt;p&gt;title:psychology and language.name:English&lt;/p&gt;&lt;/li&gt;     &lt;li&gt;&lt;p&gt;repositories.id:86 AND year:2014&lt;/p&gt;&lt;/li&gt;     &lt;li&gt;&lt;p&gt;identifiers:\&quot;oai:aura.abdn.ac.uk:2164/3837\&quot; OR identifiers:\&quot;oai:aura.abdn.ac.uk:2164/3843\&quot;&lt;/p&gt;&lt;/li&gt;     &lt;li&gt;&lt;p&gt;doi:\&quot;10.1186/1471-2458-6-309\&quot;&lt;/p&gt;&lt;/li&gt; &lt;/ul&gt;  &lt;h3&gt;Retrieving the latest Articles&lt;/h3&gt; &lt;p style&#x3D;\&quot;text-align: justify\&quot;&gt;     You can retrieve the harvested items since specific dates using the following queries: &lt;/p&gt;  &lt;ul style&#x3D;\&quot;margin-left: 30px;\&quot;&gt;     &lt;li&gt;&lt;p&gt;repositoryDocument.metadataUpdated:&gt;2017-02-10&lt;/p&gt;&lt;/li&gt;     &lt;li&gt;&lt;p&gt;repositoryDocument.metadataUpdated:&gt;2017-03-01 AND repositoryDocument.metadataUpdated:&lt;2017-03-31&lt;/p&gt;&lt;/li&gt;     &lt;/ul&gt;  &lt;h2&gt;Sort order&lt;/h2&gt;  &lt;p style&#x3D;\&quot;text-align: justify;\&quot;&gt;For search queries, the results are ordered by relevance score. For batch      requests, the results are retrieved in the order of the requests.&lt;/p&gt;  &lt;h2&gt;Parameters&lt;/h2&gt; &lt;p style&#x3D;\&quot;text-align: justify;\&quot;&gt;The API methods allow different parameters to be passed. Additionally, there is an API key parameter which is common to all API methods. For all API methods      the API key can be provided either as a query parameter or in the request header. If the API key      is not provided, the API will return HTTP 401 error. You can register for an API key &lt;a href&#x3D;\&quot;/services#api\&quot;&gt;here&lt;/a&gt;.&lt;/p&gt;  &lt;h2&gt;API methods&lt;/h2&gt;
    """
)

