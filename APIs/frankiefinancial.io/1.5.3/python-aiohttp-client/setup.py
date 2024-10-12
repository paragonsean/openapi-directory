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
    description="Frankie Financial API",
    author_email="dev-support@frankiefinancial.com",
    url="",
    keywords=["OpenAPI", "Frankie Financial API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    ------   This API allows developers to integrate the Frankie Financial Compliance Utility into their applications. The API allows:   - Checking name, address, date of birth against national databases   - Validating Australian driver&#39;s licences, passports, medicare, visas and other Australian national ID documents   - Validating Australian electricity bills   - Validating NZ driver&#39;s licences   - Validating Chinese bank cards and national ID card   - Validating International passports and national ID documents   - PEP, Sanctions, Watchlist and adverse media checking   - Australian visa checks    - Fraud list and fraud background checks   - ID validation and selfie check comparisons.    ------     Industry specific services    - Comparing Australian electricity retailers for a better deal.  ------     KYB specific services    - Query organisation ownership   - Perform KYC &amp; AML checks on shareholders, beneficial owners and office bearers.   - Query credit score and credit reports   - International company searches   - International company profiles    ------   The full version of this documentation along with supplemental articles can be found here:   - https://apidocs.frankiefinancial.com/  The traditional Swagger view of this documentation can be found here:   - https://app.swaggerhub.com/apis-docs/FrankieFinancial/kycutility  ------   Sandbox base URL is:   - https://api.demo.frankiefinancial.io/compliance/v1.2      - We do have an old sandbox at https://sandbox.frankiefinancial.com/compliance/v1.2 but this has been retired.    - All calls are the same as production, only with canned data.     - Full Swagger definition, along with test data for playing in the sandbox can be obtained once initial commercial discussions have commenced.    - Production and optional UAT access will be opened up only to those with a signed commercial contract.    ------   Contact us at hello@frankiefinancial.com to speak with a sales rep about issuing a Customer ID and Sandbox api key. 
    """
)

