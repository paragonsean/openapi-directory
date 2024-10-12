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
    description="Policy Simulator API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Policy Simulator API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
     Policy Simulator is a collection of endpoints for creating, running, and viewing a Replay. A &#x60;Replay&#x60; is a type of simulation that lets you see how your members&#39; access to resources might change if you changed your IAM policy. During a &#x60;Replay&#x60;, Policy Simulator re-evaluates, or replays, past access attempts under both the current policy and your proposed policy, and compares those results to determine how your members&#39; access might change under the proposed policy.
    """
)

