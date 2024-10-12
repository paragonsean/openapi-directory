from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_cellular_gateway_uplink_statuses200_response_inner import GetOrganizationCellularGatewayUplinkStatuses200ResponseInner
from openapi_server.models.update_network_cellular_gateway_uplink_request import UpdateNetworkCellularGatewayUplinkRequest
from openapi_server import util


async def get_network_cellular_gateway_uplink_1(request: web.Request, network_id) -> web.Response:
    """Returns the uplink settings for your MG network.

    Returns the uplink settings for your MG network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_organization_cellular_gateway_uplink_statuses_1(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, iccids=None) -> web.Response:
    """List the uplink status of every Meraki MG cellular gateway in the organization

    List the uplink status of every Meraki MG cellular gateway in the organization

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of network IDs. The returned devices will be filtered to only include these networks.
    :type network_ids: List[str]
    :param serials: A list of serial numbers. The returned devices will be filtered to only include these serials.
    :type serials: List[str]
    :param iccids: A list of ICCIDs. The returned devices will be filtered to only include these ICCIDs.
    :type iccids: List[str]

    """
    return web.Response(status=200)


async def update_network_cellular_gateway_uplink_1(request: web.Request, network_id, body=None) -> web.Response:
    """Updates the uplink settings for your MG network.

    Updates the uplink settings for your MG network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkCellularGatewayUplinkRequest.from_dict(body)
    return web.Response(status=200)
