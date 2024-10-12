from typing import List, Dict
from aiohttp import web

from openapi_server.models.area_request import AreaRequest
from openapi_server.models.path_request import PathRequest
from openapi_server.models.points_request import PointsRequest
from openapi_server import util


async def area(request: web.Request, body) -> web.Response:
    """Create a point-to-multipoint heatmap

    An area coverage assumes the same receiver height at all locations out to fixed radius (maximum 300km). Due to it&#39;s exhaustive processing it is the slowest of all the API calls. Speed can be improved significantly by adjusting the resolution &#39;res&#39; parameter. A basic request needs transmitter, receiver, antenna and output objects defined as a minimum. Model and environment options will enhance accuracy.

    :param body: A basic request needs transmitter, receiver, antenna and output objects defined as a minimum. Model and environment options will enhance accuracy.
    :type body: dict | bytes

    """
    body = AreaRequest.from_dict(body)
    return web.Response(status=200)


async def path(request: web.Request, body) -> web.Response:
    """Point-to-point path profile analysis (Tx to Rx)

    A path profile is a single link from A to B. It is much faster than an area calculation and can be used out to 300km. A basic request needs transmitter, receiver, antenna and output objects defined as a minimum. Model and environment options will enhance accuracy.

    :param body: A basic request needs transmitter, receiver, antenna and output objects defined as a minimum. Model and environment options will enhance accuracy.
    :type body: dict | bytes

    """
    body = PathRequest.from_dict(body)
    return web.Response(status=200)


async def points(request: web.Request, body) -> web.Response:
    """Point-to-multipoint path profile analysis (Many Tx, one Rx)

    The points function tests many transmitters and one receiver and is designed for route analysis. A minimal request needs a transmitters array of (latitude,longitude,altitude) locations, antenna, receiver and output objects defined as a minimum. Model and environment options will enhance accuracy.

    :param body: A minimal request needs a transmitters array of (latitude,longitude,altitude) locations, antenna, receiver and output objects defined as a minimum. Model and environment options will enhance accuracy.
    :type body: dict | bytes

    """
    body = PointsRequest.from_dict(body)
    return web.Response(status=200)
