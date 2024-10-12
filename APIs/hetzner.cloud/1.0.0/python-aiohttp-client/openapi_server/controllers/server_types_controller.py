from typing import List, Dict
from aiohttp import web

from openapi_server.models.server_types_get200_response import ServerTypesGet200Response
from openapi_server.models.server_types_id_get200_response import ServerTypesIdGet200Response
from openapi_server import util


async def server_types_get(request: web.Request, name=None) -> web.Response:
    """Get all Server Types

    Gets all Server type objects.

    :param name: Can be used to filter Server types by their name. The response will only contain the Server type matching the specified name.
    :type name: str

    """
    return web.Response(status=200)


async def server_types_id_get(request: web.Request, id) -> web.Response:
    """Get a Server Type

    Gets a specific Server type object.

    :param id: ID of Server Type
    :type id: int

    """
    return web.Response(status=200)
