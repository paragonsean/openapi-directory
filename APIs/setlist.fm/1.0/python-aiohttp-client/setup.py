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
    description="setlist.fm API",
    author_email="",
    url="",
    keywords=["OpenAPI", "setlist.fm API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt; The setlist.fm API has been designed to give you easy access to setlist data in order to build fancy websites and other applications. Before starting to use the API, be sure to ... &lt;ol&gt; &lt;li&gt;... understand how setlist.fm works (the &lt;a href&#x3D;\&quot;https://www.setlist.fm/faq\&quot;&gt;FAQ&lt;/a&gt; and the &lt;a href&#x3D;\&quot;https://www.setlist.fm/guidelines\&quot;&gt;Guidelines&lt;/a&gt; are a good starting point),&lt;/li&gt; &lt;li&gt;... read this documentation carefully and&lt;/li&gt; &lt;li&gt;... &lt;a href&#x3D;\&quot;https://www.setlist.fm/settings/api\&quot;&gt;apply for an API key&lt;/a&gt; (link for logged in users only) - if you&#39;re no registered user yet, then &lt;a href&#x3D;\&quot;https://www.setlist.fm/signup\&quot;&gt;register first&lt;/a&gt; (it&#39;s free).&lt;/li&gt; &lt;/ol&gt; &lt;/p&gt; &lt;p&gt; If this documentation isn&#39;t enough or if you&#39;ve got other things you&#39;d like to tell us about the API, visit the &lt;a href&#x3D;\&quot;https://www.setlist.fm/forum/setlistfm/setlistfm-api\&quot;&gt;API Forum&lt;/a&gt;. &lt;/p&gt; &lt;p&gt; Note that the setlist.fm API is, according to the &lt;a href&#x3D;\&quot;https://www.setlist.fm/help/api-terms\&quot;&gt;API terms of service&lt;/a&gt;, only free for non-commercial projects. If you&#39;re interested in using the API for commercial purposes, &lt;a href&#x3D;\&quot;https://www.setlist.fm/contact\&quot;&gt;contact us&lt;/a&gt;. &lt;/p&gt;  &lt;h2&gt;About this Service&lt;/h2&gt; &lt;p&gt; This service provides methods to get both setlists and components of setlists such as artists, cities, countries or venues. &lt;/p&gt;  &lt;h2&gt;Supported Content Types&lt;/h2&gt; &lt;p&gt; The REST service currently supports XML (default) and JSON content. &lt;/p&gt; &lt;p&gt; To receive a JSON response, set the &lt;code&gt;Accept&lt;/code&gt; &lt;a href&#x3D;\&quot;https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.1\&quot;&gt;header&lt;/a&gt; to &lt;em&gt;application/json&lt;/em&gt;. &lt;/p&gt;  &lt;h2&gt;Internationalization&lt;/h2&gt; &lt;p&gt; &lt;small&gt;(Please note that this is an experimental feature and does not work for all cities!)&lt;/small&gt; &lt;/p&gt; &lt;p&gt; Most of the featured methods honor the &lt;code&gt;Accept-Language&lt;/code&gt; &lt;a href&#x3D;\&quot;https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4\&quot;&gt;header&lt;/a&gt;. This header is used for localizing cities and countries. The default language is English (en), but you can provide any of the languages Spanish (es), French (fr), German (de), Portuguese (pt), Turkish (tr), Italian (it) or Polish (pl). &lt;/p&gt; &lt;p&gt; E.g. if you search a setlist for a concert that took place in Vienna and you pass &amp;quot;de&amp;quot; as header, you&#39;ll get &lt;em&gt;&amp;quot;Wien, &amp;Ouml;sterreich&amp;quot;&lt;/em&gt; instead of &lt;em&gt;&amp;quot;Vienna, Austria&amp;quot;&lt;/em&gt;.&lt;br/&gt; This also works if you use a different language than the country&#39;s native language. &lt;/p&gt; &lt;p&gt; E.g. for a concert in New York, you&#39;ll get &lt;em&gt;&amp;quot;Nueva York, Estados Unidos&amp;quot;&lt;/em&gt; instead of &lt;em&gt;&amp;quot;New York, United States&amp;quot;&lt;/em&gt; if you pass &amp;quot;es&amp;quot; as language. &lt;/p&gt;  &lt;h2&gt;API Keys&lt;/h2&gt;  API keys (&lt;a href&#x3D;\&quot;https://www.setlist.fm/settings/api\&quot;&gt;application form&lt;/a&gt;) must be included in the request with the &lt;code&gt;x-api-key&lt;/code&gt; header.  &lt;h2&gt;Version History&lt;/h2&gt; &lt;table class&#x3D;\&quot;table table-bordered table-versions\&quot;&gt; &lt;thead&gt; &lt;tr&gt; &lt;th&gt;Version&lt;/th&gt; &lt;th&gt;Docs&lt;/th&gt; &lt;th&gt;End of Service&lt;/th&gt; &lt;/tr&gt; &lt;/thead&gt; &lt;tbody&gt; &lt;tr&gt; &lt;td&gt;&lt;strong&gt;1.0&lt;/strong&gt;&lt;/td&gt; &lt;td&gt;&lt;a href&#x3D;\&quot;/docs/1.0\&quot;&gt;Docs&lt;/a&gt;&lt;/td&gt; &lt;td&gt;-&lt;/li&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td&gt;&lt;strong&gt;0.1&lt;/strong&gt;&lt;/td&gt; &lt;td&gt;&lt;/td&gt; &lt;td&gt;December 31, 2017&lt;/li&gt; &lt;/tr&gt; &lt;/tbody&gt; &lt;/table&gt;
    """
)

