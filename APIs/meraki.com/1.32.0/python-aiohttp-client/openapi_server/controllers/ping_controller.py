from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_device_live_tools_ping201_response import CreateDeviceLiveToolsPing201Response
from openapi_server.models.create_device_live_tools_ping_request import CreateDeviceLiveToolsPingRequest
from openapi_server.models.get_device_live_tools_ping200_response import GetDeviceLiveToolsPing200Response
from openapi_server import util


async def create_device_live_tools_ping_1(request: web.Request, serial, body) -> web.Response:
    """Enqueue a job to ping a target host from the device

    Enqueue a job to ping a target host from the device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceLiveToolsPingRequest.from_dict(body)
    return web.Response(status=200)


async def get_device_live_tools_ping_1(request: web.Request, serial, id) -> web.Response:
    """Return a ping job

    Return a ping job. Latency unit in response is in milliseconds. Size is in bytes.

    :param serial: 
    :type serial: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)
