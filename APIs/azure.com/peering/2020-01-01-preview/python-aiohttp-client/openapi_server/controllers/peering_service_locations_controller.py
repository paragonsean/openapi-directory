from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peering_service_location_list_result import PeeringServiceLocationListResult
from openapi_server import util


async def peering_service_locations_list(request: web.Request, subscription_id, api_version, country=None) -> web.Response:
    """peering_service_locations_list

    Lists all of the available locations for peering service.

    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str
    :param country: The country of interest, in which the locations are to be present.
    :type country: str

    """
    return web.Response(status=200)
