from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_external_price_source_request import ConfigExternalPriceSourceRequest
from openapi_server.models.get_prices_request_object import GetPricesRequestObject
from openapi_server.models.response2 import Response2
from openapi_server import util


async def api_pricing_hub_prices_post(request: web.Request, account_name, accept, content_type, x_vtex_api_app_key, x_vtex_api_app_token, body) -> web.Response:
    """Get Prices

    This route retrieves and applies prices for the items that are passed in the request. Pricing Hub will select the pricing method that will be used for each item and will fetch their respective price from the selected pricing method.     &gt;ℹ️ &gt; This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests). 

    :param account_name: Name of the VTEX account. Used as part of the URL
    :type account_name: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param x_vtex_api_app_key: The AppKey configured by the merchant
    :type x_vtex_api_app_key: str
    :param x_vtex_api_app_token: The AppToken configured by the merchant
    :type x_vtex_api_app_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetPricesRequestObject.from_dict(body)
    return web.Response(status=200)


async def config_external_price_source(request: web.Request, accept, content_type, x_vtex_api_app_key, x_vtex_api_app_token, body, an=None) -> web.Response:
    """Configure External Price Source

    This route facilitates setting up an external price source in Pricing Hub. It also allows you to activate or deactivate that source in a given account.     &gt;ℹ️ This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests). 

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Describes the type of the content being sent
    :type content_type: str
    :param x_vtex_api_app_key: The AppKey configured by the merchant
    :type x_vtex_api_app_key: str
    :param x_vtex_api_app_token: The AppToken configured by the merchant
    :type x_vtex_api_app_token: str
    :param body: 
    :type body: dict | bytes
    :param an: Name of the VTEX account
    :type an: str

    """
    body = ConfigExternalPriceSourceRequest.from_dict(body)
    return web.Response(status=200)
