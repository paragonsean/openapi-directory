from typing import List, Dict
from aiohttp import web

from openapi_server.models.as2_station_entity import As2StationEntity
from openapi_server import util


async def delete_as2_stations_id(request: web.Request, id) -> web.Response:
    """Delete As2 Station

    Delete As2 Station

    :param id: As2 Station ID.
    :type id: int

    """
    return web.Response(status=200)


async def get_as2_stations(request: web.Request, cursor=None, per_page=None) -> web.Response:
    """List As2 Stations

    List As2 Stations

    :param cursor: Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    :type cursor: str
    :param per_page: Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    :type per_page: int

    """
    return web.Response(status=200)


async def get_as2_stations_id(request: web.Request, id) -> web.Response:
    """Show As2 Station

    Show As2 Station

    :param id: As2 Station ID.
    :type id: int

    """
    return web.Response(status=200)


async def patch_as2_stations_id(request: web.Request, id, name=None, private_key=None, private_key_password=None, public_certificate=None) -> web.Response:
    """Update As2 Station

    Update As2 Station

    :param id: As2 Station ID.
    :type id: int
    :param name: AS2 Name
    :type name: str
    :param private_key: 
    :type private_key: str
    :param private_key_password: 
    :type private_key_password: str
    :param public_certificate: 
    :type public_certificate: str

    """
    return web.Response(status=200)


async def post_as2_stations(request: web.Request, name, private_key, public_certificate, private_key_password=None) -> web.Response:
    """Create As2 Station

    Create As2 Station

    :param name: AS2 Name
    :type name: str
    :param private_key: 
    :type private_key: str
    :param public_certificate: 
    :type public_certificate: str
    :param private_key_password: 
    :type private_key_password: str

    """
    return web.Response(status=200)
