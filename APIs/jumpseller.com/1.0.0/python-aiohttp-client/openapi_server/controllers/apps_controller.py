from typing import List, Dict
from aiohttp import web

from openapi_server.models.app import App
from openapi_server.models.js_app import JSApp
from openapi_server.models.js_app_edit import JSAppEdit
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def jsapps_code_json_delete(request: web.Request, login, authtoken, code) -> web.Response:
    """Delete an existing JSApp.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param code: Code of the App
    :type code: str

    """
    return web.Response(status=200)


async def jsapps_code_json_get(request: web.Request, login, authtoken, code) -> web.Response:
    """Retrieve a JSApp.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param code: Code of the App
    :type code: str

    """
    return web.Response(status=200)


async def jsapps_json_get(request: web.Request, login, authtoken) -> web.Response:
    """Retrieve all the Store&#39;s JSApps.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str

    """
    return web.Response(status=200)


async def jsapps_json_post(request: web.Request, login, authtoken, body) -> web.Response:
    """Create a Store JSApp.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param body: JSApp parameters to create
    :type body: dict | bytes

    """
    body = JSAppEdit.from_dict(body)
    return web.Response(status=200)
