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
    description="Api2Pdf - PDF Generation, Powered by AWS Lambda",
    author_email="support@api2pdf.com",
    url="",
    keywords=["OpenAPI", "Api2Pdf - PDF Generation, Powered by AWS Lambda"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
     # Introduction [Api2Pdf](https://www.api2pdf.com) is a powerful PDF generation API with no rate limits or file size constraints. Api2Pdf runs on AWS Lambda, a serverless architecture powered by Amazon to scale to millions of requests while being up to 90% cheaper than alternatives. **Supports wkhtmltopdf, Headless Chrome, LibreOffice, and PDF Merge.** You can also generate barcodes with ZXING (Zebra Crossing). # SDKs &amp; Client Libraries We&#39;ve made a number of open source libraries available for the API - Python: [https://github.com/api2pdf/api2pdf.python](https://github.com/api2pdf/api2pdf.python) - .NET: [https://github.com/api2pdf/api2pdf.dotnet](https://github.com/api2pdf/api2pdf.dotnet) - Nodejs: [https://github.com/api2pdf/api2pdf.node](https://github.com/api2pdf/api2pdf.node) - PHP: [https://github.com/Api2Pdf/api2pdf.php](https://github.com/Api2Pdf/api2pdf.php) - Ruby: (Coming soon) # Authorization Create an account at [portal.api2pdf.com](https://portal.api2pdf.com/register) to get an API key.  **Authorize your API calls** - GET requests, include apikey&#x3D;YOUR-API-KEY as a query string parameter - POST requests, add **Authorization** to your header. &#x60;&#x60;&#x60; Authorization: YOUR-API-KEY &#x60;&#x60;&#x60;  # Quickstart If you are looking for just a quick call to grab PDFs of a URL, you can do a GET request like: &#x60;&#x60;&#x60; https://v2018.api2pdf.com/chrome/url?url&#x3D;{UrlToConvert}&amp;apikey&#x3D;{YourApiKey} &#x60;&#x60;&#x60;  For more advanced usage and settings, see the API specification below. 
    """
)

