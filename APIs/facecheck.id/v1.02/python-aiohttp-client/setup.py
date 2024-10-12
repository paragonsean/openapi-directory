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
    description="Facial Recognition Reverse Image Face Search API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Facial Recognition Reverse Image Face Search API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Let your users search the Internet by face! Integrate FaceCheck facial search seamlessly with your app, website or software platform.   FaceCheck&#39;s REST API is hassle-free and easy to use. For code examples visit &lt;a href&#x3D;&#39;https://facecheck.id/Face-Search/API&#39;&gt;https://facecheck.id/Face-Search/API&lt;/a&gt;
    """
)

