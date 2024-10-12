from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_device_live_tools_ping201_response import CreateDeviceLiveToolsPing201Response
from openapi_server.models.create_device_live_tools_ping_device_request import CreateDeviceLiveToolsPingDeviceRequest
from openapi_server.models.get_device_live_tools_ping200_response import GetDeviceLiveToolsPing200Response
from openapi_server import util


async def create_device_live_tools_ping_device_1(request: web.Request, serial, body=None) -> web.Response:
    """Enqueue a job to check connectivity status to the device

    Enqueue a job to check connectivity status to the device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceLiveToolsPingDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def get_device_live_tools_ping_device_1(request: web.Request, serial, id) -> web.Response:
    """Return a ping device job

    Return a ping device job. Latency unit in response is in milliseconds. Size is in bytes.

    :param serial: 
    :type serial: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)
