from typing import List, Dict
from aiohttp import web

from openapi_server.models.express_route_service_provider_list_result import ExpressRouteServiceProviderListResult
from openapi_server import util


async def express_route_service_providers_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """express_route_service_providers_list

    The List ExpressRouteServiceProvider operation retrieves all the available ExpressRouteServiceProviders.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
