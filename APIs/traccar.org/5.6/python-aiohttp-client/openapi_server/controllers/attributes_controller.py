from typing import List, Dict
from aiohttp import web

from openapi_server.models.attribute import Attribute
from openapi_server import util


async def attributes_computed_get(request: web.Request, all=None, user_id=None, device_id=None, group_id=None, refresh=None) -> web.Response:
    """Fetch a list of Attributes

    Without params, it returns a list of Attributes the user has access to

    :param all: Can only be used by admins or managers to fetch all entities
    :type all: bool
    :param user_id: Standard users can use this only with their own _userId_
    :type user_id: int
    :param device_id: Standard users can use this only with _deviceId_s, they have access to
    :type device_id: int
    :param group_id: Standard users can use this only with _groupId_s, they have access to
    :type group_id: int
    :param refresh: 
    :type refresh: bool

    """
    return web.Response(status=200)


async def attributes_computed_id_delete(request: web.Request, id) -> web.Response:
    """Delete an Attribute

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def attributes_computed_id_put(request: web.Request, id, body) -> web.Response:
    """Update an Attribute

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Attribute.from_dict(body)
    return web.Response(status=200)


async def attributes_computed_post(request: web.Request, body) -> web.Response:
    """Create an Attribute

    

    :param body: 
    :type body: dict | bytes

    """
    body = Attribute.from_dict(body)
    return web.Response(status=200)
