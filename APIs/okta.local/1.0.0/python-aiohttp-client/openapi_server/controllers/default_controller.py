from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def clear_user_sessions(request: web.Request, user_id) -> web.Response:
    """Clear User Sessions

    Clear User Sessions

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def find_user(request: web.Request, q=None) -> web.Response:
    """Find User

    Find User

    :param q: 
    :type q: str

    """
    return web.Response(status=200)


async def get_assigned_app_links(request: web.Request, user_id) -> web.Response:
    """Get Assigned App Links

    Get Assigned App Links

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_current_user(request: web.Request, ) -> web.Response:
    """Get Current User

    Get Current User


    """
    return web.Response(status=200)


async def get_groups_for_user(request: web.Request, user_id) -> web.Response:
    """Get Groups for User

    Get Groups for User

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def get_user(request: web.Request, user_id) -> web.Response:
    """Get User

    Get User

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def reset_factors(request: web.Request, user_id) -> web.Response:
    """Reset Factors

    Reset Factors

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)
