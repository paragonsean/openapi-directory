from typing import List, Dict
from aiohttp import web

from openapi_server.models.isos_get200_response import IsosGet200Response
from openapi_server.models.isos_id_get200_response import IsosIdGet200Response
from openapi_server import util


async def isos_get(request: web.Request, name=None, architecture=None, include_architecture_wildcard=None) -> web.Response:
    """Get all ISOs

    Returns all available ISO objects.

    :param name: Can be used to filter ISOs by their name. The response will only contain the ISO matching the specified name.
    :type name: str
    :param architecture: Return only ISOs with the given architecture.
    :type architecture: str
    :param include_architecture_wildcard: Include Images with wildcard architecture (architecture is null). Works only if architecture filter is specified.
    :type include_architecture_wildcard: bool

    """
    return web.Response(status=200)


async def isos_id_get(request: web.Request, id) -> web.Response:
    """Get an ISO

    Returns a specific ISO object.

    :param id: ID of the ISO
    :type id: int

    """
    return web.Response(status=200)
