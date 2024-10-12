from typing import List, Dict
from aiohttp import web

from openapi_server.models.namespace import Namespace
from openapi_server import util


async def setup_namespace_get(request: web.Request, ) -> web.Response:
    """Returns a list of namespaces

    Returns a list of namespaces you&#39;ve previously created. The namespaces are returned in sorted order, with the most recent namespace appearing first.


    """
    return web.Response(status=200)


async def setup_namespace_id_delete(request: web.Request, id) -> web.Response:
    """Delete a namespace

    Deletes the specified namespace.

    :param id: Namespace ID.
    :type id: str

    """
    return web.Response(status=200)


async def setup_namespace_id_get(request: web.Request, id) -> web.Response:
    """Retrieve an existing namespace

    Retrieves the details of an existing namespace. You need only supply the unique webhook namespace that was returned upon namespace creation.

    :param id: Namespace ID.
    :type id: str

    """
    return web.Response(status=200)


async def setup_namespace_post(request: web.Request, ) -> web.Response:
    """Create or update a namespace

    Creates or updates the specified namespace. Any parameters not provided will be left unchanged.


    """
    return web.Response(status=200)
