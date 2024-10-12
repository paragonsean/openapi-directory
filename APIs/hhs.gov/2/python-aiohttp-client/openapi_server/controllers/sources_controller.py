from typing import List, Dict
from aiohttp import web

from openapi_server.models.media_item_wrapped import MediaItemWrapped
from openapi_server.models.source_wrapped import SourceWrapped
from openapi_server import util


async def resources_sources_id_json_get(request: web.Request, id) -> web.Response:
    """Get Source by ID

    Information about a specific source.

    :param id: The id of the source to look up
    :type id: int

    """
    return web.Response(status=200)


async def resources_sources_id_syndicate_format_get(request: web.Request, id, format, display_method=None) -> web.Response:
    """Get MediaItems for Source

    MediaItem

    :param id: The id of the record to look up
    :type id: int
    :param format: Automatically added
    :type format: str
    :param display_method: Method used to render an html request. Accepts one: [mv, list, feed]
    :type display_method: str

    """
    return web.Response(status=200)


async def resources_sources_json_get(request: web.Request, max=None, offset=None, sort=None) -> web.Response:
    """Get Sources

    Source Listings

    :param max: The maximum number of records to return
    :type max: int
    :param offset: Return records starting at the offset index.
    :type offset: int
    :param sort: The name of the property to which sorting will be applied
    :type sort: str

    """
    return web.Response(status=200)
