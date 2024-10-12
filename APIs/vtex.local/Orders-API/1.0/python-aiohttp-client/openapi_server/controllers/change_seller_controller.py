from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_window_to_change_seller_request import UpdateWindowToChangeSellerRequest
from openapi_server import util


async def get_window_to_change_seller(request: web.Request, content_type, accept) -> web.Response:
    """Get window to change seller

    Retrieves a marketplace’s window to change seller, that is, the period when it is possible to choose another seller to fulfill a given order after the original seller has canceled it.    The default period for this window is of 2 days, but it can be configured by the request Update window to change seller.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def update_window_to_change_seller(request: web.Request, content_type, accept, body) -> web.Response:
    """Update window to change seller

    Updates a marketplace’s window to change seller, that is, the period when it is possible to choose another seller to fulfill a given order after the original seller has canceled it.    It is possible to check the current window using the request Get window to change seller.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateWindowToChangeSellerRequest.from_dict(body)
    return web.Response(status=200)
