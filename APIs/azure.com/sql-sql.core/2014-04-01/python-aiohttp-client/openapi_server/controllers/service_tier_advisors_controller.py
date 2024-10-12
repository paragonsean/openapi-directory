from typing import List, Dict
from aiohttp import web

from openapi_server.models.service_tier_advisor import ServiceTierAdvisor
from openapi_server.models.service_tier_advisor_list_result import ServiceTierAdvisorListResult
from openapi_server import util


async def service_tier_advisors_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, service_tier_advisor_name) -> web.Response:
    """service_tier_advisors_get

    Gets a service tier advisor.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of database.
    :type database_name: str
    :param service_tier_advisor_name: The name of service tier advisor.
    :type service_tier_advisor_name: str

    """
    return web.Response(status=200)


async def service_tier_advisors_list_by_database(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name) -> web.Response:
    """service_tier_advisors_list_by_database

    Returns service tier advisors for specified database.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of database.
    :type database_name: str

    """
    return web.Response(status=200)
