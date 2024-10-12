from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_protection_container_mapping_input import CreateProtectionContainerMappingInput
from openapi_server.models.protection_container_mapping import ProtectionContainerMapping
from openapi_server.models.protection_container_mapping_collection import ProtectionContainerMappingCollection
from openapi_server.models.remove_protection_container_mapping_input import RemoveProtectionContainerMappingInput
from openapi_server import util


async def replication_protection_container_mappings_create(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, mapping_name, creation_input) -> web.Response:
    """Create protection container mapping.

    The operation to create a protection container mapping.

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
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param mapping_name: Protection container mapping name.
    :type mapping_name: str
    :param creation_input: Mapping creation input.
    :type creation_input: dict | bytes

    """
    creation_input = CreateProtectionContainerMappingInput.from_dict(creation_input)
    return web.Response(status=200)


async def replication_protection_container_mappings_delete(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, mapping_name, removal_input) -> web.Response:
    """Remove protection container mapping.

    The operation to delete or remove a protection container mapping.

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
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param mapping_name: Protection container mapping name.
    :type mapping_name: str
    :param removal_input: Removal input.
    :type removal_input: dict | bytes

    """
    removal_input = RemoveProtectionContainerMappingInput.from_dict(removal_input)
    return web.Response(status=200)


async def replication_protection_container_mappings_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, mapping_name) -> web.Response:
    """Gets a protection container mapping/

    Gets the details of a protection container mapping.

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
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param mapping_name: Protection Container mapping name.
    :type mapping_name: str

    """
    return web.Response(status=200)


async def replication_protection_container_mappings_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id) -> web.Response:
    """Gets the list of all protection container mappings in a vault.

    Lists the protection container mappings in the vault.

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


async def replication_protection_container_mappings_list_by_replication_protection_containers(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name) -> web.Response:
    """Gets the list of protection container mappings for a protection container.

    Lists the protection container mappings for a protection container.

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
    :param protection_container_name: Protection container name.
    :type protection_container_name: str

    """
    return web.Response(status=200)


async def replication_protection_container_mappings_purge(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, mapping_name) -> web.Response:
    """Purge protection container mapping.

    The operation to purge(force delete) a protection container mapping

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
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param mapping_name: Protection container mapping name.
    :type mapping_name: str

    """
    return web.Response(status=200)
