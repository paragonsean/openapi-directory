from typing import List, Dict
from aiohttp import web

from openapi_server.models.capabilities_result import CapabilitiesResult
from openapi_server import util


async def location_get_capabilities(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """location_get_capabilities

    Gets the capabilities for the specified location.

    :param location: The location to get capabilities for.
    :type location: str
    :param api_version: The HDInsight client API Version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
