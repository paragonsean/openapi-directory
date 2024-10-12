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
    description="Notion API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Notion API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Hello and welcome!  To make use of this API collection collection as it&#39;s written, please duplicate [this database template](https://www.notion.so/8e2c2b769e1d47d287b9ed3035d607ae?v&#x3D;dc1b92875fb94f10834ba8d36549bd2a).  [Create an integration](https://www.notion.so/my-integrations) to retrieve an API token, add your database and page ID&#39;s as variables in the collection, and start making your requests!  For our full documentation, including sample integrations and guides, visit [developers.notion.com](developers.notion.com)  Need more help? Join our [developer community on Slack](https://join.slack.com/t/notiondevs/shared_invite/zt-lkrnk74h-YmPRroySRFGiqgjI193AqA/)
    """
)

