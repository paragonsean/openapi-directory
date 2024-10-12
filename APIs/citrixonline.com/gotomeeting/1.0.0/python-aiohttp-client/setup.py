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
    description="GoToMeeting",
    author_email="developer-support@citrixonline.com",
    url="",
    keywords=["OpenAPI", "GoToMeeting"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;br&gt;The GoToMeeting API provides seamless integration of GoToMeeting provisioning and meeting management into your existing infrastructure or third party applications.&lt;br&gt;&lt;br&gt;For customers, the ability to add, suspend or delete an organizer in your GoToMeeting Corporate account from within your primary management systems simplifies and streamlines the entire process of account management. The ability to monitor meeting schedules, history and active meeting status allows managers to leverage GoToMeeting activities through your primary applications.&lt;br&gt;&lt;br&gt;For third parties, the ability to create, update or delete a meeting from within your application makes real-time collaboration possible for your customers. The ability to update meeting schedules, view history and scheduled meetings, and view attendees from past meetings allows you to enhance your users&#39; experience and the value of your applications.
    """
)

