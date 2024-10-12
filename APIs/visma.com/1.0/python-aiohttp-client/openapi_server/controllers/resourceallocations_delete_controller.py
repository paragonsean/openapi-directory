from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server import util


async def resource_allocations_delete_resource_allocation(request: web.Request, guid) -> web.Response:
    """Delete an resource allocation

    Returns: No Content (204) if succeeded. Not found (404) if resource allocation can&#39;t be found.

    :param guid: ID of the resource allocation to delete
    :type guid: str

    """
    return web.Response(status=200)


async def role_allocations_delete_role_allocation(request: web.Request, guid) -> web.Response:
    """Delete a role allocation.

    Returns: No Content (204) if succeeded. Not found (404) if role can&#39;t be found.

    :param guid: ID for the role allocation to delete.
    :type guid: str

    """
    return web.Response(status=200)
