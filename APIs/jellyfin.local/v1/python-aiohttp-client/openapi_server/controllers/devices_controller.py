from typing import List, Dict
from aiohttp import web

from openapi_server.models.device_info import DeviceInfo
from openapi_server.models.device_info_query_result import DeviceInfoQueryResult
from openapi_server.models.device_options import DeviceOptions
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def delete_device(request: web.Request, id) -> web.Response:
    """Deletes a device.

    

    :param id: Device Id.
    :type id: str

    """
    return web.Response(status=200)


async def get_device_info(request: web.Request, id) -> web.Response:
    """Get info for a device.

    

    :param id: Device Id.
    :type id: str

    """
    return web.Response(status=200)


async def get_device_options(request: web.Request, id) -> web.Response:
    """Get options for a device.

    

    :param id: Device Id.
    :type id: str

    """
    return web.Response(status=200)


async def get_devices(request: web.Request, supports_sync=None, user_id=None) -> web.Response:
    """Get Devices.

    

    :param supports_sync: Gets or sets a value indicating whether [supports synchronize].
    :type supports_sync: bool
    :param user_id: Gets or sets the user identifier.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def update_device_options(request: web.Request, id, body) -> web.Response:
    """Update device options.

    

    :param id: Device Id.
    :type id: str
    :param body: Device Options.
    :type body: dict | bytes

    """
    body = DeviceOptions.from_dict(body)
    return web.Response(status=200)
