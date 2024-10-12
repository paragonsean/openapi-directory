from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_engine_base_resource_list import BackupEngineBaseResourceList
from openapi_server import util


async def backup_engines_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, filter=None, skip_token=None) -> web.Response:
    """backup_engines_get

    The backup management servers registered to a Recovery Services vault. This returns a pageable list of servers.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param filter: Use this filter to choose the specific backup management server. backupManagementType { AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql }.
    :type filter: str
    :param skip_token: The Skip Token filter.
    :type skip_token: str

    """
    return web.Response(status=200)
