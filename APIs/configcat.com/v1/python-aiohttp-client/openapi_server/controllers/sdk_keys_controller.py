from typing import List, Dict
from aiohttp import web

from openapi_server.models.sdk_keys_model import SdkKeysModel
from openapi_server import util


async def get_sdk_keys(request: web.Request, config_id, environment_id) -> web.Response:
    """Get SDK Key

    This endpoint returns the SDK Key for your Config in a specified Environment.

    :param config_id: The identifier of the Config.
    :type config_id: str
    :type config_id: str
    :param environment_id: The identifier of the Environment.
    :type environment_id: str
    :type environment_id: str

    """
    return web.Response(status=200)
