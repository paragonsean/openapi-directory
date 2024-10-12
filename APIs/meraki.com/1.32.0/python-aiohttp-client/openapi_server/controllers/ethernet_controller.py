from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_wireless_devices_ethernet_statuses200_response_inner import GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner
from openapi_server import util


async def get_organization_wireless_devices_ethernet_statuses_2(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None) -> web.Response:
    """Endpoint to see power status for wireless devices

    Endpoint to see power status for wireless devices

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: A list of Meraki network IDs to filter results to contain only specified networks. E.g.: networkIds[]&#x3D;N_12345678&amp;networkIds[]&#x3D;L_3456
    :type network_ids: List[str]

    """
    return web.Response(status=200)
