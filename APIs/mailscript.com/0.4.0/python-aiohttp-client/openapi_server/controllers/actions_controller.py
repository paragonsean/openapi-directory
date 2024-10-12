from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_action_request import AddActionRequest
from openapi_server.models.add_action_response import AddActionResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_all_actions_response import GetAllActionsResponse
from openapi_server.models.key import Key
from openapi_server import util


async def add_action(request: web.Request, body) -> web.Response:
    """Add an action

    

    :param body: Add action body
    :type body: dict | bytes

    """
    body = AddActionRequest.from_dict(body)
    return web.Response(status=200)


async def delete_action(request: web.Request, action) -> web.Response:
    """Delete an action

    

    :param action: ID of the action
    :type action: str

    """
    return web.Response(status=200)


async def get_all_actions(request: web.Request, ) -> web.Response:
    """Get all actions for the user

    


    """
    return web.Response(status=200)


async def update_action(request: web.Request, action, body) -> web.Response:
    """Update an action key

    

    :param action: ID of action
    :type action: str
    :param body: Action body
    :type body: dict | bytes

    """
    body = AddActionRequest.from_dict(body)
    return web.Response(status=200)
