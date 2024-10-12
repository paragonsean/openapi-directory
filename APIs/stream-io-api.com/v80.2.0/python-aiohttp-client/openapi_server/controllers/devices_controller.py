from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.create_device_request import CreateDeviceRequest
from openapi_server.models.list_devices_response import ListDevicesResponse
from openapi_server.models.response import Response
from openapi_server import util


async def create_device(request: web.Request, body) -> web.Response:
    """Create device

    Adds a new device to a user, if the same device already exists the call will have no effect 

    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def delete_device(request: web.Request, id=None, user_id=None) -> web.Response:
    """Delete device

    Deletes device 

    :param id: 
    :type id: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def list_devices(request: web.Request, user_id=None) -> web.Response:
    """List devices

    Returns all available devices 

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)
