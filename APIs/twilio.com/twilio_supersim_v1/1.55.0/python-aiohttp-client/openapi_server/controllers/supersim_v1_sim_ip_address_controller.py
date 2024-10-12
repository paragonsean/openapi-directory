from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_sim_ip_address_response import ListSimIpAddressResponse
from openapi_server import util


async def list_sim_ip_address(request: web.Request, sim_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_sim_ip_address

    Retrieve a list of IP Addresses for the given Super SIM.

    :param sim_sid: The SID of the Super SIM to list IP Addresses for.
    :type sim_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
