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
    description="Amazon WorkSpaces",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon WorkSpaces"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon WorkSpaces Service&lt;/fullname&gt; &lt;p&gt;Amazon WorkSpaces enables you to provision virtual, cloud-based Microsoft Windows or Amazon Linux desktops for your users, known as &lt;i&gt;WorkSpaces&lt;/i&gt;. WorkSpaces eliminates the need to procure and deploy hardware or install complex software. You can quickly add or remove users as your needs change. Users can access their virtual desktops from multiple devices or web browsers.&lt;/p&gt; &lt;p&gt;This API Reference provides detailed information about the actions, data types, parameters, and errors of the WorkSpaces service. For more information about the supported Amazon Web Services Regions, endpoints, and service quotas of the Amazon WorkSpaces service, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/wsp.html\&quot;&gt;WorkSpaces endpoints and quotas&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can also manage your WorkSpaces resources using the WorkSpaces console, Command Line Interface (CLI), and SDKs. For more information about administering WorkSpaces, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/adminguide/\&quot;&gt;Amazon WorkSpaces Administration Guide&lt;/a&gt;. For more information about using the Amazon WorkSpaces client application or web browser to access provisioned WorkSpaces, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/workspaces/latest/userguide/\&quot;&gt;Amazon WorkSpaces User Guide&lt;/a&gt;. For more information about using the CLI to manage your WorkSpaces resources, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cli/latest/reference/workspaces/index.html\&quot;&gt;WorkSpaces section of the CLI Reference&lt;/a&gt;.&lt;/p&gt;
    """
)

