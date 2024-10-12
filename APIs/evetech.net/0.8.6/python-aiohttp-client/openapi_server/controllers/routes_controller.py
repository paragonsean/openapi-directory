from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.error_limited import ErrorLimited
from openapi_server.models.gateway_timeout import GatewayTimeout
from openapi_server.models.get_route_origin_destination_not_found import GetRouteOriginDestinationNotFound
from openapi_server.models.internal_server_error import InternalServerError
from openapi_server.models.service_unavailable import ServiceUnavailable
from openapi_server import util


async def get_route_origin_destination(request: web.Request, destination, origin, avoid=None, connections=None, datasource=None, flag=None, if_none_match=None) -> web.Response:
    """Get route

    Get the systems between origin and destination  --- Alternate route: &#x60;/dev/route/{origin}/{destination}/&#x60;  Alternate route: &#x60;/legacy/route/{origin}/{destination}/&#x60;  Alternate route: &#x60;/v1/route/{origin}/{destination}/&#x60;  --- This route is cached for up to 86400 seconds

    :param destination: destination solar system ID
    :type destination: int
    :param origin: origin solar system ID
    :type origin: int
    :param avoid: avoid solar system ID(s)
    :type avoid: List[int]
    :param connections: connected solar system pairs
    :type connections: List[]
    :param datasource: The server name you would like data from
    :type datasource: str
    :param flag: route security preference
    :type flag: str
    :param if_none_match: ETag from a previous request. A 304 will be returned if this matches the current ETag
    :type if_none_match: str

    """
    return web.Response(status=200)
