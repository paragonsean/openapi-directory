from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_sm_user_access_devices200_response_inner import GetNetworkSmUserAccessDevices200ResponseInner
from openapi_server import util


async def delete_network_sm_user_access_device_1(request: web.Request, network_id, user_access_device_id) -> web.Response:
    """Delete a User Access Device

    Delete a User Access Device

    :param network_id: 
    :type network_id: str
    :param user_access_device_id: 
    :type user_access_device_id: str

    """
    return web.Response(status=200)


async def get_network_sm_user_access_devices_1(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """List User Access Devices and its Trusted Access Connections

    List User Access Devices and its Trusted Access Connections

    :param network_id: 
    :type network_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)
