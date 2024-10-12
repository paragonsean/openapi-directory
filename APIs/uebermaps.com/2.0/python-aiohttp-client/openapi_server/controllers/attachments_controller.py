from typing import List, Dict
from aiohttp import web

from openapi_server.models.attachment import Attachment
from openapi_server import util


async def attachments_id_delete(request: web.Request, id) -> web.Response:
    """Delete attachment

    Delete attachment.

    :param id: Attachment id
    :type id: int

    """
    return web.Response(status=200)


async def maps_id_attachments_get(request: web.Request, id) -> web.Response:
    """List attachments for a given map

    List attachments for a given map.

    :param id: Map id
    :type id: int

    """
    return web.Response(status=200)


async def maps_id_attachments_post(request: web.Request, id, image) -> web.Response:
    """Upload map attachment

    Upload map attachment. Wrap attachment parameters in [attachment]

    :param id: Map id
    :type id: int
    :param image: Base64 encoded image
    :type image: str

    """
    return web.Response(status=200)


async def spots_id_attachments_get(request: web.Request, id) -> web.Response:
    """List attachments for a given spot

    List attachments for a given spot.

    :param id: Spot id
    :type id: int

    """
    return web.Response(status=200)


async def spots_id_attachments_post(request: web.Request, id, image) -> web.Response:
    """Upload spot attachment

    Upload spot attachment. Wrap attachment parameters in [attachment]

    :param id: Spot id
    :type id: int
    :param image: Base64 encoded image
    :type image: str

    """
    return web.Response(status=200)
