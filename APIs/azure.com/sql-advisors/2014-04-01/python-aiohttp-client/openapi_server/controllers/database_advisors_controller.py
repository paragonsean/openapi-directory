from typing import List, Dict
from aiohttp import web

from openapi_server.models.advisor import Advisor
from openapi_server.models.advisor_list_result import AdvisorListResult
from openapi_server import util


async def database_advisors_create_or_update(request: web.Request, resource_group_name, server_name, database_name, advisor_name, subscription_id, api_version, parameters) -> web.Response:
    """database_advisors_create_or_update

    Creates or updates a database advisor.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param advisor_name: The name of the Database Advisor.
    :type advisor_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested advisor resource state.
    :type parameters: dict | bytes

    """
    parameters = Advisor.from_dict(parameters)
    return web.Response(status=200)


async def database_advisors_get(request: web.Request, resource_group_name, server_name, database_name, advisor_name, subscription_id, api_version) -> web.Response:
    """database_advisors_get

    Returns details of a Database Advisor.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param advisor_name: The name of the Database Advisor.
    :type advisor_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def database_advisors_list_by_database(request: web.Request, resource_group_name, server_name, database_name, subscription_id, api_version) -> web.Response:
    """database_advisors_list_by_database

    Returns a list of database advisors.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database.
    :type database_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
