from typing import List, Dict
from aiohttp import web

from openapi_server.models.access import Access
from openapi_server import util


async def permission_apps_app_id_delete(request: web.Request, app_id, user_id) -> web.Response:
    """Removes permission that allows the app to access this user&#39;s data

    

    :param app_id: The id of the app
    :type app_id: str
    :param user_id: The id of the user
    :type user_id: str

    """
    return web.Response(status=200)


async def permission_apps_app_id_get(request: web.Request, app_id, user_id) -> web.Response:
    """Returns permission that allows the app to access this user&#39;s data

    

    :param app_id: The id of the app
    :type app_id: str
    :param user_id: The id of the user
    :type user_id: str

    """
    return web.Response(status=200)


async def permission_apps_app_id_post(request: web.Request, app_id, user_id, _date=None, ip=None) -> web.Response:
    """Adds permission to allow the app to access this user&#39;s data

    

    :param app_id: The id of the app
    :type app_id: str
    :param user_id: The id of the user
    :type user_id: str
    :param _date: The time (in milliseconds) of when the user agreed to the access request
    :type _date: int
    :param ip: The ip address of the user agreeing to the access request
    :type ip: str

    """
    return web.Response(status=200)
