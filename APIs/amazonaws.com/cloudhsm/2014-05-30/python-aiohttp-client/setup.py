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
    description="Amazon CloudHSM",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon CloudHSM"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;AWS CloudHSM Service&lt;/fullname&gt; &lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt;
    """
)

