from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.routing_app_coverage_create_request import RoutingAppCoverageCreateRequest
from openapi_server.models.routing_app_coverage_response import RoutingAppCoverageResponse
from openapi_server.models.routing_app_coverage_update_request import RoutingAppCoverageUpdateRequest
from openapi_server import util


async def routing_app_coverages_create_instance(request: web.Request, body) -> web.Response:
    """routing_app_coverages_create_instance

    

    :param body: RoutingAppCoverage representation
    :type body: dict | bytes

    """
    body = RoutingAppCoverageCreateRequest.from_dict(body)
    return web.Response(status=200)


async def routing_app_coverages_delete_instance(request: web.Request, id) -> web.Response:
    """routing_app_coverages_delete_instance

    

    :param id: the id of the requested resource
    :type id: str

    """
    return web.Response(status=200)


async def routing_app_coverages_get_instance(request: web.Request, id, fields_routing_app_coverages=None, include=None) -> web.Response:
    """routing_app_coverages_get_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param fields_routing_app_coverages: the fields to include for returned resources of type routingAppCoverages
    :type fields_routing_app_coverages: List[str]
    :param include: comma-separated list of relationships to include
    :type include: List[str]

    """
    return web.Response(status=200)


async def routing_app_coverages_update_instance(request: web.Request, id, body) -> web.Response:
    """routing_app_coverages_update_instance

    

    :param id: the id of the requested resource
    :type id: str
    :param body: RoutingAppCoverage representation
    :type body: dict | bytes

    """
    body = RoutingAppCoverageUpdateRequest.from_dict(body)
    return web.Response(status=200)
