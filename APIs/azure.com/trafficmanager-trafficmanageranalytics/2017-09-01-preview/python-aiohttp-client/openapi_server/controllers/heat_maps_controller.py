from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.heat_map_model import HeatMapModel
from openapi_server import util


async def heat_map_get(request: web.Request, subscription_id, resource_group_name, profile_name, heat_map_type, api_version, top_left=None, bot_right=None) -> web.Response:
    """heat_map_get

    Gets latest heatmap for Traffic Manager profile.

    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group containing the Traffic Manager endpoint.
    :type resource_group_name: str
    :param profile_name: The name of the Traffic Manager profile.
    :type profile_name: str
    :param heat_map_type: The type of HeatMap for the Traffic Manager profile.
    :type heat_map_type: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param top_left: The top left latitude,longitude pair of the rectangular viewport to query for.
    :type top_left: List[float]
    :param bot_right: The bottom right latitude,longitude pair of the rectangular viewport to query for.
    :type bot_right: List[float]

    """
    return web.Response(status=200)
