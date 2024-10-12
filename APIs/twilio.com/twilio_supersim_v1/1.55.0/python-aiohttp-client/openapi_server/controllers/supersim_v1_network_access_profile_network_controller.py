from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_network_access_profile_network_response import ListNetworkAccessProfileNetworkResponse
from openapi_server.models.supersim_v1_network_access_profile_network_access_profile_network import SupersimV1NetworkAccessProfileNetworkAccessProfileNetwork
from openapi_server import util


async def create_network_access_profile_network(request: web.Request, network_access_profile_sid, network) -> web.Response:
    """create_network_access_profile_network

    Add a Network resource to the Network Access Profile resource.

    :param network_access_profile_sid: The unique string that identifies the Network Access Profile resource.
    :type network_access_profile_sid: str
    :param network: The SID of the Network resource to be added to the Network Access Profile resource.
    :type network: str

    """
    return web.Response(status=200)


async def delete_network_access_profile_network(request: web.Request, network_access_profile_sid, sid) -> web.Response:
    """delete_network_access_profile_network

    Remove a Network resource from the Network Access Profile resource&#39;s.

    :param network_access_profile_sid: The unique string that identifies the Network Access Profile resource.
    :type network_access_profile_sid: str
    :param sid: The SID of the Network resource to be removed from the Network Access Profile resource.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_network_access_profile_network(request: web.Request, network_access_profile_sid, sid) -> web.Response:
    """fetch_network_access_profile_network

    Fetch a Network Access Profile resource&#39;s Network resource.

    :param network_access_profile_sid: The unique string that identifies the Network Access Profile resource.
    :type network_access_profile_sid: str
    :param sid: The SID of the Network resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_network_access_profile_network(request: web.Request, network_access_profile_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_network_access_profile_network

    Retrieve a list of Network Access Profile resource&#39;s Network resource.

    :param network_access_profile_sid: The unique string that identifies the Network Access Profile resource.
    :type network_access_profile_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
