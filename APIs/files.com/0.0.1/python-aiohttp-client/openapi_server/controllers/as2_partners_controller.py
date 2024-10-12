from typing import List, Dict
from aiohttp import web

from openapi_server.models.as2_partner_entity import As2PartnerEntity
from openapi_server import util


async def delete_as2_partners_id(request: web.Request, id) -> web.Response:
    """Delete As2 Partner

    Delete As2 Partner

    :param id: As2 Partner ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_as2_partners(request: web.Request, cursor=None, per_page=None) -> web.Response:
    """List As2 Partners

    List As2 Partners

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_as2_partners_id(request: web.Request, id) -> web.Response:
    """Show As2 Partner

    Show As2 Partner

    :param id: As2 Partner ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_as2_partners_id(request: web.Request, id, enable_dedicated_ips=None, name=None, public_certificate=None, server_certificate=None, uri=None) -> web.Response:
    """Update As2 Partner

    Update As2 Partner

    :param id: As2 Partner ID.
    :type id: int
    :param enable_dedicated_ips: 
    :type enable_dedicated_ips: bool
    :param name: AS2 Name
    :type name: str
    :param public_certificate: 
    :type public_certificate: str
    :param server_certificate: Remote server certificate security setting
    :type server_certificate: str
    :param uri: URL base for AS2 responses
    :type uri: str

    """
    return web.Response(status=200)


async def post_as2_partners(request: web.Request, as2_station_id, name, public_certificate, uri, enable_dedicated_ips=None, server_certificate=None) -> web.Response:
    """Create As2 Partner

    Create As2 Partner

    :param as2_station_id: Id of As2Station for this partner
    :type as2_station_id: int
    :param name: AS2 Name
    :type name: str
    :param public_certificate: 
    :type public_certificate: str
    :param uri: URL base for AS2 responses
    :type uri: str
    :param enable_dedicated_ips: 
    :type enable_dedicated_ips: bool
    :param server_certificate: Remote server certificate security setting
    :type server_certificate: str

    """
    return web.Response(status=200)
