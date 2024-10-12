from typing import List, Dict
from aiohttp import web

from openapi_server.models.hook import Hook
from openapi_server.models.hook_edit import HookEdit
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def hooks_id_json_delete(request: web.Request, login, authtoken, id) -> web.Response:
    """Delete an existing Hook.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Hook
    :type id: int

    """
    return web.Response(status=200)


async def hooks_id_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve a single Hook.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Hook
    :type id: int

    """
    return web.Response(status=200)


async def hooks_id_json_put(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Update a Hook.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Hook
    :type id: int
    :param body: Hook parameters.
    :type body: dict | bytes

    """
    body = HookEdit.from_dict(body)
    return web.Response(status=200)


async def hooks_json_get(request: web.Request, login, authtoken, limit=None, page=None) -> web.Response:
    """Retrieve all Hooks.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param limit: List restriction
    :type limit: int
    :param page: List page
    :type page: int

    """
    return web.Response(status=200)


async def hooks_json_post(request: web.Request, login, authtoken, body) -> web.Response:
    """Create a new Hook.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param body: Hook parameters.
    :type body: dict | bytes

    """
    body = HookEdit.from_dict(body)
    return web.Response(status=200)
