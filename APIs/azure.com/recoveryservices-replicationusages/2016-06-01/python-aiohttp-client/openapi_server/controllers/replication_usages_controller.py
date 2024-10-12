from typing import List, Dict
from aiohttp import web

from openapi_server.models.replication_usage_list import ReplicationUsageList
from openapi_server import util


async def replication_usages_list(request: web.Request, subscription_id, api_version, resource_group_name, vault_name) -> web.Response:
    """replication_usages_list

    Fetches the replication usages of the vault.

    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str

    """
    return web.Response(status=200)
