from typing import List, Dict
from aiohttp import web

from openapi_server.models.role_list_result import RoleListResult
from openapi_server import util


async def roles_list_by_hub(request: web.Request, resource_group_name, hub_name, api_version, subscription_id) -> web.Response:
    """roles_list_by_hub

    Gets all the roles for the hub.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param hub_name: The name of the hub.
    :type hub_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
