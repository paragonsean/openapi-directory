from typing import List, Dict
from aiohttp import web

from openapi_server.models.protection_container_resource_list import ProtectionContainerResourceList
from openapi_server import util


async def backup_protection_containers_list(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, filter=None) -> web.Response:
    """backup_protection_containers_list

    Lists the containers registered to Recovery Services Vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param filter: OData filter options.
    :type filter: str

    """
    return web.Response(status=200)
