from typing import List, Dict
from aiohttp import web

from openapi_server.models.storage_classification_mapping import StorageClassificationMapping
from openapi_server.models.storage_classification_mapping_collection import StorageClassificationMappingCollection
from openapi_server.models.storage_classification_mapping_input import StorageClassificationMappingInput
from openapi_server import util


async def replication_storage_classification_mappings_create(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, storage_classification_name, storage_classification_mapping_name, pairing_input) -> web.Response:
    """Create storage classification mapping.

    The operation to create a storage classification mapping.

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
    :param storage_classification_name: Storage classification name.
    :type storage_classification_name: str
    :param storage_classification_mapping_name: Storage classification mapping name.
    :type storage_classification_mapping_name: str
    :param pairing_input: Pairing input.
    :type pairing_input: dict | bytes

    """
    pairing_input = StorageClassificationMappingInput.from_dict(pairing_input)
    return web.Response(status=200)


async def replication_storage_classification_mappings_delete(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, storage_classification_name, storage_classification_mapping_name) -> web.Response:
    """Delete a storage classification mapping.

    The operation to delete a storage classification mapping.

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
    :param storage_classification_name: Storage classification name.
    :type storage_classification_name: str
    :param storage_classification_mapping_name: Storage classification mapping name.
    :type storage_classification_mapping_name: str

    """
    return web.Response(status=200)


async def replication_storage_classification_mappings_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, storage_classification_name, storage_classification_mapping_name) -> web.Response:
    """Gets the details of a storage classification mapping.

    Gets the details of the specified storage classification mapping.

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
    :param storage_classification_name: Storage classification name.
    :type storage_classification_name: str
    :param storage_classification_mapping_name: Storage classification mapping name.
    :type storage_classification_mapping_name: str

    """
    return web.Response(status=200)


async def replication_storage_classification_mappings_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id) -> web.Response:
    """Gets the list of storage classification mappings objects under a vault.

    Lists the storage classification mappings in the vault.

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


async def replication_storage_classification_mappings_list_by_replication_storage_classifications(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, storage_classification_name) -> web.Response:
    """Gets the list of storage classification mappings objects under a storage.

    Lists the storage classification mappings for the fabric.

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
    :param storage_classification_name: Storage classification name.
    :type storage_classification_name: str

    """
    return web.Response(status=200)
