from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def interference(request: web.Request, network, name) -> web.Response:
    """Find the best server for overlapping coverage

    Merge and analyse sites within a network channel to determine the best server at a given location. Each site will be dynamically allocated a monochrome colour from a palette and the strongest signal promoted at a given location.

    :param network: Network name eg. Overlapping broadcast stations
    :type network: str
    :param name: Interference layer name eg. QRM_map
    :type name: str

    """
    return web.Response(status=200)


async def mesh(request: web.Request, network, name) -> web.Response:
    """Merge sites into a super layer.

    A merge of &#39;area&#39; calculations for a network to create a single super layer. Stronger signals are promoted over weaker ones. The same colour key must be used.

    :param network: Network name eg. 100_BLUE_repeaters_nationwide
    :type network: str
    :param name: Super layer name eg. National_map
    :type name: str

    """
    return web.Response(status=200)


async def network(request: web.Request, net, nam, lat, lon, alt, rxg=None) -> web.Response:
    """Find the best server for somewhere

    Query your network to find the best server(s) for a given receiver/customer location. A previously generated network is required.

    :param net: Network name
    :type net: str
    :param nam: Super layer name
    :type nam: str
    :param lat: Latitude in decimal degrees
    :type lat: float
    :param lon: Longitude in decimal degrees
    :type lon: float
    :param alt: Height above ground level in metres
    :type alt: int
    :param rxg: Receiver gain in dBi
    :type rxg: float

    """
    return web.Response(status=200)
