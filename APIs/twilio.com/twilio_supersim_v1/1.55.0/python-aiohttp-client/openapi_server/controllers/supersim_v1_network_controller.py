from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_network_response import ListNetworkResponse
from openapi_server.models.supersim_v1_network import SupersimV1Network
from openapi_server import util


async def fetch_network(request: web.Request, sid) -> web.Response:
    """fetch_network

    Fetch a Network resource.

    :param sid: The SID of the Network resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_network(request: web.Request, iso_country=None, mcc=None, mnc=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_network

    Retrieve a list of Network resources.

    :param iso_country: The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the Network resources to read.
    :type iso_country: str
    :param mcc: The &#39;mobile country code&#39; of a country. Network resources with this &#x60;mcc&#x60; in their &#x60;identifiers&#x60; will be read.
    :type mcc: str
    :param mnc: The &#39;mobile network code&#39; of a mobile operator network. Network resources with this &#x60;mnc&#x60; in their &#x60;identifiers&#x60; will be read.
    :type mnc: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
