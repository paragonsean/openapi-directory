from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_device_secret_response import ListDeviceSecretResponse
from openapi_server.models.microvisor_v1_device_device_secret import MicrovisorV1DeviceDeviceSecret
from openapi_server import util


async def create_device_secret(request: web.Request, device_sid, key, value) -> web.Response:
    """create_device_secret

    Create a secret for a Microvisor Device.

    :param device_sid: A 34-character string that uniquely identifies the Device.
    :type device_sid: str
    :param key: The secret key; up to 100 characters.
    :type key: str
    :param value: The secret value; up to 4096 characters.
    :type value: str

    """
    return web.Response(status=200)


async def delete_device_secret(request: web.Request, device_sid, key) -> web.Response:
    """delete_device_secret

    Delete a secret for a Microvisor Device.

    :param device_sid: A 34-character string that uniquely identifies the Device.
    :type device_sid: str
    :param key: The secret key; up to 100 characters.
    :type key: str

    """
    return web.Response(status=200)


async def fetch_device_secret(request: web.Request, device_sid, key) -> web.Response:
    """fetch_device_secret

    Retrieve a Secret for a Device.

    :param device_sid: A 34-character string that uniquely identifies the Device.
    :type device_sid: str
    :param key: The secret key; up to 100 characters.
    :type key: str

    """
    return web.Response(status=200)


async def list_device_secret(request: web.Request, device_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_device_secret

    Retrieve a list of all Secrets for a Device.

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


async def update_device_secret(request: web.Request, device_sid, key, value) -> web.Response:
    """update_device_secret

    Update a secret for a Microvisor Device.

    :param device_sid: A 34-character string that uniquely identifies the Device.
    :type device_sid: str
    :param key: The secret key; up to 100 characters.
    :type key: str
    :param value: The secret value; up to 4096 characters.
    :type value: str

    """
    return web.Response(status=200)
