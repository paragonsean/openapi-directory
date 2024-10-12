from typing import List, Dict
from aiohttp import web

from openapi_server.models.location_capabilities import LocationCapabilities
from openapi_server import util


async def capabilities_list_by_location(request: web.Request, location_name, subscription_id, api_version) -> web.Response:
    """capabilities_list_by_location

    Gets the subscription capabilities available for the specified location.

    :param location_name: The location name whose capabilities are retrieved.
    :type location_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
