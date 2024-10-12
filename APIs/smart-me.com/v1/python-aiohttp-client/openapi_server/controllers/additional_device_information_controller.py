from typing import List, Dict
from aiohttp import web

from openapi_server.models.additional_device_information import AdditionalDeviceInformation
from openapi_server import util


async def additional_device_information_get(request: web.Request, id) -> web.Response:
    """Gets the additional information (e.g. Firmware Version) about a device.

    Gets the additional information (e.g. Firmware Version) about a device.

    :param id: The ID of the device
    :type id: str

    """
    return web.Response(status=200)
