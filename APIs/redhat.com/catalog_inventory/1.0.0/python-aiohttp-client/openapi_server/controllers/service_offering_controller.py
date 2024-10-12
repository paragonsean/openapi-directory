from typing import List, Dict
from aiohttp import web

from openapi_server.models.applied_inventories_parameters_service_plan import AppliedInventoriesParametersServicePlan
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.order_parameters_service_offering import OrderParametersServiceOffering
from openapi_server.models.order_service_offering200_response import OrderServiceOffering200Response
from openapi_server.models.service_instances_collection import ServiceInstancesCollection
from openapi_server.models.service_offering import ServiceOffering
from openapi_server.models.service_offering_nodes_collection import ServiceOfferingNodesCollection
from openapi_server.models.service_offerings_collection import ServiceOfferingsCollection
from openapi_server.models.service_plans_collection import ServicePlansCollection
from openapi_server.models.tag import Tag
from openapi_server import util


async def applied_inventories_tags_for_service_offering(request: web.Request, id, body) -> web.Response:
    """Invokes computing of ServiceInventories tags for given ServiceOffering

    Returns an array of inventories tags

    :param id: ID of the resource
    :type id: str
    :param body: Parameters defining input data for computing inventories
    :type body: dict | bytes

    """
    body = AppliedInventoriesParametersServicePlan.from_dict(body)
    return web.Response(status=200)


async def list_service_offering_service_instances(request: web.Request, id, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List ServiceInstances for ServiceOffering

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


async def list_service_offering_service_offering_nodes(request: web.Request, id, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List ServiceOfferingNodes for ServiceOffering

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


async def list_service_offering_service_plans(request: web.Request, id, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List ServicePlans for ServiceOffering

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


async def list_service_offerings(request: web.Request, limit=None, offset=None, filter=None, sort_by=None) -> web.Response:
    """List ServiceOfferings

    Returns an array of ServiceOffering objects

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


async def order_service_offering(request: web.Request, id, body) -> web.Response:
    """Order an existing ServiceOffering

    Returns a Task id

    :param id: ID of the resource
    :type id: str
    :param body: Order parameters defining the service and provider control
    :type body: dict | bytes

    """
    body = OrderParametersServiceOffering.from_dict(body)
    return web.Response(status=200)


async def show_service_offering(request: web.Request, id) -> web.Response:
    """Show an existing ServiceOffering

    Returns a ServiceOffering object

    :param id: ID of the resource
    :type id: str

    """
    return web.Response(status=200)
