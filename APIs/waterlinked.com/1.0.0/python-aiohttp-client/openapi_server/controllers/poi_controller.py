from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_poi_payload import CreatePoiPayload
from openapi_server.models.error import Error
from openapi_server.models.update_poi_payload import UpdatePoiPayload
from openapi_server.models.waterlinked_poi import WaterlinkedPoi
from openapi_server import util


async def poi_create(request: web.Request, payload) -> web.Response:
    """Create poi

    Create a new POI

    :param payload: A list of all POI
    :type payload: dict | bytes

    """
    payload = CreatePoiPayload.from_dict(payload)
    return web.Response(status=200)


async def poi_delete(request: web.Request, id) -> web.Response:
    """Delete poi

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def poi_list(request: web.Request, ) -> web.Response:
    """List poi

    List all points of interest


    """
    return web.Response(status=200)


async def poi_show(request: web.Request, id) -> web.Response:
    """Show poi

    Get a POI

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def poi_update(request: web.Request, id, payload) -> web.Response:
    """Update poi

    

    :param id: 
    :type id: int
    :param payload: A list of all POI
    :type payload: dict | bytes

    """
    payload = UpdatePoiPayload.from_dict(payload)
    return web.Response(status=200)
