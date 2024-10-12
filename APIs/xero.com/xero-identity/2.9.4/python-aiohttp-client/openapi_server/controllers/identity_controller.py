from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection import Connection
from openapi_server import util


async def delete_connection(request: web.Request, id) -> web.Response:
    """Deletes a connection for this user (i.e. disconnect a tenant)

    Override the base server url that include version

    :param id: Unique identifier for retrieving single object
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_connections(request: web.Request, auth_event_id=None) -> web.Response:
    """Retrieves the connections for this user

    Override the base server url that include version

    :param auth_event_id: Filter by authEventId
    :type auth_event_id: str
    :type auth_event_id: str

    """
    return web.Response(status=200)
