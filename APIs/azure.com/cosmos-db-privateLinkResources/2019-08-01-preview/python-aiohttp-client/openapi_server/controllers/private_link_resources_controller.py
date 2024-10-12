from typing import List, Dict
from aiohttp import web

from openapi_server.models.private_link_resource import PrivateLinkResource
from openapi_server.models.private_link_resource_list_result import PrivateLinkResourceListResult
from openapi_server import util


async def private_link_resources_get(request: web.Request, subscription_id, resource_group_name, api_version, account_name, group_name) -> web.Response:
    """private_link_resources_get

    Gets the private link resources that need to be created for a Cosmos DB account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str
    :param group_name: The name of the private link resource.
    :type group_name: str

    """
    return web.Response(status=200)


async def private_link_resources_list_by_database_account(request: web.Request, subscription_id, resource_group_name, api_version, account_name) -> web.Response:
    """private_link_resources_list_by_database_account

    Gets the private link resources that need to be created for a Cosmos DB account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param api_version: Version of the API to be used with the client request. The current version is 2019-08-01.
    :type api_version: str
    :param account_name: Cosmos DB database account name.
    :type account_name: str

    """
    return web.Response(status=200)
