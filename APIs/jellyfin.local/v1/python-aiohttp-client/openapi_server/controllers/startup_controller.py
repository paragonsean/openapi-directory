from typing import List, Dict
from aiohttp import web

from openapi_server.models.startup_configuration_dto import StartupConfigurationDto
from openapi_server.models.startup_remote_access_dto import StartupRemoteAccessDto
from openapi_server.models.startup_user_dto import StartupUserDto
from openapi_server import util


async def complete_wizard(request: web.Request, ) -> web.Response:
    """Completes the startup wizard.

    


    """
    return web.Response(status=200)


async def get_first_user(request: web.Request, ) -> web.Response:
    """Gets the first user.

    


    """
    return web.Response(status=200)


async def get_first_user2(request: web.Request, ) -> web.Response:
    """Gets the first user.

    


    """
    return web.Response(status=200)


async def get_startup_configuration(request: web.Request, ) -> web.Response:
    """Gets the initial startup wizard configuration.

    


    """
    return web.Response(status=200)


async def set_remote_access(request: web.Request, body) -> web.Response:
    """Sets remote access and UPnP.

    

    :param body: The startup remote access dto.
    :type body: dict | bytes

    """
    body = StartupRemoteAccessDto.from_dict(body)
    return web.Response(status=200)


async def update_initial_configuration(request: web.Request, body) -> web.Response:
    """Sets the initial startup wizard configuration.

    

    :param body: The updated startup configuration.
    :type body: dict | bytes

    """
    body = StartupConfigurationDto.from_dict(body)
    return web.Response(status=200)


async def update_startup_user(request: web.Request, body=None) -> web.Response:
    """Sets the user name and password.

    

    :param body: The DTO containing username and password.
    :type body: dict | bytes

    """
    body = StartupUserDto.from_dict(body)
    return web.Response(status=200)
