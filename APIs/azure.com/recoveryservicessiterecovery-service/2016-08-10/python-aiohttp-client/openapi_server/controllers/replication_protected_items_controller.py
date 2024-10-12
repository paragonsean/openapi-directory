from typing import List, Dict
from aiohttp import web

from openapi_server.models.apply_recovery_point_input import ApplyRecoveryPointInput
from openapi_server.models.disable_protection_input import DisableProtectionInput
from openapi_server.models.enable_protection_input import EnableProtectionInput
from openapi_server.models.planned_failover_input import PlannedFailoverInput
from openapi_server.models.replication_protected_item import ReplicationProtectedItem
from openapi_server.models.replication_protected_item_collection import ReplicationProtectedItemCollection
from openapi_server.models.reverse_replication_input import ReverseReplicationInput
from openapi_server.models.test_failover_cleanup_input import TestFailoverCleanupInput
from openapi_server.models.test_failover_input import TestFailoverInput
from openapi_server.models.unplanned_failover_input import UnplannedFailoverInput
from openapi_server.models.update_mobility_service_request import UpdateMobilityServiceRequest
from openapi_server.models.update_replication_protected_item_input import UpdateReplicationProtectedItemInput
from openapi_server import util


async def replication_protected_items_apply_recovery_point(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name, apply_recovery_point_input) -> web.Response:
    """Change or apply recovery point.

    The operation to change the recovery point of a failed over replication protected item.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: The ARM fabric name.
    :type fabric_name: str
    :param protection_container_name: The protection container name.
    :type protection_container_name: str
    :param replicated_protected_item_name: The replicated protected item&#39;s name.
    :type replicated_protected_item_name: str
    :param apply_recovery_point_input: The ApplyRecoveryPointInput.
    :type apply_recovery_point_input: dict | bytes

    """
    apply_recovery_point_input = ApplyRecoveryPointInput.from_dict(apply_recovery_point_input)
    return web.Response(status=200)


async def replication_protected_items_create(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name, input) -> web.Response:
    """Enables protection.

    The operation to create an ASR replication protected item (Enable replication).

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Name of the fabric.
    :type fabric_name: str
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param replicated_protected_item_name: A name for the replication protected item.
    :type replicated_protected_item_name: str
    :param input: Enable Protection Input.
    :type input: dict | bytes

    """
    input = EnableProtectionInput.from_dict(input)
    return web.Response(status=200)


async def replication_protected_items_delete(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name, disable_protection_input) -> web.Response:
    """Disables protection.

    The operation to disable replication on a replication protected item. This will also remove the item.

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
    :param replicated_protected_item_name: Replication protected item name.
    :type replicated_protected_item_name: str
    :param disable_protection_input: Disable protection input.
    :type disable_protection_input: dict | bytes

    """
    disable_protection_input = DisableProtectionInput.from_dict(disable_protection_input)
    return web.Response(status=200)


async def replication_protected_items_failover_commit(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name) -> web.Response:
    """Execute commit failover

    Operation to commit the failover of the replication protected item.

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
    :param replicated_protected_item_name: Replication protected item name.
    :type replicated_protected_item_name: str

    """
    return web.Response(status=200)


async def replication_protected_items_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name) -> web.Response:
    """Gets the details of a Replication protected item.

    Gets the details of an ASR replication protected item.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric unique name.
    :type fabric_name: str
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param replicated_protected_item_name: Replication protected item name.
    :type replicated_protected_item_name: str

    """
    return web.Response(status=200)


async def replication_protected_items_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, skip_token=None, filter=None) -> web.Response:
    """Gets the list of replication protected items.

    Gets the list of ASR replication protected items in the vault.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param skip_token: The pagination token. Possible values: \&quot;FabricId\&quot; or \&quot;FabricId_CloudId\&quot; or null
    :type skip_token: str
    :param filter: OData filter options.
    :type filter: str

    """
    return web.Response(status=200)


