from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_catalogue(request: web.Request, catalogue_id) -> web.Response:
    """Catalogue Detail

    Return the content of the selected catalogue.

    :param catalogue_id: The identifier for the selected catalogue.
    :type catalogue_id: str

    """
    return web.Response(status=200)


async def get_catalogue_asset(request: web.Request, catalogue_id, title=None, start=None, end=None, updated_after=None, limit=None, aliases=None) -> web.Response:
    """Catalogue Asset Collection

    Return the content of the selected catalogue.

    :param catalogue_id: The identifier for the selected catalogue.
    :type catalogue_id: str
    :param title: The query string for a title search
    :type title: str
    :param start: The Start Date for the catalogue date range.
    :type start: str
    :param end: The End Date for the catalogue date range.
    :type end: str
    :param updated_after: Retrieve items only that have been updated after this point.
    :type updated_after: str
    :param limit: Restrict number of returned items Min &#x3D; 1, Max &#x3D; 500.
    :type limit: 
    :param aliases: Flag to display Legacy and Provider Ids.
    :type aliases: bool

    """
    return web.Response(status=200)


async def get_catalogue_asset_detail(request: web.Request, catalogue_id, asset_id) -> web.Response:
    """Catalogue Asset Detail

    Return the content of the selected catalogue asset.

    :param catalogue_id: The identifier for the selected catalogue.
    :type catalogue_id: str
    :param asset_id: The identifier for the selected catalogue asset.
    :type asset_id: str

    """
    return web.Response(status=200)


async def list_catalogues(request: web.Request, ) -> web.Response:
    """Catalogue Collection

    Return a collection of Catalogues.


    """
    return web.Response(status=200)
