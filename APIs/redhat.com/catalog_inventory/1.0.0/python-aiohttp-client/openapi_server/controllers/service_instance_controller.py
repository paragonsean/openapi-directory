from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.service_instance import ServiceInstance
from openapi_server.models.service_instances_collection import ServiceInstancesCollection
from openapi_server import util


async def list_service_instances(request: web.Request, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List ServiceInstances

    Returns an array of ServiceInstance objects

    :param limit: The numbers of items to return per page.
    :type limit: int
    :param offset: The number of items to skip before starting to collect the result set.
    :type offset: int
    :param filter: Filter for querying collections.
    :type filter: dict | bytes
    :type filter: Dict[str, ]
    :param sort_by: The list of attribute and order to sort the result set by.
    :type sort_by: dict | bytes
    :type sort_by: Dict[str, ]

    """
    filter = .from_dict(filter)
    sort_by = .from_dict(sort_by)
    return web.Response(status=200)


async def show_service_instance(request: web.Request, id) -> web.Response:
    """Show an existing ServiceInstance

    Returns a ServiceInstance object

    :param id: ID of the resource
    :type id: str

    """
    return web.Response(status=200)
