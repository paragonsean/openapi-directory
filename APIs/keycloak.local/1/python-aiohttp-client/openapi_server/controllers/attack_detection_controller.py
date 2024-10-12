from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def realm_attack_detection_brute_force_users_delete(request: web.Request, realm) -> web.Response:
    """Clear any user login failures for all users   This can release temporary disabled users

    

    :param realm: realm name (not id!)
    :type realm: str

    """
    return web.Response(status=200)


async def realm_attack_detection_brute_force_users_user_id_delete(request: web.Request, realm, user_id) -> web.Response:
    """Clear any user login failures for the user   This can release temporary disabled user

    

    :param realm: realm name (not id!)
    :type realm: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def realm_attack_detection_brute_force_users_user_id_get(request: web.Request, realm, user_id) -> web.Response:
    """Get status of a username in brute force detection

    

    :param realm: realm name (not id!)
    :type realm: str
    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)
