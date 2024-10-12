from typing import List, Dict
from aiohttp import web

from openapi_server.models.link_create_request import LinkCreateRequest
from openapi_server.models.link_response import LinkResponse
from openapi_server.models.page_link_response import PageLinkResponse
from openapi_server import util


async def create_payment_link(request: web.Request, body=None) -> web.Response:
    """Create a payment link.

    

    :param body: 
    :type body: dict | bytes

    """
    body = LinkCreateRequest.from_dict(body)
    return web.Response(status=200)


async def get_payment_link(request: web.Request, link_id) -> web.Response:
    """Get payment link by id.

    

    :param link_id: 
    :type link_id: str

    """
    return web.Response(status=200)


async def get_payment_links(request: web.Request, merchant_id, account_id, portal_id, mode, page=None, limit=None) -> web.Response:
    """List all payment links.

    

    :param merchant_id: 
    :type merchant_id: str
    :param account_id: 
    :type account_id: str
    :param portal_id: 
    :type portal_id: str
    :param mode: 
    :type mode: str
    :param page: 
    :type page: int
    :param limit: 
    :type limit: int

    """
    return web.Response(status=200)


async def update_payment_link(request: web.Request, link_id, body=None) -> web.Response:
    """Update a payment link.

    

    :param link_id: 
    :type link_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = LinkCreateRequest.from_dict(body)
    return web.Response(status=200)
