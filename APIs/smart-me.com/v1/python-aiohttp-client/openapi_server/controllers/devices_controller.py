from typing import List, Dict
from aiohttp import web

from openapi_server.models.device import Device
from openapi_server.models.device_to_post import DeviceToPost
from openapi_server import util


async def api_devices_id_get(request: web.Request, id) -> web.Response:
    """Gets a Device by it&#39;s ID

    Gets a Device by it&#39;s ID

    :param id: The ID of the device
    :type id: str

    """
    return web.Response(status=200)


async def devices_get(request: web.Request, ) -> web.Response:
    """Gets all Devices

    Gets all Devices


    """
    return web.Response(status=200)


async def devices_post(request: web.Request, body) -> web.Response:
    """Creates or updates a Device or updates it&#39;s values.

    Creates or updates a Device or updates it&#39;s values.               For a new device leave the ID empty. To create a device you have to set the DeviceEnergyType.              To update values, add the ID of the device and the values you like to set.  (See the Data Type Model for more Information)

    :param body: Device object with all the data
    :type body: dict | bytes

    """
    body = DeviceToPost.from_dict(body)
    return web.Response(status=200)


async def devices_put(request: web.Request, id, switch_state, switch_number=None) -> web.Response:
    """Updates the On/Off Switch on a device.               For new implementations please use the \&quot;actions\&quot; command

    Updates the On/Off Switch on a device              For new implementations please use the \&quot;actions\&quot; command

    :param id: The ID of the device
    :type id: str
    :param switch_state: The new state of the switch
    :type switch_state: bool
    :param switch_number: The number of the switch if there are multiple (1 for L1, 3 for L3)
    :type switch_number: int

    """
    return web.Response(status=200)
