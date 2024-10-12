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
    description="LanguageTool API",
    author_email="",
    url="",
    keywords=["OpenAPI", "LanguageTool API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Check texts for style and grammar issues with &lt;a href&#x3D;&#39;https://languagetool.org&#39;&gt;LanguageTool&lt;/a&gt;. Please consider the following default limitations:&lt;ul&gt;&lt;li&gt;your daily request limit depending on &lt;a href&#x3D;&#39;https://languagetool.org/editor/settings/access-tokens&#39;&gt;your plan&lt;/a&gt; &lt;li&gt;maximum number of requests per minute: 20 (free) / 80 (Premium) &lt;li&gt;maximum number of characters per minute: 75,000 (free) / 300,000 (Premium) &lt;li&gt;maximum number of characters per request: 20,000 (free) / 60,000 (Premium) &lt;li&gt;for the free version, also consider the &lt;a href&#x3D;&#39;https://dev.languagetool.org/public-http-api&#39;&gt;limitations documented here&lt;/a&gt; &lt;li&gt;&lt;b&gt;Note:&lt;/b&gt; any parameters or outputs not part of this documentation are internal and must not be relied on&lt;/ul&gt; Need more generous limits? Just &lt;a href&#x3D;&#39;https://languagetool.org/proofreading-api&#39;&gt;contact us&lt;/a&gt;.
    """
)

