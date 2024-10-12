from typing import List, Dict
from aiohttp import web

from openapi_server.models.location_capabilities import LocationCapabilities
from openapi_server import util


async def capabilities_list_by_location(request: web.Request, api_version, subscription_id, location_id) -> web.Response:
    """capabilities_list_by_location

    Gets the capabilities available for the specified location.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param location_id: The location id whose capabilities are retrieved.
    :type location_id: str

    """
    return web.Response(status=200)
