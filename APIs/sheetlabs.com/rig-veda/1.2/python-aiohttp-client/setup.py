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
    description="rv API",
    author_email="ab.techwriter@gmail.com",
    url="",
    keywords=["OpenAPI", "rv API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    # Introduction This API returns information about all of the verses in Rig Veda. The results are JSON objects that contain the name of the god, poet, and meter of the verses in Rig Veda, the category of the god and the poet, and the _mandal_ and _sukta_ number.  The API uses the Swagger 2.0 specification.  # Authentication This is an open API.  # Try it out This sandbox can be used to get data for only one kind of resource, that is, to fetch the data for a category being sung to.  The remaining resources work a similar fashion. For details, see the reference documentation. 
    """
)

