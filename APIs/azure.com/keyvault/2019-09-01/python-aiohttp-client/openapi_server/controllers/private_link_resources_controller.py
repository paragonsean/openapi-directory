from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.private_link_resource_list_result import PrivateLinkResourceListResult
from openapi_server import util


async def private_link_resources_list_by_vault(request: web.Request, subscription_id, resource_group_name, vault_name, api_version) -> web.Response:
    """private_link_resources_list_by_vault

    Gets the private link resources supported for the key vault.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group that contains the key vault.
    :type resource_group_name: str
    :param vault_name: The name of the key vault.
    :type vault_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
