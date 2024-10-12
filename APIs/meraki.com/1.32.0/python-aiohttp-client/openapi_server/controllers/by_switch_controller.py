from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_switch_ports_by_switch200_response_inner import GetOrganizationSwitchPortsBySwitch200ResponseInner
from openapi_server import util


async def get_organization_switch_ports_by_switch_2(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, port_profile_ids=None, name=None, mac=None, macs=None, serial=None, serials=None, configuration_updated_after=None) -> web.Response:
    """List the switchports in an organization by switch

    List the switchports in an organization by switch

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 50. Default is 50.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter switchports by network.
    :type network_ids: List[str]
    :param port_profile_ids: Optional parameter to filter switchports belonging to the specified switchport profiles.
    :type port_profile_ids: List[str]
    :param name: Optional parameter to filter switchports belonging to switches by name. All returned switches will have a name that contains the search term or is an exact match.
    :type name: str
    :param mac: Optional parameter to filter switchports belonging to switches by MAC address. All returned switches will have a MAC address that contains the search term or is an exact match.
    :type mac: str
    :param macs: Optional parameter to filter switchports by one or more MAC addresses belonging to devices. All switchports returned belong to MAC addresses of switches that are an exact match.
    :type macs: List[str]
    :param serial: Optional parameter to filter switchports belonging to switches by serial number. All returned switches will have a serial number that contains the search term or is an exact match.
    :type serial: str
    :param serials: Optional parameter to filter switchports belonging to switches with one or more serial numbers. All switchports returned belong to serial numbers of switches that are an exact match.
    :type serials: List[str]
    :param configuration_updated_after: Optional parameter to filter results by switches where the configuration has been updated after the given timestamp.
    :type configuration_updated_after: str

    """
    return web.Response(status=200)
