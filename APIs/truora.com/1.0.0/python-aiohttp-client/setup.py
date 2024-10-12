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
    description="Checks API",
    author_email="api@truora.com",
    url="",
    keywords=["OpenAPI", "Checks API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    **NOTE:** This is a preview of the API and it is not considered stable since refinements are still being made.  # Introduction  Welcome to the  **Truora Check** [**RESTful API**](https://en.wikipedia.org/wiki/Representational_state_transfer) reference. You may also want to check out our [**Validations API docs**](https://docs.validations.truora.com/) or our [**Signals API docs**](https://docs.signals.truora.com/).  Truora Check API allows performing full background checks on people, vehicles and companies. There are three main types of background checks:  - **Personal background check**: Verifies national IDs in multiple databases of public and legal entities in the LATAM region. For every national ID, returns information on: personal identity, criminal records, international background check, and professional background.  - **Vehicle background check**: Verifies the vehicle documents and the owner identity in multiple databases of public and legal entities in the LATAM region. For every vehicle and owner type, returns information on: personal identity, driving records, criminal records, and vehicle information.    - **Company background check**: Verifies the tax ID or a company name in multiple databases of public and legal entities in the LATAM region. For every company, returns the associated: business status, legal and criminal records, and media reports.  # API Key V1 is live!  API key version 1 is now live. Users with version 0 API keys are not immediately required to upgrade to V1 but should plan to do so at their earliest convenience. The changes for integration with API keys v1 are as follows:  - The field &#x60;&#x60;user_authorized&#x60;&#x60; is now required to perform person checks. This field indicates the API user has authorization to perform the check in compliance with data protection law. - The field &#x60;&#x60;homonym_scores&#x60;&#x60; is no longer included in our person check response as its results are already included in the body of the check and keeping them duplicated is generating unnecessary confusion.   # API composition  ## Endpoints  - **Check endpoints**: Provide an easy way to create and search for a background check. They also allow inserting groups of checks into reports. Each check contains scores, datasets and databases.   &#x60;&#x60;&#x60;plain https://api.truora.com/v1/checks &#x60;&#x60;&#x60;  - **Report endpoints**: Support batch uploads and grouping multiple checks together. Excel and .csv files are supported for batch uploads.   &#x60;&#x60;&#x60;plain https://api.truora.com/v1/reports &#x60;&#x60;&#x60;  - **Configuration endpoints**: Allows personalizing data sets and scores for customized background checks.  &#x60;&#x60;&#x60;plain https://api.truora.com/v1/config &#x60;&#x60;&#x60;  - **Continuous check endpoints**: Allows creating recurring checks and get notified whenever a change in the check score occurs.  &#x60;&#x60;&#x60;plain https://api.truora.com/v1/continuous_checks &#x60;&#x60;&#x60;  - **Behavior endpoints**: Allows sharing anonymous feedback about a person behavior when interacting with the company.  &#x60;&#x60;&#x60;plain https://api.truora.com/v1/behaviour &#x60;&#x60;&#x60;  - **Hooks endpoints**: Allows sending notifications via requests to your service or another third-party service whenever certain events occur.  &#x60;&#x60;&#x60;plain https://api.truora.com/v1/hooks &#x60;&#x60;&#x60;  ## Datasets  Categories that group the resulting information for background checks from databases are called datasets. Datasets are divided in:  - **Personal identity**: Corroborates the existence and validates personal identity documents.   - **Criminal record**: Checks for crimes according to each country penal code or criminal code. Keep in mind that data aged less than 10 years is usually more consistent.  - **Legal background**: Checks for lawsuits filed. Keep in mind that data aged less than 10 years is usually more consistent.  - **International background**: Checks international lists for crimes related to identity theft, money laundering, terrorist financing, and high crimes.  - **Professional background**: Checks professional regulatory entities for relevant information.  - **Affiliations and insurances**: Checks the history and status of social security affiliations.  - **Alert in media**: Checks major media agencies for relevant news related to violent actions.      - **Vehicle information**: Checks for the physical characteristics of the vehicle, technical status, insurance history, and other relevant information.  - **Traffic fines**: Checks for outstanding traffic fines.  - **Driving licenses**: Shows information relevant to the driver. Such as license status and driver certificates.  - **Business background**: Checks for business status, legal and criminal history, and other relevant information.  - **Taxes and Finances**: Checks for the information related to personal finances, liabilities, and taxes.  ## Requests Format  The POST requests receive a body that must be encoded in &#x60;www-x-form-urlencoded&#x60;, for instance:  &#x60;&#x60;&#x60;plain type&#x3D;person&amp;national_id&#x3D;123456&amp;country&#x3D;CO &#x60;&#x60;&#x60;  The responses are always encoded in &#x60;JSON&#x60; format.  ## Errors  Whenever there is an error, a JSON with the following format is returned:  &#x60;&#x60;&#x60;json {     \&quot;code\&quot;: &lt;Truora error code&gt;,     \&quot;http_code\&quot;: &lt;The HTTP status of the response&gt;,     \&quot;message\&quot;: &lt;The error message&gt; } &#x60;&#x60;&#x60;  for instance:  &#x60;&#x60;&#x60;json {     \&quot;code\&quot;: 10404,     \&quot;http_code\&quot;: 404,     \&quot;message\&quot;: \&quot;The Check was not found\&quot; } &#x60;&#x60;&#x60;  ## SDKs  If your favorite language was not on the next list, You can use our [OpenAPI 3 spec](https://docs.truora.com/openapi.json) to generate it using the [Open API Generator](https://openapi-generator.tech/docs/installation).  To download the SDK click on the desired programming language:  - [C# .Net Core](https://truora-sdk.s3.amazonaws.com/checks/checks_csharp-netcore_latest.zip)  - [Elixir](https://truora-sdk.s3.amazonaws.com/checks/checks_elixir_latest.zip)  - [Go](https://truora-sdk.s3.amazonaws.com/checks/checks_go_latest.zip)  - [Java](https://truora-sdk.s3.amazonaws.com/checks/checks_java_latest.zip)  - [JavaScript](https://truora-sdk.s3.amazonaws.com/checks/checks_javascript_latest.zip)  - [Objc](https://truora-sdk.s3.amazonaws.com/checks/checks_objc_latest.zip)  - [Php](https://truora-sdk.s3.amazonaws.com/checks/checks_php_latest.zip)  - [Python](https://truora-sdk.s3.amazonaws.com/checks/checks_python_latest.zip)  - [Ruby](https://truora-sdk.s3.amazonaws.com/checks/checks_ruby_latest.zip)  You can see the full list of supported platforms here:  https://openapi-generator.tech/docs/generators   
    """
)

