from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_device_wireless_radio_settings_request import UpdateDeviceWirelessRadioSettingsRequest
from openapi_server import util


async def get_device_wireless_radio_settings_1(request: web.Request, serial) -> web.Response:
    """Return the radio settings of a device

    Return the radio settings of a device

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def update_device_wireless_radio_settings_1(request: web.Request, serial, body=None) -> web.Response:
    """Update the radio settings of a device

    Update the radio settings of a device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceWirelessRadioSettingsRequest.from_dict(body)
    return web.Response(status=200)
