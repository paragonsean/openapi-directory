from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.actions_response import ActionsResponse
from openapi_server import util


async def actions_get(request: web.Request, id=None, sort=None, status=None) -> web.Response:
    """Get all Actions

    Returns all Action objects. You can &#x60;sort&#x60; the results by using the sort URI parameter, and filter them with the &#x60;status&#x60; parameter.

    :param id: Can be used multiple times, the response will contain only Actions with specified IDs
    :type id: int
    :param sort: Can be used multiple times.
    :type sort: str
    :param status: Can be used multiple times, the response will contain only Actions with specified statuses
    :type status: str

    """
    return web.Response(status=200)


async def actions_id_get(request: web.Request, id) -> web.Response:
    """Get an Action

    Returns a specific Action object.

    :param id: ID of the Resource
    :type id: int

    """
    return web.Response(status=200)
