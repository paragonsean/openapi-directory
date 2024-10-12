from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_error_template import DefaultErrorTemplate
from openapi_server.models.default_success_template import DefaultSuccessTemplate
from openapi_server import util


async def calls_participants_add(request: web.Request, token, id, users) -> web.Response:
    """calls_participants_add

    Registers new participants added to a Call.

    :param token: Authentication token. Requires scope: &#x60;calls:write&#x60;
    :type token: str
    :param id: &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method.
    :type id: str
    :param users: The list of users to add as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
    :type users: str

    """
    return web.Response(status=200)


async def calls_participants_remove(request: web.Request, token, id, users) -> web.Response:
    """calls_participants_remove

    Registers participants removed from a Call.

    :param token: Authentication token. Requires scope: &#x60;calls:write&#x60;
    :type token: str
    :param id: &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method.
    :type id: str
    :param users: The list of users to remove as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
    :type users: str

    """
    return web.Response(status=200)
