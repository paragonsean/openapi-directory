from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_engine_base_resource import BackupEngineBaseResource
from openapi_server.models.backup_engine_base_resource_list import BackupEngineBaseResourceList
from openapi_server import util


async def backup_engines_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, backup_engine_name, filter=None, skip_token=None) -> web.Response:
    """backup_engines_get

    Returns backup management server registered to Recovery Services Vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param backup_engine_name: Name of the backup management server.
    :type backup_engine_name: str
    :param filter: OData filter options.
    :type filter: str
    :param skip_token: skipToken Filter.
    :type skip_token: str

    """
    return web.Response(status=200)


async def backup_engines_list(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, filter=None, skip_token=None) -> web.Response:
    """backup_engines_list

    Backup management servers registered to Recovery Services Vault. Returns a pageable list of servers.

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
    :param skip_token: skipToken Filter.
    :type skip_token: str

    """
    return web.Response(status=200)
