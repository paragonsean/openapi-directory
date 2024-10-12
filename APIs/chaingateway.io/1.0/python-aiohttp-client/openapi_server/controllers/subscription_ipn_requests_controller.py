from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_failed_ipns import ListFailedIPNs
from openapi_server.models.list_subscribed_addresses import ListSubscribedAddresses
from openapi_server.models.resend_failed_ipn import ResendFailedIPN
from openapi_server.models.resend_failed_ipn_request import ResendFailedIPNRequest
from openapi_server.models.subscribe_address import SubscribeAddress
from openapi_server.models.subscribe_address_request import SubscribeAddressRequest
from openapi_server.models.unsubscribe_address import UnsubscribeAddress
from openapi_server.models.unsubscribe_address_request import UnsubscribeAddressRequest
from openapi_server import util


async def list_failed_ipns(request: web.Request, content_type, authorization) -> web.Response:
    """listFailedIPNs

    Returns all subscriptions/IPNs created with an account.

    :param content_type: 
    :type content_type: str
    :param authorization: API Key
    :type authorization: str

    """
    return web.Response(status=200)


async def list_subscribed_addresses(request: web.Request, content_type, authorization) -> web.Response:
    """listSubscribedAddresses

    Returns all subscriptions/IPNs created with an account.

    :param content_type: 
    :type content_type: str
    :param authorization: API Key
    :type authorization: str

    """
    return web.Response(status=200)


async def resend_failed_ipn(request: web.Request, authorization, body) -> web.Response:
    """resendFailedIPN

    Returns all subscriptions/IPNs created with an account.

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = ResendFailedIPNRequest.from_dict(body)
    return web.Response(status=200)


async def subscribe_address(request: web.Request, authorization, body) -> web.Response:
    """subscribeAddress

    Creates a new subscription/IPN for the given address (and contractaddress). You will receive a notification to the given url every time a deposit is received. Unsubscribe the address before sending tokens/ETH from it or you won&#39;t get reliable notifications anymore.  

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = SubscribeAddressRequest.from_dict(body)
    return web.Response(status=200)


async def unsubscribe_address(request: web.Request, authorization, body) -> web.Response:
    """unsubscribeAddress

    Deletes an existing subscription/IPN for the given address (and contractaddress).

    :param authorization: API Key
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = UnsubscribeAddressRequest.from_dict(body)
    return web.Response(status=200)
