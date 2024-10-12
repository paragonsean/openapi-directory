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
    description="Voodoo Manufacturing 3D Print API",
    author_email="support@voodoomfg.com",
    url="",
    keywords=["OpenAPI", "Voodoo Manufacturing 3D Print API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Welcome to the Voodoo Manufacturing API docs!  Your Voodoo Manufacturing API key must be included with each request to the API. The API will look for the key in the \&quot;api_key\&quot; header of the request. &lt;a href&#x3D;\&quot;https://voodoomfg.com/3d-print-api#get-access\&quot; target&#x3D;\&quot;_blank\&quot;&gt;You can request a key here.&lt;/a&gt;  This API provides a programmatic interface for submitting printing orders to Voodoo Manufacturing. The general process for creating an order is as follows:   - Get a list of the available materials with the /materials endpoint   - Upload models to the API with the /models endpoint   - Get quotes for shipping methods with the /order/shipping endpoint   - Get a quote for an order with the /order/create endpoint   - Confirm the order with the /order/confirm endpoint  Uploaded models and orders can be retrieved either in bulk or by id at the /model and /order endpoints, respectively.  In some cases, you may wish to get a quote for a specific model without the context of an order. In this case, you may use the /model/quote (if you&#39;ve already uploaded the model to the API) or the /model/quote_attrs (lets you quote based on calculated model attributes) endpoints. 
    """
)

