from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_device_management_interface_request import UpdateDeviceManagementInterfaceRequest
from openapi_server import util


async def get_device_management_interface_1(request: web.Request, serial) -> web.Response:
    """Return the management interface settings for a device

    Return the management interface settings for a device

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def update_device_management_interface_1(request: web.Request, serial, body=None) -> web.Response:
    """Update the management interface settings for a device

    Update the management interface settings for a device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceManagementInterfaceRequest.from_dict(body)
    return web.Response(status=200)
