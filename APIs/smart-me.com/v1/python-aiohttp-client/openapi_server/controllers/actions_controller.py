from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_information import ActionInformation
from openapi_server.models.action_to_post import ActionToPost
from openapi_server import util


async def actions_get(request: web.Request, id) -> web.Response:
    """Gets all available Actions of a Device

    Gets all available Actions of a Device

    :param id: The ID of the device
    :type id: str

    """
    return web.Response(status=200)


async def actions_post(request: web.Request, body) -> web.Response:
    """Set an action for the specified device.

    Set an action for the specified device.

    :param body: The Action Data
    :type body: dict | bytes

    """
    body = ActionToPost.from_dict(body)
    return web.Response(status=200)
