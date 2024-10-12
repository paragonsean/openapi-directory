from typing import List, Dict
from aiohttp import web

from openapi_server.models.smart_me_device_configuration_container import SmartMeDeviceConfigurationContainer
from openapi_server import util


async def smart_me_device_configuration_get(request: web.Request, id) -> web.Response:
    """Gets the configuration of a smart-me device.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def smart_me_device_configuration_post(request: web.Request, body) -> web.Response:
    """Sets the configuration of a smart-me device. The device needs to be online.

    

    :param body: 
    :type body: dict | bytes

    """
    body = SmartMeDeviceConfigurationContainer.from_dict(body)
    return web.Response(status=200)
