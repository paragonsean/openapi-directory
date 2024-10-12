from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_mapping_input import CreateNetworkMappingInput
from openapi_server.models.network_mapping import NetworkMapping
from openapi_server.models.network_mapping_collection import NetworkMappingCollection
from openapi_server.models.update_network_mapping_input import UpdateNetworkMappingInput
from openapi_server import util


async def replication_network_mappings_create(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, network_name, network_mapping_name, input) -> web.Response:
    """Creates network mapping.

    The operation to create an ASR network mapping.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Primary fabric name.
    :type fabric_name: str
    :param network_name: Primary network name.
    :type network_name: str
    :param network_mapping_name: Network mapping name.
    :type network_mapping_name: str
    :param input: Create network mapping input.
    :type input: dict | bytes

    """
    input = CreateNetworkMappingInput.from_dict(input)
    return web.Response(status=200)


async def replication_network_mappings_delete(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, network_name, network_mapping_name) -> web.Response:
    """Delete network mapping.

    The operation to delete a network mapping.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Primary fabric name.
    :type fabric_name: str
    :param network_name: Primary network name.
    :type network_name: str
    :param network_mapping_name: ARM Resource Name for network mapping.
    :type network_mapping_name: str

    """
    return web.Response(status=200)


async def replication_network_mappings_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, network_name, network_mapping_name) -> web.Response:
    """Gets network mapping by name.

    Gets the details of an ASR network mapping

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Primary fabric name.
    :type fabric_name: str
    :param network_name: Primary network name.
    :type network_name: str
    :param network_mapping_name: Network mapping name.
    :type network_mapping_name: str

    """
    return web.Response(status=200)


async def replication_network_mappings_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id) -> web.Response:
    """Gets all the network mappings under a vault.

    Lists all ASR network mappings in the vault.

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


async def replication_network_mappings_list_by_replication_networks(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, network_name) -> web.Response:
    """Gets all the network mappings under a network.

    Lists all ASR network mappings for the specified network.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Primary fabric name.
    :type fabric_name: str
    :param network_name: Primary network name.
    :type network_name: str

    """
    return web.Response(status=200)


async def replication_network_mappings_update(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, network_name, network_mapping_name, input) -> web.Response:
    """Updates network mapping.

    The operation to update an ASR network mapping.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Primary fabric name.
    :type fabric_name: str
    :param network_name: Primary network name.
    :type network_name: str
    :param network_mapping_name: Network mapping name.
    :type network_mapping_name: str
    :param input: Update network mapping input.
    :type input: dict | bytes

    """
    input = UpdateNetworkMappingInput.from_dict(input)
    return web.Response(status=200)
