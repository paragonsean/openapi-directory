from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_network_access_profile_response import ListNetworkAccessProfileResponse
from openapi_server.models.supersim_v1_network_access_profile import SupersimV1NetworkAccessProfile
from openapi_server import util


async def create_network_access_profile(request: web.Request, networks=None, unique_name=None) -> web.Response:
    """create_network_access_profile

    Create a new Network Access Profile

    :param networks: List of Network SIDs that this Network Access Profile will allow connections to.
    :type networks: List[str]
    :param unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource.
    :type unique_name: str

    """
    return web.Response(status=200)


async def fetch_network_access_profile(request: web.Request, sid) -> web.Response:
    """fetch_network_access_profile

    Fetch a Network Access Profile instance from your account.

    :param sid: The SID of the Network Access Profile resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_network_access_profile(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_network_access_profile

    Retrieve a list of Network Access Profiles from your account.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_network_access_profile(request: web.Request, sid, unique_name=None) -> web.Response:
    """update_network_access_profile

    Updates the given properties of a Network Access Profile in your account.

    :param sid: The SID of the Network Access Profile to update.
    :type sid: str
    :param unique_name: The new unique name of the Network Access Profile.
    :type unique_name: str

    """
    return web.Response(status=200)
