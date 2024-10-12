from typing import List, Dict
from aiohttp import web

from openapi_server.models.infra_role import InfraRole
from openapi_server.models.infra_role_list import InfraRoleList
from openapi_server import util


async def infra_roles_get(request: web.Request, subscription_id, resource_group_name, location, infra_role, api_version) -> web.Response:
    """infra_roles_get

    Returns the requested infrastructure role description.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param infra_role: Infrastructure role name.
    :type infra_role: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def infra_roles_list(request: web.Request, subscription_id, resource_group_name, location, api_version, filter=None) -> web.Response:
    """infra_roles_list

    Returns a list of all infrastructure roles at a location.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: OData filter parameter.
    :type filter: str

    """
    return web.Response(status=200)
