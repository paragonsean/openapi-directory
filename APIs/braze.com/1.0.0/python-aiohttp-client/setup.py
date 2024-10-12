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
    description="Braze Endpoints",
    author_email="",
    url="",
    keywords=["OpenAPI", "Braze Endpoints"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    # Braze API Overview  Braze provides a high performance REST API to allow you to track users, send messages, export data, and more.  A REST API is a way to programmatically transfer information over the web using a predefined schema. Braze has created many different endpoints with specific requirements that will perform various actions and/or return various data. API access is done using HTTPS web requests to your company&#39;s REST API endpoint (this will correspond to your Dashboard URL as shown in the table below).  Customers using Braze&#39;s EU database should use &#x60;https://rest.fra-01.braze.eu/&#x60;. For more information on REST API endpoints for customers using Braze&#39;s EU database see our [EU/US Implementation Differences documentation](https://www.braze.com/docs/developer_guide/eu01_us3_sdk_implementation_differences/overview/).  ## Braze Instances  Instance    | Dashboard URL   | REST Endpoint ----------- |---------------- | -------------------- US-01 | &#x60;https://dashboard.braze.com&#x60; or&lt;br&gt; &#x60;https://dashboard-01.braze.com&#x60; | &#x60;https://rest.iad-01.braze.com&#x60; US-02 | &#x60;https://dashboard-02.braze.com&#x60; | &#x60;https://rest.iad-02.braze.com&#x60; US-03 | &#x60;https://dashboard-03.braze.com&#x60; | &#x60;https://rest.iad-03.braze.com&#x60; US-04 | &#x60;https://dashboard-04.braze.com&#x60; | &#x60;https://rest.iad-04.braze.com&#x60; US-06 | &#x60;https://dashboard-06.braze.com&#x60; | &#x60;https://rest.iad-06.braze.com&#x60; EU-01 | &#x60;https://dashboard.braze.eu&#x60; or&lt;br&gt; &#x60;https://dashboard-01.braze.eu&#x60; | &#x60;https://rest.fra-01.braze.eu&#x60;   # Using Braze&#39;s Postman Collection   If you have a Postman account (MacOS, Windows, and Linux versions can be downloaded from their website located [here](https://www.getpostman.com)), you can go to our Postman documentation and click the orange &#x60;Run in Postman&#x60; button in the top, right corner. This will allow you to [create an environment](#setting-up-your-postman-environment), as well as edit the available &#x60;POST&#x60; and &#x60;GET&#x60; requests to suit your own needs.  ## Setting Up Your Postman Environment  The Braze Postman Collection uses a templating variable, &#x60;{{instance_url}}&#x60;, to substitute the REST API URL of your Braze instance into the pre-built requests. Rather than having to manually edit all requests in the Collection, you can set up this variable in your Postman environment. To do so, please follow the steps below:  1. Click on the gear icon in the top right corner of the Postman app.  2. Select \&quot;Manage Environments\&quot; to open a modal window which displays your active environments. 3. In the bottom right corner of the modal window, click \&quot;Add\&quot; to create a new environment. 4. Give this environment a name (e.g. \&quot;Braze API Requests\&quot;) and add keys for &#x60;instance_url&#x60; and &#x60;api_key&#x60; with values corresponding to [your Braze instance](https://www.braze.com/docs/api/basics/#endpoints) and [Braze REST API Key](https://www.braze.com/docs/api/basics/#app-group-rest-api-keys), as pictured below.   As of April, 2020 Braze has changed how we read App Group API keys. Instead of passing them in the request body or through url parameters, we now read the App Group Rest&#x60;api_key&#x60; through the HTTP Authorization header. API keys not passed through the HTTP Authorization Header will coninue to work until they have been sunset.   ## Using the Pre-Built Requests from the Collection  Once you have configured your environment. You can use any of the pre-built requests in the collection as a template for building new API requests. To start using one of the pre-built requests, simply click on it within the &#39;Collections&#39; menu on the left side of Postman. This will open the request as a new tab in the main window of the Postman app.  In general, there are two types of requests that Braze&#39;s API endpoints accept - &#x60;GET&#x60; and &#x60;POST&#x60;. Depending on which &#x60;HTTP&#x60; method the endpoint uses, you&#39;ll need to edit the pre-built request differently.  ### Edit a POST Request  When editing a &#x60;POST&#x60; request, you&#39;ll need to open the request and navigate to the &#x60;Body&#x60; section in the request editor. For readability, select the &#x60;raw&#x60; radio button to format the &#x60;JSON&#x60; request body.  ### Edit a GET Request  When editing a &#x60;GET&#x60; request, you will need to edit the parameters passed in the request URL. To edit these easily, select the &#x60;Params&#x60; button next to the URL bar and edit the key-value pairs in the fields that will appear below the URL bar.  ## Send Your Request  Once your API request is ready to send, click on the &#39;Send&#39; button next to the URL bar. The request will be sent and the response data will be populated in a section underneath the request editor. From here, you can view the raw data returned from Braze&#39;s API, see the HTTP response code, see how long the request took to process, and view header information.
    """
)

