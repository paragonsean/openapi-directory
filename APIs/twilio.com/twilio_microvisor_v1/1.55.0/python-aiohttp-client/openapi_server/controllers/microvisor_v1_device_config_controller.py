from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_device_config_response import ListDeviceConfigResponse
from openapi_server.models.microvisor_v1_device_device_config import MicrovisorV1DeviceDeviceConfig
from openapi_server import util


async def create_device_config(request: web.Request, device_sid, key, value) -> web.Response:
    """create_device_config

    Create a config for a Microvisor Device.

    :param device_sid: A 34-character string that uniquely identifies the Device.
    :type device_sid: str
    :param key: The config key; up to 100 characters.
    :type key: str
    :param value: The config value; up to 4096 characters.
    :type value: str

    """
    return web.Response(status=200)


async def delete_device_config(request: web.Request, device_sid, key) -> web.Response:
    """delete_device_config

    Delete a config for a Microvisor Device.

    :param device_sid: A 34-character string that uniquely identifies the Device.
    :type device_sid: str
    :param key: The config key; up to 100 characters.
    :type key: str

    """
    return web.Response(status=200)


async def fetch_device_config(request: web.Request, device_sid, key) -> web.Response:
    """fetch_device_config

    Retrieve a Config for a Device.

    :param device_sid: A 34-character string that uniquely identifies the Device.
    :type device_sid: str
    :param key: The config key; up to 100 characters.
    :type key: str

    """
    return web.Response(status=200)


async def list_device_config(request: web.Request, device_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_device_config

    Retrieve a list of all Configs for a Device.

    :param device_sid: A 34-character string that uniquely identifies the Device.
    :type device_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_device_config(request: web.Request, device_sid, key, value) -> web.Response:
    """update_device_config

    Update a config for a Microvisor Device.

    :param device_sid: A 34-character string that uniquely identifies the Device.
    :type device_sid: str
    :param key: The config key; up to 100 characters.
    :type key: str
    :param value: The config value; up to 4096 characters.
    :type value: str

    """
    return web.Response(status=200)
