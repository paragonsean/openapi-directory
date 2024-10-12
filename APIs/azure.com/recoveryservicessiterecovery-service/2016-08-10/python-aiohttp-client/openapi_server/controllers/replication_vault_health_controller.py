from typing import List, Dict
from aiohttp import web

from openapi_server.models.vault_health_details import VaultHealthDetails
from openapi_server import util


async def replication_vault_health_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id) -> web.Response:
    """Gets the health summary for the vault.

    Gets the health details of the vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)
