from typing import List, Dict
from aiohttp import web

from openapi_server.models.workload_protectable_item_resource_list import WorkloadProtectableItemResourceList
from openapi_server import util


async def protectable_items_list(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, filter=None, skip_token=None) -> web.Response:
    """protectable_items_list

    Based on the query filter and the pagination parameters, this operation provides a pageable list of objects within the subscription that can be protected.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param filter: Using the following query filters, you can sort a specific backup item based on: type of backup item, status, name of the item, and more.  providerType eq { AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql } and status eq { NotProtected , Protecting , Protected } and friendlyName {name} and skipToken eq {string which provides the next set of list} and topToken eq {int} and backupManagementType eq { AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql }.
    :type filter: str
    :param skip_token: The Skip Token filter.
    :type skip_token: str

    """
    return web.Response(status=200)
