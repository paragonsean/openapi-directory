from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_device_cellular_sims_request import UpdateDeviceCellularSimsRequest
from openapi_server import util


async def get_device_cellular_sims_2(request: web.Request, serial) -> web.Response:
    """Return the SIM and APN configurations for a cellular device.

    Return the SIM and APN configurations for a cellular device.

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def update_device_cellular_sims_2(request: web.Request, serial, body=None) -> web.Response:
    """Updates the SIM and APN configurations for a cellular device.

    Updates the SIM and APN configurations for a cellular device.

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateDeviceCellularSimsRequest.from_dict(body)
    return web.Response(status=200)
