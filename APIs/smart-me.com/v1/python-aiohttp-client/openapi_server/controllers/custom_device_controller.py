from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_device_to_post import CustomDeviceToPost
from openapi_server import util


async def api_custom_device_id_get(request: web.Request, id) -> web.Response:
    """Gets a Custom Device by it&#39;s ID

    Gets a Device by it&#39;s ID

    :param id: The ID of the device
    :type id: str

    """
    return web.Response(status=200)


async def custom_device_get(request: web.Request, ) -> web.Response:
    """Gets all Custom Devices

    Gets all Devices


    """
    return web.Response(status=200)


async def custom_device_post(request: web.Request, body) -> web.Response:
    """Creates or updates a Custom Device or updates it&#39;s values.

    Creates or updates a Custom Device or updates it&#39;s values.              A Custom Device can be any device that like to add some measurement values to the smart-me Cloud.              Only use a custom device for all non meters.              For a new device leave the ID empty. To create a device you have to set the DeviceEnergyType.              To update values, add the ID of the device and the values you like to set.  (See the Data Type Model for more Information)

    :param body: Device object with all the data
    :type body: dict | bytes

    """
    body = CustomDeviceToPost.from_dict(body)
    return web.Response(status=200)
