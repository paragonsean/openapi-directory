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
    description="ODN API",
    author_email="",
    url="",
    keywords=["OpenAPI", "ODN API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Socrata OpenDataNetwork (ODN) REST API exposes public data, often continuosly updated and enhanced, from many thousands of public government and non profit agencies.  Much of this data originating from independent sources is fused together to create new, and often powerful, entity level data. The API, in addition to search and autosuggest capabilities for finding datasets, enables data based comparisons across geographical regions such as states, counties, metropolitan areas, cities and zip codes using highly vetted data providers such as US Census, BEA, HUD and others. Comparison data is preformatted for easy and efficient display on a chart, graph or interactive map.  The API also exposes data organized by narrative style questions a human might ask. The questions can be rapidly found using an autosuggest style index, and then used to directly access all data needed to thoroughly and authoritatively answer the question. Retrieved data includes time series (temporally aligned), tabular, map heavy (includes spatial boundaries), and auto generated unstructured descriptive text.  The ODN API does not duplicate API endpoints or services provided by public sector agencies, but rather, returns context relevant pre-populated REST URLs, when appropriate, so the caller can access data directly from the source.  The [open source](http://github.com/socrata/odn-backend) API powers [OpenDataNetwork.com](http://OpenDataNetwork.com), an [open source](http://github.com/socrata/opendatanetwork.com) site; the site highlights myriad uses and provides API badges with contextually relevant API example REST endpoints and documentation pointers.  Finally, we continuously add new dat sources which appear automatically in the API, so if your favorite data source is not available, check back soon. You can also join us [HERE](http://www.opendatanetwork.com/join-open-data-network) and receive updates or let us know which data sources you are most interested in.  ## App Tokens  Registering for and including a [Socrata application token](https://dev.socrata.com/docs/app-tokens.html) is _required_ for the ODN API. They can be passed either using the &#x60;app_token&#x60; parameter or the &#x60;X-App-Token&#x60; HTTP header.
    """
)

