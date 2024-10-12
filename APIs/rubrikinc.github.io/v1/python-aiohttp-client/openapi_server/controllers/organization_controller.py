from typing import List, Dict
from aiohttp import web

from openapi_server.models.envoy_bulk_update import EnvoyBulkUpdate
from openapi_server.models.envoy_create import EnvoyCreate
from openapi_server.models.envoy_detail_list import EnvoyDetailList
from openapi_server.models.envoy_id_list import EnvoyIdList
from openapi_server import util


async def bulk_create_envoys(request: web.Request, id, body) -> web.Response:
    """Create a list of Rubrik Envoy objects

    Create a list of Rubrik Envoy objects for a specified organization and specify the properties to assign to the Rubrik Envoy objects.

    :param id: ID assigned to an organization object.
    :type id: str
    :param body: Properties to assign to the Rubrik Envoy objects.
    :type body: list | bytes

    """
    body = [EnvoyCreate.from_dict(d) for d in body]
    return web.Response(status=200)


async def bulk_delete_envoys(request: web.Request, id, body) -> web.Response:
    """Remove a list of Rubrik Envoy objects

    Remove a list of Rubrik Envoy objects from an organization and delete the objects from the Rubrik cluster.

    :param id: ID assigned to an organization object.
    :type id: str
    :param body: A list of Rubrik Envoy objects IDs.
    :type body: dict | bytes

    """
    body = EnvoyIdList.from_dict(body)
    return web.Response(status=200)


async def bulk_update_envoys(request: web.Request, id, body) -> web.Response:
    """Update a list of Rubrik Envoy objects

    Change one or more of the properties of a list of Rubrik Envoy objects.

    :param id: ID assigned to an organization object.
    :type id: str
    :param body: Properties to assign to the Rubrik Envoy objects.
    :type body: list | bytes

    """
    body = [EnvoyBulkUpdate.from_dict(d) for d in body]
    return web.Response(status=200)