async def replication_protected_items_list_by_replication_protection_containers(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name) -> web.Response:
    """Gets the list of Replication protected items.

    Gets the list of ASR replication protected items in the protection container.

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


async def replication_protected_items_planned_failover(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name, failover_input) -> web.Response:
    """Execute planned failover

    Operation to initiate a planned failover of the replication protected item.

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
    :param replicated_protected_item_name: Replication protected item name.
    :type replicated_protected_item_name: str
    :param failover_input: Disable protection input.
    :type failover_input: dict | bytes

    """
    failover_input = PlannedFailoverInput.from_dict(failover_input)
    return web.Response(status=200)


async def replication_protected_items_purge(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name) -> web.Response:
    """Purges protection.

    The operation to delete or purge a replication protected item. This operation will force delete the replication protected item. Use the remove operation on replication protected item to perform a clean disable replication for the item.

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
    :param replicated_protected_item_name: Replication protected item name.
    :type replicated_protected_item_name: str

    """
    return web.Response(status=200)


async def replication_protected_items_repair_replication(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name) -> web.Response:
    """Resynchronize or repair replication.

    The operation to start resynchronize/repair replication for a replication protected item requiring resynchronization.

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
    :param protection_container_name: The name of the container.
    :type protection_container_name: str
    :param replicated_protected_item_name: The name of the replication protected item.
    :type replicated_protected_item_name: str

    """
    return web.Response(status=200)


async def replication_protected_items_reprotect(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name, rr_input) -> web.Response:
    """Execute Reverse Replication\\Reprotect

    Operation to reprotect or reverse replicate a failed over replication protected item.

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
    :param replicated_protected_item_name: Replication protected item name.
    :type replicated_protected_item_name: str
    :param rr_input: Disable protection input.
    :type rr_input: dict | bytes

    """
    rr_input = ReverseReplicationInput.from_dict(rr_input)
    return web.Response(status=200)


async def replication_protected_items_test_failover(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name, failover_input) -> web.Response:
    """Execute test failover

    Operation to perform a test failover of the replication protected item.

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
    :param replicated_protected_item_name: Replication protected item name.
    :type replicated_protected_item_name: str
    :param failover_input: Test failover input.
    :type failover_input: dict | bytes

    """
    failover_input = TestFailoverInput.from_dict(failover_input)
    return web.Response(status=200)


async def replication_protected_items_test_failover_cleanup(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name, cleanup_input) -> web.Response:
    """Execute test failover cleanup.

    Operation to clean up the test failover of a replication protected item.

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
    :param replicated_protected_item_name: Replication protected item name.
    :type replicated_protected_item_name: str
    :param cleanup_input: Test failover cleanup input.
    :type cleanup_input: dict | bytes

    """
    cleanup_input = TestFailoverCleanupInput.from_dict(cleanup_input)
    return web.Response(status=200)


async def replication_protected_items_unplanned_failover(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name, failover_input) -> web.Response:
    """Execute unplanned failover

    Operation to initiate a failover of the replication protected item.

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
    :param replicated_protected_item_name: Replication protected item name.
    :type replicated_protected_item_name: str
    :param failover_input: Disable protection input.
    :type failover_input: dict | bytes

    """
    failover_input = UnplannedFailoverInput.from_dict(failover_input)
    return web.Response(status=200)


async def replication_protected_items_update(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name, update_protection_input) -> web.Response:
    """Updates protection.

    The operation to update the recovery settings of an ASR replication protected item.

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
    :param replicated_protected_item_name: Replication protected item name.
    :type replicated_protected_item_name: str
    :param update_protection_input: Update protection input.
    :type update_protection_input: dict | bytes

    """
    update_protection_input = UpdateReplicationProtectedItemInput.from_dict(update_protection_input)
    return web.Response(status=200)


async def replication_protected_items_update_mobility_service(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replication_protected_item_name, update_mobility_service_request) -> web.Response:
    """Update the mobility service on a protected item.

    The operation to update(push update) the installed mobility service software on a replication protected item to the latest available version.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: The name of the fabric containing the protected item.
    :type fabric_name: str
    :param protection_container_name: The name of the container containing the protected item.
    :type protection_container_name: str
    :param replication_protected_item_name: The name of the protected item on which the agent is to be updated.
    :type replication_protected_item_name: str
    :param update_mobility_service_request: Request to update the mobility service on the protected item.
    :type update_mobility_service_request: dict | bytes

    """
    update_mobility_service_request = UpdateMobilityServiceRequest.from_dict(update_mobility_service_request)
    return web.Response(status=200)
