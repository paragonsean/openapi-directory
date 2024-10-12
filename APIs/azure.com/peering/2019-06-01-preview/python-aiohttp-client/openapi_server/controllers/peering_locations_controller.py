from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peering_location_list_result import PeeringLocationListResult
from openapi_server import util


async def peering_locations_list(request: web.Request, kind, subscription_id, api_version) -> web.Response:
    """peering_locations_list

    Lists all of the available peering locations for the specified kind of peering.

    :param kind: The kind of the peering.
    :type kind: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)
