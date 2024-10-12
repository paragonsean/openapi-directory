from typing import List, Dict
from aiohttp import web

from openapi_server.models.protection_container_resource import ProtectionContainerResource
from openapi_server.models.protection_container_resource_list import ProtectionContainerResourceList
from openapi_server import util


async def protection_containers_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name) -> web.Response:
    """protection_containers_get

    Gets details of the specific container registered to your Recovery Services vault.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param fabric_name: The fabric name associated with the container.
    :type fabric_name: str
    :param container_name: The container name used for this GET operation.
    :type container_name: str

    """
    return web.Response(status=200)


async def protection_containers_list(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, filter=None) -> web.Response:
    """protection_containers_list

    Lists the containers registered to the Recovery Services vault.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param filter: The following equation is used to sort or filter the containers registered to the vault. providerType eq {AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql} and status eq {Unknown, NotRegistered, Registered, Registering} and friendlyName eq {containername} and backupManagementType eq {AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql}.
    :type filter: str

    """
    return web.Response(status=200)


async def protection_containers_refresh(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name) -> web.Response:
    """protection_containers_refresh

    Discovers the containers in the subscription that can be protected in a Recovery Services vault. This is an asynchronous operation. To learn the status of the operation, use the GetRefreshOperationResult API.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param fabric_name: The fabric name associated with the container.
    :type fabric_name: str

    """
    return web.Response(status=200)
