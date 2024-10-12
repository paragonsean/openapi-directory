from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection_role import ConnectionRole
from openapi_server import util


async def setup_connection_role_get(request: web.Request, ) -> web.Response:
    """Returns a list of connection roles

    Returns a list of connection roles you&#39;ve previously created. The connection roles are returned in sorted order, with the most recent connection role appearing first.


    """
    return web.Response(status=200)


async def setup_connection_role_id_delete(request: web.Request, id) -> web.Response:
    """Delete a connection role.

    Deletes the specified connection role.

    :param id: Connection role ID
    :type id: str

    """
    return web.Response(status=200)


async def setup_connection_role_id_get(request: web.Request, id) -> web.Response:
    """Return a connection role

    Returns a connection role

    :param id: Connection role ID
    :type id: str

    """
    return web.Response(status=200)


async def setup_connection_role_post(request: web.Request, ) -> web.Response:
    """Create or update a connection role

    Creates or updates the specified connection role by setting the values of the parameters passed. Any parameters not provided will be left unchanged.


    """
    return web.Response(status=200)
