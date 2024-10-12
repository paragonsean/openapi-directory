from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_protection_container_input import CreateProtectionContainerInput
from openapi_server.models.discover_protectable_item_request import DiscoverProtectableItemRequest
from openapi_server.models.protection_container import ProtectionContainer
from openapi_server.models.protection_container_collection import ProtectionContainerCollection
from openapi_server.models.switch_protection_input import SwitchProtectionInput
from openapi_server import util


async def replication_protection_containers_create(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, creation_input) -> web.Response:
    """Create a protection container.

    Operation to create a protection container.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Unique fabric ARM name.
    :type fabric_name: str
    :param protection_container_name: Unique protection container ARM name.
    :type protection_container_name: str
    :param creation_input: Creation input.
    :type creation_input: dict | bytes

    """
    creation_input = CreateProtectionContainerInput.from_dict(creation_input)
    return web.Response(status=200)


async def replication_protection_containers_delete(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name) -> web.Response:
    """Removes a protection container.

    Operation to remove a protection container.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Unique fabric ARM name.
    :type fabric_name: str
    :param protection_container_name: Unique protection container ARM name.
    :type protection_container_name: str

    """
    return web.Response(status=200)


async def replication_protection_containers_discover_protectable_item(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, discover_protectable_item_request) -> web.Response:
    """Adds a protectable item to the replication protection container.

    The operation to a add a protectable item to a protection container(Add physical server.)

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: The name of the fabric.
    :type fabric_name: str
    :param protection_container_name: The name of the protection container.
    :type protection_container_name: str
    :param discover_protectable_item_request: The request object to add a protectable item.
    :type discover_protectable_item_request: dict | bytes

    """
    discover_protectable_item_request = DiscoverProtectableItemRequest.from_dict(discover_protectable_item_request)
    return web.Response(status=200)


async def replication_protection_containers_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name) -> web.Response:
    """Gets the protection container details.

    Gets the details of a protection container.

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


async def replication_protection_containers_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id) -> web.Response:
    """Gets the list of all protection containers in a vault.

    Lists the protection containers in a vault.

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


async def replication_protection_containers_list_by_replication_fabrics(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name) -> web.Response:
    """Gets the list of protection container for a fabric.

    Lists the protection containers in the specified fabric.

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

    """
    return web.Response(status=200)


async def replication_protection_containers_switch_protection(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, switch_input) -> web.Response:
    """Switches protection from one container to another or one replication provider to another.

    Operation to switch protection from one container to another or one replication provider to another.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Unique fabric name.
    :type fabric_name: str
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param switch_input: Switch protection input.
    :type switch_input: dict | bytes

    """
    switch_input = SwitchProtectionInput.from_dict(switch_input)
    return web.Response(status=200)
