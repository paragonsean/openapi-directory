from typing import List, Dict
from aiohttp import web

from openapi_server.models.baudrate import Baudrate
from openapi_server.models.hat import Hat
from openapi_server import util


async def get(request: web.Request, device, baudrate, address) -> web.Response:
    """get

    Gets data from the slave identified by {address}

    :param device: The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning
    :type device: str
    :param baudrate: Baudrate to communicate with M-Bus devices
    :type baudrate: dict | bytes
    :param address: The slave device to get data from
    :type address: str

    """
    baudrate = .from_dict(baudrate)
    return web.Response(status=200)


async def get_multi(request: web.Request, device, baudrate, address, maxframes) -> web.Response:
    """get_multi

    Gets data from the slave identified by {address}, and supports multiple responses from the slave

    :param device: The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning
    :type device: str
    :param baudrate: Baudrate to communicate with M-Bus devices
    :type baudrate: dict | bytes
    :param address: The slave device to get data from
    :type address: str
    :param maxframes: The slave device to get data from
    :type maxframes: int

    """
    baudrate = .from_dict(baudrate)
    return web.Response(status=200)


async def hat(request: web.Request, ) -> web.Response:
    """hat

    Gets Raspberry Pi Hat information


    """
    return web.Response(status=200)


async def hat_off(request: web.Request, ) -> web.Response:
    """hat_off

    Turns off power to the M-Bus


    """
    return web.Response(status=200)


async def hat_on(request: web.Request, ) -> web.Response:
    """hat_on

    Turns on power to the M-Bus


    """
    return web.Response(status=200)


async def mbus_api(request: web.Request, ) -> web.Response:
    """mbus_api

    Returns this API specification


    """
    return web.Response(status=200)


async def scan(request: web.Request, device, baudrate) -> web.Response:
    """scan

    Scan the specified device for slaves

    :param device: The serial device to scan - /dev/ is pre-pended to {device} by M-Bus HTTPD before scanning
    :type device: str
    :param baudrate: Baudrate to communicate with M-Bus devices
    :type baudrate: dict | bytes

    """
    baudrate = .from_dict(baudrate)
    return web.Response(status=200)
