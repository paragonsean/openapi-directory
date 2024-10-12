from typing import List, Dict
from aiohttp import web

from openapi_server.models.blink_device_leds_request import BlinkDeviceLedsRequest
from openapi_server.models.create_device_live_tools_ping201_response import CreateDeviceLiveToolsPing201Response
from openapi_server.models.create_device_live_tools_ping_device_request import CreateDeviceLiveToolsPingDeviceRequest
from openapi_server.models.create_device_live_tools_ping_request import CreateDeviceLiveToolsPingRequest
from openapi_server.models.cycle_device_switch_ports_request import CycleDeviceSwitchPortsRequest
from openapi_server.models.get_device_live_tools_ping200_response import GetDeviceLiveToolsPing200Response
from openapi_server import util


async def blink_device_leds_0(request: web.Request, serial, body=None) -> web.Response:
    """Blink the LEDs on a device

    Blink the LEDs on a device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = BlinkDeviceLedsRequest.from_dict(body)
    return web.Response(status=200)


async def create_device_live_tools_ping_0(request: web.Request, serial, body) -> web.Response:
    """Enqueue a job to ping a target host from the device

    Enqueue a job to ping a target host from the device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceLiveToolsPingRequest.from_dict(body)
    return web.Response(status=200)


async def create_device_live_tools_ping_device_0(request: web.Request, serial, body=None) -> web.Response:
    """Enqueue a job to check connectivity status to the device

    Enqueue a job to check connectivity status to the device

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateDeviceLiveToolsPingDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def cycle_device_switch_ports_0(request: web.Request, serial, body) -> web.Response:
    """Cycle a set of switch ports

    Cycle a set of switch ports

    :param serial: 
    :type serial: str
    :param body: 
    :type body: dict | bytes

    """
    body = CycleDeviceSwitchPortsRequest.from_dict(body)
    return web.Response(status=200)


async def get_device_live_tools_ping_0(request: web.Request, serial, id) -> web.Response:
    """Return a ping job

    Return a ping job. Latency unit in response is in milliseconds. Size is in bytes.

    :param serial: 
    :type serial: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_device_live_tools_ping_device_0(request: web.Request, serial, id) -> web.Response:
    """Return a ping device job

    Return a ping device job. Latency unit in response is in milliseconds. Size is in bytes.

    :param serial: 
    :type serial: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def reboot_device_0(request: web.Request, serial) -> web.Response:
    """Reboot a device

    Reboot a device

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)
