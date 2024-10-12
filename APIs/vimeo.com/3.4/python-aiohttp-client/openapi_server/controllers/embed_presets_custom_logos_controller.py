from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.picture import Picture
from openapi_server import util


async def create_custom_logo(request: web.Request, user_id) -> web.Response:
    """Add a custom logo

    

    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def create_custom_logo_alt1(request: web.Request, ) -> web.Response:
    """Add a custom logo

    


    """
    return web.Response(status=200)


async def get_custom_logo(request: web.Request, logo_id, user_id) -> web.Response:
    """Get a specific custom logo

    

    :param logo_id: The ID of the custom logo.
    :type logo_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def get_custom_logo_alt1(request: web.Request, logo_id) -> web.Response:
    """Get a specific custom logo

    

    :param logo_id: The ID of the custom logo.
    :type logo_id: 

    """
    return web.Response(status=200)


async def get_custom_logos(request: web.Request, user_id) -> web.Response:
    """Get all the custom logos that belong to a user

    

    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def get_custom_logos_alt1(request: web.Request, ) -> web.Response:
    """Get all the custom logos that belong to a user

    


    """
    return web.Response(status=200)
