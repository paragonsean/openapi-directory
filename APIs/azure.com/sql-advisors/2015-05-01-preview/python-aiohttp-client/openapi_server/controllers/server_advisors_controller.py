from typing import List, Dict
from aiohttp import web

from openapi_server.models.advisor import Advisor
from openapi_server import util


async def server_advisors_get(request: web.Request, resource_group_name, server_name, advisor_name, subscription_id, api_version) -> web.Response:
    """server_advisors_get

    Gets a server advisor.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param advisor_name: The name of the Server Advisor.
    :type advisor_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def server_advisors_list_by_server(request: web.Request, resource_group_name, server_name, subscription_id, api_version) -> web.Response:
    """server_advisors_list_by_server

    Gets a list of server advisors.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def server_advisors_update(request: web.Request, resource_group_name, server_name, advisor_name, subscription_id, api_version, parameters) -> web.Response:
    """server_advisors_update

    Updates a server advisor.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param advisor_name: The name of the Server Advisor.
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
