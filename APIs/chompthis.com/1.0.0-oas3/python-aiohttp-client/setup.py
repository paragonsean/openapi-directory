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
    description="Chomp Food Database API Documentation",
    author_email="",
    url="",
    keywords=["OpenAPI", "Chomp Food Database API Documentation"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    ## Important An **[API key](https://chompthis.com/api/)** is required for access to this API. Get yours at **[https://chompthis.com/api](https://chompthis.com/api/)**.  ### Getting Started   * **[Subscribe](https://chompthis.com/api/#pricing)** to the API.   * Scroll down and click the \&quot;**Authorize**\&quot; button.   * Enter your API key into the \&quot;**value**\&quot; input, click the \&quot;**Authorize**\&quot; button, then click the \&quot;**Close**\&quot; button.   * Scroll down to the section titled \&quot;**default**\&quot; and click on the API endpoint you wish to use.   * Click the \&quot;**Try it out**\&quot; button.   * Enter the information the endpoint requires.   * Click the \&quot;**Execute**\&quot; button.  ### Example    * Branded food response object: **[View example &amp;raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/branded-food-response-object.json)**   * Ingredient response object: **[View example &amp;raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/ingredient-response-object.json)**   * Error response object: **[View example &amp;raquo;](https://raw.githubusercontent.com/chompfoods/examples/master/error-response-object.json)**  ### How Do I Find My API Key?   * Your API key was sent to the email address you used to create your subscription.   * You will also find your API key in the **[Client Center](https://chompthis.com/api/manage.php)**.   * Read **[this article](https://desk.zoho.com/portal/chompthis/kb/articles/how-do-i-find-my-api-key)** for more information.  ### Helpful Links   * **Help &amp; Support**     * [Knowledge Base &amp;raquo;](https://desk.zoho.com/portal/chompthis/kb/chomp)     * [Support &amp;raquo;](https://chompthis.com/api/ticket-new.php)     * [Client Center &amp;raquo;](https://chompthis.com/api/manage.php)   * **Pricing**     * [Subscription Options &amp;raquo;](https://chompthis.com/api/)     * [Cost Calculator &amp;raquo;](https://chompthis.com/api/cost-calculator.php)   * **Guidelines**     * [Terms &amp; License &amp;raquo;](https://chompthis.com/api/terms.php)     * [Attribution &amp;raquo;](https://chompthis.com/api/docs/attribution.php) 
    """
)

