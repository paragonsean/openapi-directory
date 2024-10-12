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
    description="SwaggerHub Registry API",
    author_email="",
    url="",
    keywords=["OpenAPI", "SwaggerHub Registry API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    # Overview Use SwaggerHub Registry API to access, manage, and update the following resources in SwaggerHub, bypassing the web interface:   * APIs   * Domains   * Integrations   * Projects   * Templates   SwaggerHub also provides the [User Management API](https://app.swaggerhub.com/apis-docs/swagger-hub/user-management-api/) to get information about organizations and manage organization members.  # Base URL Use the following base URL for SwaggerHub SaaS:          http(s)://api.swaggerhub.com  **Note:** This documentation is for SwaggerHub SaaS. On-Premise customers should use the bundled API definition, which can be found at the URLs provided below.  Version 1.29.0 or later:      http(s)://SERVER/v1/openapi.yaml - YAML version     http(s)://SERVER/v1/openapi.json - JSON version  Earlier versions:      http(s)://SERVER/v1/swagger.yaml - YAML version     http(s)://SERVER/v1/swagger.json - JSON version  # Authentication Operations that update data or access private data require authentication using an API key. You can find your personal API key on the [API Keys](https://app.swaggerhub.com/settings/apiKey) page in your account settings. Send this key in the &#x60;Authorization&#x60; header when making requests to the Registry API:      Authorization: YOUR_API_KEY  To test API calls from this documentation page, click the **Authorize** button below and paste your API key there.  **Important:** Keep the API key secure and do not store it directly in your code. # Tools In addition to calling the Registry API directly, you can use the following tools to interact with the API from the command line or CI/CD pipeline:   * [SwaggerHub CLI](https://www.npmjs.com/package/swaggerhub-cli)   * [Maven plugin](https://github.com/swagger-api/swaggerhub-maven-plugin)  * [Gradle plugin](https://github.com/swagger-api/swaggerhub-gradle-plugin) 
    """
)

