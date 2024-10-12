from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_merchant_request import CreateMerchantRequest
from openapi_server.models.create_merchant_response import CreateMerchantResponse
from openapi_server.models.list_merchant_response import ListMerchantResponse
from openapi_server.models.merchant import Merchant
from openapi_server.models.request_activation_response import RequestActivationResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server import util


async def get_merchants(request: web.Request, page_number=None, page_size=None) -> web.Response:
    """Get a list of merchant accounts

    Returns the list of merchant accounts that your API credential has access to. The list is grouped into pages as defined by the query parameters.   To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Account read

    :param page_number: The number of the page to fetch.
    :type page_number: int
    :param page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
    :type page_size: int

    """
    return web.Response(status=200)


async def get_merchants_merchant_id(request: web.Request, merchant_id) -> web.Response:
    """Get a merchant account

    Returns the merchant account specified in the path. Your API credential must have access to the merchant account.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Account read

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str

    """
    return web.Response(status=200)


async def post_merchants(request: web.Request, body=None) -> web.Response:
    """Create a merchant account

    Creates a merchant account for the company account specified in the request.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Accounts read and write

    :param body: 
    :type body: dict | bytes

    """
    body = CreateMerchantRequest.from_dict(body)
    return web.Response(status=200)


async def post_merchants_merchant_id_activate(request: web.Request, merchant_id) -> web.Response:
    """Request to activate a merchant account

    Sends a request to activate the merchant account identified in the path.  You get the result of the activation asynchronously through a [&#x60;merchant.updated&#x60;](https://docs.adyen.com/api-explorer/ManagementNotification/latest/post/merchant.updated) webhook. Once the merchant account is activated, you can start using it to accept payments and payouts.  Use this endpoint if your integration requires it, such as Adyen for Platforms Manage. Your Adyen contact will set up your access.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Accounts read and write

    :param merchant_id: The unique identifier of the merchant account.
    :type merchant_id: str

    """
    return web.Response(status=200)
