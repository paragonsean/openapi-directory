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
    description="API v1.0.0",
    author_email="",
    url="",
    keywords=["OpenAPI", "API v1.0.0"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/80638214aa04722c9203)  &lt;span style&#x3D;&#39;margin-left: 0.5em;&#39;&gt;or&lt;/span&gt;  &lt;a href&#x3D;&#39;https://documenter.getpostman.com/view/3559821/TVeqcn2L&#39; class&#x3D;&#39;openapi-button&#39; _ngcontent-c6&gt;View Postman docs&lt;/a&gt;    # Quickstart    Visit [github](https://github.com/EmitKnowledge/Envoice) to view the quickstart tutorial.    &lt;div class&#x3D;&#39;postman-tutorial&#39;&gt;    # Tutorial for running the API in postman    Click on \&quot;\&quot;Run in Postman\&quot;\&quot; button  &lt;br /&gt;&lt;br /&gt;  ![postman - tutorial - 1](/Assets/images/api/postman-tutorial/postman-tutorial-1.png)     ---     A new page will open.  Click the \&quot;\&quot;Postman for windows\&quot;\&quot; to run postman as a desktop app.  Make sure you have already [installed](https://www.getpostman.com/docs/postman/launching_postman/installation_and_updates) Postman.  &lt;br /&gt;&lt;br /&gt;  ![postman - tutorial - 2](/Assets/images/api/postman-tutorial/postman-tutorial-2.png)     ---     In chrome an alert might show up to set a default app for opening postman links. Click on \&quot;\&quot;Open Postman\&quot;\&quot;.  &lt;br /&gt;&lt;br /&gt;  ![postman - tutorial - 3](/Assets/images/api/postman-tutorial/postman-tutorial-3.png)     ---     The OpenAPI specification will be imported in Postman as a new collection named \&quot;\&quot;Envoice api\&quot;\&quot;  &lt;br /&gt;&lt;br /&gt;  ![postman - tutorial - 4](/Assets/images/api/postman-tutorial/postman-tutorial-4.png)     ---     When testing be sure to check and modify the environment variables to suit your api key and secret. The domain is set to envoice&#39;s endpoint so you don&#39;t really need to change that.    &lt;sub&gt;\\*Eye button in top right corner &lt;/sub&gt;  &lt;br /&gt;&lt;br /&gt;   ![postman - tutorial - 5](/Assets/images/api/postman-tutorial/postman-tutorial-5.png)  &lt;br /&gt;&lt;br /&gt;   ![postman - tutorial - 6](/Assets/images/api/postman-tutorial/postman-tutorial-6.png)     ---     You don&#39;t need to change the values of the header parameters, because they will be replaced automatically when you send a request with real values from the environment configured in the previous step.  &lt;br /&gt;&lt;br /&gt;  ![postman - tutorial - 7](/Assets/images/api/postman-tutorial/postman-tutorial-7.png)     ---     Modify the example data to suit your needs and send a request.  &lt;br /&gt;&lt;br /&gt;  ![postman - tutorial - 8](/Assets/images/api/postman-tutorial/postman-tutorial-8.png)  &lt;/div&gt;    # Webhooks    Webhooks allow you to build or set up Envoice Apps which subscribe to invoice activities.   When one of those events is triggered, we&#39;ll send a HTTP POST payload to the webhook&#39;s configured URL.   Webhooks can be used to update an external invoice data storage.    In order to use webhooks visit [this link](/account/settings#api-tab) and add upto 10 webhook urls that will return status &#x60;200&#x60; in order to signal that the webhook is working.  All nonworking webhooks will be ignored after a certain period of time and several retry attempts.  If after several attempts the webhook starts to work, we will send you all activities, both past and present, in chronological order.    The payload of the webhook is in format:  &#x60;&#x60;&#x60;  {      Signature: \&quot;\&quot;sha256 string\&quot;\&quot;,      Timestamp: \&quot;\&quot;YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\&quot;\&quot;,      Activity: {          Message: \&quot;string\&quot;,          Link: \&quot;share url\&quot;,          Type: int,                  InvoiceNumber: \&quot;string\&quot;,          InvoiceId: int,                  OrderNumber: \&quot;string\&quot;,          OrderId: int,          Id: int,          CreatedOn: \&quot;YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\&quot;      }  }  &#x60;&#x60;&#x60;            
    """
)

