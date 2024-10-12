from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def contacts_get(request: web.Request, action, _json=None) -> web.Response:
    """contacts_get

    

    :param action: Determines the action to execute.
    :type action: str
    :param _json: Defines whether to return the response as JSON or CSV separated by semicolon.
    :type _json: 

    """
    return web.Response(status=200)


async def contacts_post(request: web.Request, action, _json=None, id=None, nick=None, empfaenger=None, email=None) -> web.Response:
    """contacts_post

    

    :param action: Determines the action to execute.
    :type action: str
    :param _json: Defines whether to return the response as JSON or CSV separated by semicolon.
    :type _json: 
    :param id: The contact ID for editing/deletion.
    :type id: str
    :param nick: The contacts name.
    :type nick: str
    :param empfaenger: The contacts phone number.
    :type empfaenger: str
    :param email: The contacts email address.
    :type email: str

    """
    return web.Response(status=200)
