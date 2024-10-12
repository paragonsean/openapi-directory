from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.peering_list_result import PeeringListResult
from openapi_server import util


async def legacy_peerings_list(request: web.Request, peering_location, kind, subscription_id, api_version) -> web.Response:
    """legacy_peerings_list

    Lists all of the legacy peerings under the given subscription matching the specified kind and location.

    :param peering_location: The location of the peering.
    :type peering_location: str
    :param kind: The kind of the peering.
    :type kind: str
    :param subscription_id: The Azure subscription ID.
    :type subscription_id: str
    :param api_version: The client API version.
    :type api_version: str

    """
    return web.Response(status=200)
