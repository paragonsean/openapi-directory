from typing import List, Dict
from aiohttp import web

from openapi_server.models.command import Command
from openapi_server.models.command_type import CommandType
from openapi_server import util


async def commands_get(request: web.Request, all=None, user_id=None, device_id=None, group_id=None, refresh=None) -> web.Response:
    """Fetch a list of Saved Commands

    Without params, it returns a list of Saved Commands the user has access to

    :param all: Can only be used by admins or managers to fetch all entities
    :type all: bool
    :param user_id: Standard users can use this only with their own _userId_
    :type user_id: int
    :param device_id: Standard users can use this only with _deviceId_s, they have access to
    :type device_id: int
    :param group_id: Standard users can use this only with _groupId_s, they have access to
    :type group_id: int
    :param refresh: 
    :type refresh: bool

    """
    return web.Response(status=200)


async def commands_id_delete(request: web.Request, id) -> web.Response:
    """Delete a Saved Command

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def commands_id_put(request: web.Request, id, body) -> web.Response:
    """Update a Saved Command

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Command.from_dict(body)
    return web.Response(status=200)


async def commands_post(request: web.Request, body) -> web.Response:
    """Create a Saved Command

    

    :param body: 
    :type body: dict | bytes

    """
    body = Command.from_dict(body)
    return web.Response(status=200)


async def commands_send_get(request: web.Request, device_id=None) -> web.Response:
    """Fetch a list of Saved Commands supported by Device at the moment

    Return a list of saved commands linked to Device and its groups, filtered by current Device protocol support

    :param device_id: Standard users can use this only with _deviceId_s, they have access to
    :type device_id: int

    """
    return web.Response(status=200)


async def commands_send_post(request: web.Request, body) -> web.Response:
    """Dispatch commands to device

    Dispatch a new command or Saved Command if _body.id_ set

    :param body: 
    :type body: dict | bytes

    """
    body = Command.from_dict(body)
    return web.Response(status=200)


async def commands_types_get(request: web.Request, device_id=None, protocol=None, text_channel=None) -> web.Response:
    """Fetch a list of available Commands for the Device or all possible Commands if Device ommited

    

    :param device_id: Internal device identifier. Only works if device has already reported some locations
    :type device_id: int
    :param protocol: Protocol name. Can be used instead of device id
    :type protocol: str
    :param text_channel: When &#x60;true&#x60; return SMS commands. If not specified or &#x60;false&#x60; return data commands
    :type text_channel: bool

    """
    return web.Response(status=200)
