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
    description="AWS AppConfig Data",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS AppConfig Data"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;AppConfig Data provides the data plane APIs your application uses to retrieve configuration data. Here&#39;s how it works:&lt;/p&gt; &lt;p&gt;Your application retrieves configuration data by first establishing a configuration session using the AppConfig Data &lt;a&gt;StartConfigurationSession&lt;/a&gt; API action. Your session&#39;s client then makes periodic calls to &lt;a&gt;GetLatestConfiguration&lt;/a&gt; to check for and retrieve the latest data available.&lt;/p&gt; &lt;p&gt;When calling &lt;code&gt;StartConfigurationSession&lt;/code&gt;, your code sends the following information:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Identifiers (ID or name) of an AppConfig application, environment, and configuration profile that the session tracks.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;(Optional) The minimum amount of time the session&#39;s client must wait between calls to &lt;code&gt;GetLatestConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;In response, AppConfig provides an &lt;code&gt;InitialConfigurationToken&lt;/code&gt; to be given to the session&#39;s client and used the first time it calls &lt;code&gt;GetLatestConfiguration&lt;/code&gt; for that session.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This token should only be used once in your first call to &lt;code&gt;GetLatestConfiguration&lt;/code&gt;. You &lt;i&gt;must&lt;/i&gt; use the new token in the &lt;code&gt;GetLatestConfiguration&lt;/code&gt; response (&lt;code&gt;NextPollConfigurationToken&lt;/code&gt;) in each subsequent call to &lt;code&gt;GetLatestConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;When calling &lt;code&gt;GetLatestConfiguration&lt;/code&gt;, your client code sends the most recent &lt;code&gt;ConfigurationToken&lt;/code&gt; value it has and receives in response:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;NextPollConfigurationToken&lt;/code&gt;: the &lt;code&gt;ConfigurationToken&lt;/code&gt; value to use on the next call to &lt;code&gt;GetLatestConfiguration&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;NextPollIntervalInSeconds&lt;/code&gt;: the duration the client should wait before making its next call to &lt;code&gt;GetLatestConfiguration&lt;/code&gt;. This duration may vary over the course of the session, so it should be used instead of the value sent on the &lt;code&gt;StartConfigurationSession&lt;/code&gt; call.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The configuration: the latest data intended for the session. This may be empty if the client already has the latest version of the configuration.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;The &lt;code&gt;InitialConfigurationToken&lt;/code&gt; and &lt;code&gt;NextPollConfigurationToken&lt;/code&gt; should only be used once. To support long poll use cases, the tokens are valid for up to 24 hours. If a &lt;code&gt;GetLatestConfiguration&lt;/code&gt; call uses an expired token, the system returns &lt;code&gt;BadRequestException&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information and to view example CLI commands that show how to retrieve a configuration using the AppConfig Data &lt;code&gt;StartConfigurationSession&lt;/code&gt; and &lt;code&gt;GetLatestConfiguration&lt;/code&gt; API actions, see &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration\&quot;&gt;Retrieving the configuration&lt;/a&gt; in the &lt;i&gt;AppConfig User Guide&lt;/i&gt;.&lt;/p&gt;
    """
)

