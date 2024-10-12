from typing import List, Dict
from aiohttp import web

from openapi_server.models.device import Device
from openapi_server.models.device_accumulators import DeviceAccumulators
from openapi_server import util


async def devices_get(request: web.Request, all=None, user_id=None, id=None, unique_id=None) -> web.Response:
    """Fetch a list of Devices

    Without any params, returns a list of the user&#39;s devices

    :param all: Can only be used by admins or managers to fetch all entities
    :type all: bool
    :param user_id: Standard users can use this only with their own _userId_
    :type user_id: int
    :param id: To fetch one or more devices. Multiple params can be passed like &#x60;id&#x3D;31&amp;id&#x3D;42&#x60;
    :type id: int
    :param unique_id: To fetch one or more devices. Multiple params can be passed like &#x60;uniqueId&#x3D;333331&amp;uniqieId&#x3D;44442&#x60;
    :type unique_id: str

    """
    return web.Response(status=200)


async def devices_id_accumulators_put(request: web.Request, id, body) -> web.Response:
    """Update total distance and hours of the Device

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = DeviceAccumulators.from_dict(body)
    return web.Response(status=200)


async def devices_id_delete(request: web.Request, id) -> web.Response:
    """Delete a Device

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def devices_id_put(request: web.Request, id, body) -> web.Response:
    """Update a Device

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Device.from_dict(body)
    return web.Response(status=200)


async def devices_post(request: web.Request, body) -> web.Response:
    """Create a Device

    

    :param body: 
    :type body: dict | bytes

    """
    body = Device.from_dict(body)
    return web.Response(status=200)
