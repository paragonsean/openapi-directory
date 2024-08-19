from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.traffic_manager_geographic_hierarchy import TrafficManagerGeographicHierarchy
from openapi_server import util


async def geographic_hierarchies_get_default(request: web.Request, api_version) -> web.Response:
    """geographic_hierarchies_get_default

    Gets the default Geographic Hierarchy used by the Geographic traffic routing method.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
