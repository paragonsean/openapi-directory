from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def activate_user(request: web.Request, user_id, send_email=None) -> web.Response:
    """Activate User

    Activate User

    :param user_id: 
    :type user_id: str
    :param send_email: 
    :type send_email: str

    """
    return web.Response(status=200)


async def deactivate_user(request: web.Request, user_id) -> web.Response:
    """Deactivate User

    Deactivate User

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def reset_password(request: web.Request, user_id, send_email=None) -> web.Response:
    """Reset Password

    Reset Password

    :param user_id: 
    :type user_id: str
    :param send_email: 
    :type send_email: str

    """
    return web.Response(status=200)


async def set_temp_password(request: web.Request, user_id, temp_password=None) -> web.Response:
    """Set Temp Password

    Set Temp Password

    :param user_id: 
    :type user_id: str
    :param temp_password: 
    :type temp_password: str

    """
    return web.Response(status=200)


async def suspend_user(request: web.Request, user_id) -> web.Response:
    """Suspend User

    Suspend User

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def unlock_user(request: web.Request, user_id) -> web.Response:
    """Unlock User

    Unlock User

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def unsuspend_user(request: web.Request, user_id) -> web.Response:
    """Unsuspend User

    Unsuspend User

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)
