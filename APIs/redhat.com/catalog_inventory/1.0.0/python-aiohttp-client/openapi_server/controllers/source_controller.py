from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.service_instances_collection import ServiceInstancesCollection
from openapi_server.models.service_inventories_collection import ServiceInventoriesCollection
from openapi_server.models.service_offering_nodes_collection import ServiceOfferingNodesCollection
from openapi_server.models.service_offerings_collection import ServiceOfferingsCollection
from openapi_server.models.service_plans_collection import ServicePlansCollection
from openapi_server.models.source import Source
from openapi_server.models.sources_collection import SourcesCollection
from openapi_server.models.tasks_collection import TasksCollection
from openapi_server import util


async def incremental_refresh_source(request: web.Request, id) -> web.Response:
    """Incremental Refresh an existing Source

    Incremental Refresh a source object

    :param id: ID of the resource
    :type id: str

    """
    return web.Response(status=200)


async def list_source_service_instances(request: web.Request, id, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List ServiceInstances for Source

    Returns an array of ServiceInstance objects

    :param id: ID of the resource
    :type id: str
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


async def list_source_service_inventories(request: web.Request, id, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List ServiceInventories for Source

    Returns an array of ServiceInventory objects

    :param id: ID of the resource
    :type id: str
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


async def list_source_service_offering_nodes(request: web.Request, id, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List ServiceOfferingNodes for Source

    Returns an array of ServiceOfferingNode objects

    :param id: ID of the resource
    :type id: str
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


async def list_source_service_offerings(request: web.Request, id, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List ServiceOfferings for Source

    Returns an array of ServiceOffering objects

    :param id: ID of the resource
    :type id: str
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


async def list_source_service_plans(request: web.Request, id, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List ServicePlans for Source

    Returns an array of ServicePlan objects

    :param id: ID of the resource
    :type id: str
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


async def list_source_tasks(request: web.Request, id, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List Tasks for Source

    Returns an array of Task objects

    :param id: ID of the resource
    :type id: str
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


async def list_sources(request: web.Request, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List Sources

    Returns an array of Source objects

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


async def refresh_source(request: web.Request, id) -> web.Response:
    """ Refresh an existing Source

    Refresh a source object

    :param id: ID of the resource
    :type id: str

    """
    return web.Response(status=200)


async def show_source(request: web.Request, id) -> web.Response:
    """Show an existing Source

    Returns a Source object

    :param id: ID of the resource
    :type id: str

    """
    return web.Response(status=200)
