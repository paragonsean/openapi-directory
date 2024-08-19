from typing import List, Dict
from aiohttp import web

from openapi_server.models.client_error_response import ClientErrorResponse
from openapi_server.models.partner import Partner
from openapi_server.models.partner_list import PartnerList
from openapi_server.models.partner_upsert import PartnerUpsert
from openapi_server.models.server_error_response import ServerErrorResponse
from openapi_server.models.validation_error_response import ValidationErrorResponse
from openapi_server import util


async def create_partner(request: web.Request, body) -> web.Response:
    """Create a partner

    Create a new partner. Returns a partner object if the create is succeded.

    :param body: PartnerUpsert object that you would like to store.
    :type body: dict | bytes

    """
    body = PartnerUpsert.from_dict(body)
    return web.Response(status=200)


async def delete_partner(request: web.Request, id) -> web.Response:
    """Delete a partner

    Delete an existing partner.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def get_partner(request: web.Request, id) -> web.Response:
    """Retrieve a partner

    Retrieves the details of an existing partner.

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def list_partner(request: web.Request, page=None, per_page=None) -> web.Response:
    """List all partners

    Returns a list of your partners. The partners are returned sorted by creation date, with the most recent partners appearing first.

    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)


async def update_partner(request: web.Request, id, body) -> web.Response:
    """Update a partner

    Update an existing partner. Returns a partner object if the update is succeded.

    :param id: 
    :type id: int
    :param body: Partner object that you would like to update.
    :type body: dict | bytes

    """
    body = PartnerUpsert.from_dict(body)
    return web.Response(status=200)
