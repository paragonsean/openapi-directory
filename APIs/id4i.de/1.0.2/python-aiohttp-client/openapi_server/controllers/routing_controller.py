from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.route import Route
from openapi_server.models.routing_file import RoutingFile
from openapi_server.models.routing_file_request import RoutingFileRequest
from openapi_server import util


async def get_all_routes(request: web.Request, id4n, type, organization_id=None, interpolate=None) -> web.Response:
    """Retrieve all routes of a GUID (or ID4N)

    

    :param id4n: id4n
    :type id4n: str
    :param type: The type of route you want to have
    :type type: str
    :param organization_id: organizationId
    :type organization_id: str
    :param interpolate: interpolate
    :type interpolate: bool

    """
    return web.Response(status=200)


async def get_route(request: web.Request, id4n, type, private_routes=None, public_routes=None, interpolate=None) -> web.Response:
    """Retrieve current route of a GUID (or ID4N)

    

    :param id4n: id4n
    :type id4n: str
    :param type: The type of route you want to have
    :type type: str
    :param private_routes: privateRoutes
    :type private_routes: bool
    :param public_routes: publicRoutes
    :type public_routes: bool
    :param interpolate: interpolate
    :type interpolate: bool

    """
    return web.Response(status=200)


async def get_routing_file(request: web.Request, id4n, organization_id=None) -> web.Response:
    """Retrieve routing file

    

    :param id4n: id4n
    :type id4n: str
    :param organization_id: organizationId
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_routing_file(request: web.Request, id4n, body) -> web.Response:
    """Store routing file

    

    :param id4n: id4n
    :type id4n: str
    :param body: rfr
    :type body: dict | bytes

    """
    body = RoutingFileRequest.from_dict(body)
    return web.Response(status=200)
