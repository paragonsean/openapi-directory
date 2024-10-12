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
    description="Amazon QLDB Session",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon QLDB Session"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;The transactional data APIs for Amazon QLDB&lt;/p&gt; &lt;note&gt; &lt;p&gt;Instead of interacting directly with this API, we recommend using the QLDB driver or the QLDB shell to execute data transactions on a ledger.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you are working with an AWS SDK, use the QLDB driver. The driver provides a high-level abstraction layer above this &lt;i&gt;QLDB Session&lt;/i&gt; data plane and manages &lt;code&gt;SendCommand&lt;/code&gt; API calls for you. For information and a list of supported programming languages, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/qldb/latest/developerguide/getting-started-driver.html\&quot;&gt;Getting started with the driver&lt;/a&gt; in the &lt;i&gt;Amazon QLDB Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you are working with the AWS Command Line Interface (AWS CLI), use the QLDB shell. The shell is a command line interface that uses the QLDB driver to interact with a ledger. For information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/qldb/latest/developerguide/data-shell.html\&quot;&gt;Accessing Amazon QLDB using the QLDB shell&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;
    """
)

