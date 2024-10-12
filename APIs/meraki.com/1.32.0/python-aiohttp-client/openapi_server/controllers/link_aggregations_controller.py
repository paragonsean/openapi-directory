from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_switch_link_aggregation_request import CreateNetworkSwitchLinkAggregationRequest
from openapi_server.models.update_network_switch_link_aggregation_request import UpdateNetworkSwitchLinkAggregationRequest
from openapi_server import util


async def create_network_switch_link_aggregation_1(request: web.Request, network_id, body=None) -> web.Response:
    """Create a link aggregation group

    Create a link aggregation group

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchLinkAggregationRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_switch_link_aggregation_1(request: web.Request, network_id, link_aggregation_id) -> web.Response:
    """Split a link aggregation group into separate ports

    Split a link aggregation group into separate ports

    :param network_id: 
    :type network_id: str
    :param link_aggregation_id: 
    :type link_aggregation_id: str

    """
    return web.Response(status=200)


async def get_network_switch_link_aggregations_1(request: web.Request, network_id) -> web.Response:
    """List link aggregation groups

    List link aggregation groups

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_switch_link_aggregation_1(request: web.Request, network_id, link_aggregation_id, body=None) -> web.Response:
    """Update a link aggregation group

    Update a link aggregation group

    :param network_id: 
    :type network_id: str
    :param link_aggregation_id: 
    :type link_aggregation_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchLinkAggregationRequest.from_dict(body)
    return web.Response(status=200)
