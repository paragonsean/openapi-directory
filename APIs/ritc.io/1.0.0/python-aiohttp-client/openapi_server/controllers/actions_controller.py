from typing import List, Dict
from aiohttp import web

from openapi_server.models.action59 import Action59
from openapi_server.models.action_full_response import ActionFullResponse
from openapi_server.models.action_short_response import ActionShortResponse
from openapi_server import util


async def add_action(request: web.Request, action_object) -> web.Response:
    """add_action

    Create a new action

    :param action_object: Action information
    :type action_object: dict | bytes

    """
    action_object = Action59.from_dict(action_object)
    return web.Response(status=200)


async def get_action(request: web.Request, action_id) -> web.Response:
    """get_action

    Get an action

    :param action_id: Id of action_id
    :type action_id: str

    """
    return web.Response(status=200)


async def list_actions(request: web.Request, ) -> web.Response:
    """list_actions

    List actions


    """
    return web.Response(status=200)


async def remove_action(request: web.Request, action_id) -> web.Response:
    """remove_action

    Delete an action

    :param action_id: Id of action
    :type action_id: str

    """
    return web.Response(status=200)


async def update_action(request: web.Request, action_id, action_object) -> web.Response:
    """update_action

    Update information about a specific action

    :param action_id: Id of user
    :type action_id: str
    :param action_object: Action information
    :type action_object: dict | bytes

    """
    action_object = Action59.from_dict(action_object)
    return web.Response(status=200)
