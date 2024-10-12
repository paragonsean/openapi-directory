from typing import List, Dict
from aiohttp import web

from openapi_server.models.protection_container_resource import ProtectionContainerResource
from openapi_server import util


async def protection_containers_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name) -> web.Response:
    """protection_containers_get

    Gets details of the specific container registered to your Recovery Services Vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Name of the fabric where the container belongs.
    :type fabric_name: str
    :param container_name: Name of the container whose details need to be fetched.
    :type container_name: str

    """
    return web.Response(status=200)


async def protection_containers_inquire(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, filter=None) -> web.Response:
    """Inquires all the protectable items under the given container.

    This is an async operation and the results should be tracked using location header or Azure-async-url.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric Name associated with the container.
    :type fabric_name: str
    :param container_name: Name of the container in which inquiry needs to be triggered.
    :type container_name: str
    :param filter: OData filter options.
    :type filter: str

    """
    return web.Response(status=200)


async def protection_containers_refresh(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, filter=None) -> web.Response:
    """protection_containers_refresh

    Discovers all the containers in the subscription that can be backed up to Recovery Services Vault. This is an  asynchronous operation. To know the status of the operation, call GetRefreshOperationResult API.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated the container.
    :type fabric_name: str
    :param filter: OData filter options.
    :type filter: str

    """
    return web.Response(status=200)


async def protection_containers_register(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, parameters) -> web.Response:
    """protection_containers_register

    Registers the container with Recovery Services vault.  This is an asynchronous operation. To track the operation status, use location header to call get latest status of  the operation.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the container.
    :type fabric_name: str
    :param container_name: Name of the container to be registered.
    :type container_name: str
    :param parameters: Request body for operation
    :type parameters: dict | bytes

    """
    parameters = ProtectionContainerResource.from_dict(parameters)
    return web.Response(status=200)


async def protection_containers_unregister(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name) -> web.Response:
    """protection_containers_unregister

    Unregisters the given container from your Recovery Services Vault. This is an asynchronous operation. To determine  whether the backend service has finished processing the request, call Get Container Operation Result API.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Name of the fabric where the container belongs.
    :type fabric_name: str
    :param container_name: Name of the container which needs to be unregistered from the Recovery Services Vault.
    :type container_name: str

    """
    return web.Response(status=200)
