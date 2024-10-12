from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_recovery_services_provider_input import AddRecoveryServicesProviderInput
from openapi_server.models.recovery_services_provider import RecoveryServicesProvider
from openapi_server.models.recovery_services_provider_collection import RecoveryServicesProviderCollection
from openapi_server import util


async def replication_recovery_services_providers_create(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, provider_name, add_provider_input) -> web.Response:
    """Adds a recovery services provider.

    The operation to add a recovery services provider.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param provider_name: Recovery services provider name.
    :type provider_name: str
    :param add_provider_input: Add provider input.
    :type add_provider_input: dict | bytes

    """
    add_provider_input = AddRecoveryServicesProviderInput.from_dict(add_provider_input)
    return web.Response(status=200)


async def replication_recovery_services_providers_delete(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, provider_name) -> web.Response:
    """Deletes provider from fabric. Note: Deleting provider for any fabric other than SingleHost is unsupported. To maintain backward compatibility for released clients the object \&quot;deleteRspInput\&quot; is used (if the object is empty we assume that it is old client and continue the old behavior).

    The operation to removes/delete(unregister) a recovery services provider from the vault

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param provider_name: Recovery services provider name.
    :type provider_name: str

    """
    return web.Response(status=200)


async def replication_recovery_services_providers_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, provider_name) -> web.Response:
    """Gets the details of a recovery services provider.

    Gets the details of registered recovery services provider.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param provider_name: Recovery services provider name
    :type provider_name: str

    """
    return web.Response(status=200)


async def replication_recovery_services_providers_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id) -> web.Response:
    """Gets the list of registered recovery services providers in the vault. This is a view only api.

    Lists the registered recovery services providers in the vault

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


async def replication_recovery_services_providers_list_by_replication_fabrics(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name) -> web.Response:
    """Gets the list of registered recovery services providers for the fabric.

    Lists the registered recovery services providers for the specified fabric.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name
    :type fabric_name: str

    """
    return web.Response(status=200)


async def replication_recovery_services_providers_purge(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, provider_name) -> web.Response:
    """Purges recovery service provider from fabric

    The operation to purge(force delete) a recovery services provider from the vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param provider_name: Recovery services provider name.
    :type provider_name: str

    """
    return web.Response(status=200)


async def replication_recovery_services_providers_refresh_provider(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, provider_name) -> web.Response:
    """Refresh details from the recovery services provider.

    The operation to refresh the information from the recovery services provider.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param provider_name: Recovery services provider name.
    :type provider_name: str

    """
    return web.Response(status=200)
