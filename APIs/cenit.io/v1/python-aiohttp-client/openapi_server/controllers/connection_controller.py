from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection import Connection
from openapi_server import util


async def setup_connection_get(request: web.Request, ) -> web.Response:
    """Returns a list of connections

    Returns a list of connections you&#39;ve previously created. The connections are returned in sorted order, with the most recent connection appearing first.


    """
    return web.Response(status=200)


async def setup_connection_id_delete(request: web.Request, id) -> web.Response:
    """Delete a connection

    Permanently deletes a connection. It cannot be undone.

    :param id: Connection ID
    :type id: str

    """
    return web.Response(status=200)


async def setup_connection_id_get(request: web.Request, id) -> web.Response:
    """Retrieve an existing connection

    Retrieves the details of an existing connection. You need only supply the unique connection identifier that was returned upon connection creation.

    :param id: Connection ID
    :type id: str

    """
    return web.Response(status=200)


async def setup_connection_post(request: web.Request, ) -> web.Response:
    """Create or update a connection

    Creates or updates the specified connection by setting the values of the parameters passed. Any parameters not provided will be left unchanged.


    """
    return web.Response(status=200)
