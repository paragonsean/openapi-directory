from typing import List, Dict
from aiohttp import web

from openapi_server.models.cancelthetransaction_request import CancelthetransactionRequest
from openapi_server.models.refundthetransaction_request import RefundthetransactionRequest
from openapi_server.models.settle_response import SettleResponse
from openapi_server.models.settlethetransaction_request import SettlethetransactionRequest
from openapi_server import util


async def cancelthetransaction(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, accept, content_type, transaction_id, body) -> web.Response:
    """Cancel the transaction

    Cancel&#39;s transaction that was previously approved, but not settled.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param transaction_id: 
    :type transaction_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CancelthetransactionRequest.from_dict(body)
    return web.Response(status=200)


async def refundthetransaction(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, accept, content_type, transaction_id, body) -> web.Response:
    """Refund the transaction

    Refunds transaction&#39;s value that was previously settled.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param transaction_id: 
    :type transaction_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RefundthetransactionRequest.from_dict(body)
    return web.Response(status=200)


async def settlethetransaction(request: web.Request, x_provider_api_app_key, x_provider_api_app_token, accept, content_type, transaction_id, body) -> web.Response:
    """Settle the transaction

    Settles transaction&#39;s value.

    :param x_provider_api_app_key: The AppKey configured by the merchant (optional configuration)
    :type x_provider_api_app_key: str
    :param x_provider_api_app_token: The AppToken configured by the merchant (optional configuration)
    :type x_provider_api_app_token: str
    :param accept: Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    :type accept: str
    :param content_type: The Media type of the body of the request.  Default value for payment provider protocol is application/json
    :type content_type: str
    :param transaction_id: 
    :type transaction_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SettlethetransactionRequest.from_dict(body)
    return web.Response(status=200)
