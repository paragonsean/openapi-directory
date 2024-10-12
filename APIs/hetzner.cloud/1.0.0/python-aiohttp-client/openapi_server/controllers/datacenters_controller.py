from typing import List, Dict
from aiohttp import web

from openapi_server.models.datacenters_get200_response import DatacentersGet200Response
from openapi_server.models.datacenters_id_get200_response import DatacentersIdGet200Response
from openapi_server import util


async def datacenters_get(request: web.Request, name=None) -> web.Response:
    """Get all Datacenters

    Returns all Datacenter objects.

    :param name: Can be used to filter Datacenters by their name. The response will only contain the Datacenter matching the specified name. When the name does not match the Datacenter name format, an &#x60;invalid_input&#x60; error is returned.
    :type name: str

    """
    return web.Response(status=200)


async def datacenters_id_get(request: web.Request, id) -> web.Response:
    """Get a Datacenter

    Returns a specific Datacenter object.

    :param id: ID of Datacenter
    :type id: int

    """
    return web.Response(status=200)
