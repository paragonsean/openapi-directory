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
    description="Amazon Simple Workflow Service",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Simple Workflow Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon Simple Workflow Service&lt;/fullname&gt; &lt;p&gt;The Amazon Simple Workflow Service (Amazon SWF) makes it easy to build applications that use Amazon&#39;s cloud to coordinate work across distributed components. In Amazon SWF, a &lt;i&gt;task&lt;/i&gt; represents a logical unit of work that is performed by a component of your workflow. Coordinating tasks in a workflow involves managing intertask dependencies, scheduling, and concurrency in accordance with the logical flow of the application.&lt;/p&gt; &lt;p&gt;Amazon SWF gives you full control over implementing tasks and coordinating them without worrying about underlying complexities such as tracking their progress and maintaining their state.&lt;/p&gt; &lt;p&gt;This documentation serves as reference only. For a broader overview of the Amazon SWF programming model, see the &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amazonswf/latest/developerguide/\&quot;&gt;Amazon SWF Developer Guide&lt;/a&gt; &lt;/i&gt;.&lt;/p&gt;
    """
)

