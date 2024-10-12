from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.create_command_request import CreateCommandRequest
from openapi_server.models.create_command_response import CreateCommandResponse
from openapi_server.models.delete_command_response import DeleteCommandResponse
from openapi_server.models.get_command_response import GetCommandResponse
from openapi_server.models.list_commands_response import ListCommandsResponse
from openapi_server.models.update_command_request import UpdateCommandRequest
from openapi_server.models.update_command_response import UpdateCommandResponse
from openapi_server import util


async def create_command(request: web.Request, body) -> web.Response:
    """Create command

    Creates custom chat command 

    :param body: Command
    :type body: dict | bytes

    """
    body = CreateCommandRequest.from_dict(body)
    return web.Response(status=200)


async def delete_command(request: web.Request, name) -> web.Response:
    """Delete command

    Deletes custom chat command 

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def get_command(request: web.Request, name) -> web.Response:
    """Get command

    Returns custom command by its name 

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def list_commands(request: web.Request, ) -> web.Response:
    """List commands

    Returns all custom commands 


    """
    return web.Response(status=200)


async def update_command(request: web.Request, name, body) -> web.Response:
    """Update command

    Updates custom chat command 

    :param name: 
    :type name: str
    :param body: Command
    :type body: dict | bytes

    """
    body = UpdateCommandRequest.from_dict(body)
    return web.Response(status=200)
