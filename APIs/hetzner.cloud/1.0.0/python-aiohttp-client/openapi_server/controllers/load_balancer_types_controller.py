from typing import List, Dict
from aiohttp import web

from openapi_server.models.load_balancer_types_get200_response import LoadBalancerTypesGet200Response
from openapi_server.models.load_balancer_types_id_get200_response import LoadBalancerTypesIdGet200Response
from openapi_server import util


async def load_balancer_types_get(request: web.Request, name=None) -> web.Response:
    """Get all Load Balancer Types

    Gets all Load Balancer type objects.

    :param name: Can be used to filter Load Balancer types by their name. The response will only contain the Load Balancer type matching the specified name.
    :type name: str

    """
    return web.Response(status=200)


async def load_balancer_types_id_get(request: web.Request, id) -> web.Response:
    """Get a Load Balancer Type

    Gets a specific Load Balancer type object.

    :param id: ID of Load Balancer type
    :type id: int

    """
    return web.Response(status=200)
