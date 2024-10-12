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
    description="Alerter System API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Alerter System API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;This is the &lt;a href&#x3D;\&quot;/\&quot;&gt;Alerter System&lt;/a&gt; API playground. More documentation is available at the &lt;a href&#x3D;\&quot;/help/developers/\&quot;&gt;API Help Center&lt;/a&gt;.&lt;/p&gt;&lt;p&gt;The \&quot;Available Authorizations\&quot; in the Authorize popup only applies to this playground web interface. Other &lt;a href&#x3D;\&quot;/help/developers/authorization/\&quot;&gt;authorizations&lt;/a&gt; are available for the actual API.&lt;/p&gt;
    """
)

