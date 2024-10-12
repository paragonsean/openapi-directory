from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_device_response import ListDeviceResponse
from openapi_server.models.microvisor_v1_device import MicrovisorV1Device
from openapi_server import util


async def fetch_device(request: web.Request, sid) -> web.Response:
    """fetch_device

    Fetch a specific Device.

    :param sid: A 34-character string that uniquely identifies this Device.
    :type sid: str

    """
    return web.Response(status=200)


async def list_device(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_device

    Retrieve a list of all Devices registered with the Account.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_device(request: web.Request, sid, logging_enabled=None, restart_app=None, target_app=None, unique_name=None) -> web.Response:
    """update_device

    Update a specific Device.

    :param sid: A 34-character string that uniquely identifies this Device.
    :type sid: str
    :param logging_enabled: A Boolean flag specifying whether to enable application logging. Logs will be enabled or extended for 24 hours.
    :type logging_enabled: bool
    :param restart_app: Set to true to restart the App running on the Device.
    :type restart_app: bool
    :param target_app: The SID or unique name of the App to be targeted to the Device.
    :type target_app: str
    :param unique_name: A unique and addressable name to be assigned to this Device by the developer. It may be used in place of the Device SID.
    :type unique_name: str

    """
    return web.Response(status=200)
