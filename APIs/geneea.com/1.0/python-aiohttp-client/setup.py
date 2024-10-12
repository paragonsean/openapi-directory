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
    description="Geneea Natural Language Processing",
    author_email="",
    url="",
    keywords=["OpenAPI", "Geneea Natural Language Processing"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;div class&#x3D;\&quot;api-description\&quot;&gt;     &lt;h2&gt;Authentication&lt;/h2&gt;     &lt;p&gt;For all calls, supply your API key. &lt;a href&#x3D;\&quot;https://www.geneea.com/pricing\&quot;&gt;Sign up to &lt;em&gt;obtain the key&lt;/em&gt;&lt;/a&gt;.&lt;/p&gt;     &lt;p&gt;         Our API supports both &lt;em&gt;unencrypted (HTTP)&lt;/em&gt; and &lt;em&gt;encrypted (HTTPS)&lt;/em&gt; protocols.         However, for security reasons, we strongly encourage using only the encrypted version.     &lt;/p&gt;     &lt;p&gt;The API key should be supplied as either a request parameter &lt;code&gt;user_key&lt;/code&gt; or in &lt;code&gt;Authorization&lt;/code&gt; header.&lt;/p&gt;     &lt;pre&gt;&lt;code&gt;Authorization: user_key &amp;lt;YOUR_API_KEY&amp;gt;&lt;/code&gt;&lt;/pre&gt;      &lt;h2&gt;API operations&lt;/h2&gt;     &lt;p&gt;         All API operations can perform analysis on supplied raw text or on text extracted from a given URL.         Optionally, one can supply additional information which can make the result more precise. An example         of such information would be the language of text or a particular text extractor for URL resources.     &lt;/p&gt;     &lt;p&gt;The supported types of analyses are:&lt;/p&gt;     &lt;ul&gt;         &lt;li&gt;&lt;strong&gt;lemmatization&lt;/strong&gt; &amp;longrightarrow;             Finds out lemmata (basic forms) of all the words in the document.         &lt;/li&gt;         &lt;li&gt;&lt;strong&gt;correction&lt;/strong&gt; &amp;longrightarrow;             Performs correction (diacritization) on all the words in the document.         &lt;/li&gt;         &lt;li&gt;&lt;strong&gt;topic detection&lt;/strong&gt; &amp;longrightarrow;             Determines a topic of the document, e.g. finance or sports.         &lt;/li&gt;         &lt;li&gt;&lt;strong&gt;sentiment analysis&lt;/strong&gt; &amp;longrightarrow;             Determines a sentiment of the document, i.e. how positive or negative the document is.         &lt;/li&gt;         &lt;li&gt;&lt;strong&gt;named entity recognition&lt;/strong&gt; &amp;longrightarrow;             Finds named entities (like person, location, date etc.) mentioned the the document.         &lt;/li&gt;     &lt;/ul&gt;      &lt;h2&gt;Encoding&lt;/h2&gt;     &lt;p&gt;The supplied text is expected to be in UTF-8 encoding, this is especially important for non-english texts.&lt;/p&gt;      &lt;h2&gt;Returned values&lt;/h2&gt;     &lt;p&gt;The API calls always return objects in serialized JSON format in UTF-8 encoding.&lt;/p&gt;     &lt;p&gt;         If any error occurs, the HTTP response code will be in the range &lt;code&gt;4xx&lt;/code&gt; (client-side error) or         &lt;code&gt;5xx&lt;/code&gt; (server-side error). In this situation, the body of the response will contain information         about the error in JSON format, with &lt;code&gt;exception&lt;/code&gt; and &lt;code&gt;message&lt;/code&gt; values.     &lt;/p&gt;      &lt;h2&gt;URL limitations&lt;/h2&gt;     &lt;p&gt;         All the requests are semantically &lt;code&gt;GET&lt;/code&gt;. However, for longer texts, you may run into issues         with URL length limit. Therefore, it&#39;s possible to always issue a &lt;code&gt;POST&lt;/code&gt; request with all         the parameters encoded as a JSON in the request body.     &lt;/p&gt;     &lt;p&gt;Example:&lt;/p&gt;     &lt;pre&gt;&lt;code&gt;         POST /s1/sentiment         Content-Type: application/json          {\&quot;text\&quot;:\&quot;There is no harm in being sometimes wrong - especially if one is promptly found out.\&quot;}     &lt;/code&gt;&lt;/pre&gt;     &lt;p&gt;This is equivalent to &lt;code&gt;GET /s1/sentiment?text&#x3D;There%20is%20no%20harm...&lt;/code&gt;&lt;/p&gt;      &lt;h2&gt;Request limitations&lt;/h2&gt;     &lt;p&gt;         The API has other limitations concerning the size of the HTTP requests. The maximum allowed size of any         POST request body is &lt;em&gt;512 KiB&lt;/em&gt;. For request with a URL resource, the maximum allowed number of         extracted characters from each such resource is &lt;em&gt;100,000&lt;/em&gt;.     &lt;/p&gt;      &lt;h2&gt;Terms of Service&lt;/h2&gt;     &lt;p&gt;         By using the API, you agree to our         &lt;a href&#x3D;\&quot;https://www.geneea.com/terms.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Terms of Service Agreement&lt;/a&gt;.     &lt;/p&gt;      &lt;h2&gt;More information&lt;/h2&gt;     &lt;p&gt;         &lt;a href&#x3D;\&quot;https://help.geneea.com/index.html\&quot; target&#x3D;\&quot;_blank\&quot;&gt;         The Interpretor Public Documentation         &lt;/a&gt;     &lt;/p&gt; &lt;/div&gt; 
    """
)

