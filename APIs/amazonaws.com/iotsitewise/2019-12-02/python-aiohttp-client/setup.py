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
    description="AWS IoT SiteWise",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS IoT SiteWise"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Welcome to the IoT SiteWise API Reference. IoT SiteWise is an Amazon Web Services service that connects &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/Internet_of_things#Industrial_applications\&quot;&gt;Industrial Internet of Things (IIoT)&lt;/a&gt; devices to the power of the Amazon Web Services Cloud. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/\&quot;&gt;IoT SiteWise User Guide&lt;/a&gt;. For information about IoT SiteWise quotas, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html\&quot;&gt;Quotas&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.
    """
)

