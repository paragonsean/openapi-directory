# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_apply_recovery_point(client):
    """Test case for replication_protected_items_apply_recovery_point

    Change or apply recovery point.
    """
    apply_recovery_point_input = {"properties":{"providerSpecificDetails":{"instanceType":"instanceType"},"recoveryPointId":"recoveryPointId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}/applyRecoveryPoint'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        json=apply_recovery_point_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_create(client):
    """Test case for replication_protected_items_create

    Enables protection.
    """
    input = {"properties":{"policyId":"policyId","providerSpecificDetails":{"instanceType":"instanceType"},"protectableItemId":"protectableItemId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_delete(client):
    """Test case for replication_protected_items_delete

    Disables protection.
    """
    disable_protection_input = {"properties":{"disableProtectionReason":"NotSpecified","replicationProviderInput":{"instanceType":"instanceType"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}/remove'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        json=disable_protection_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_failover_commit(client):
    """Test case for replication_protected_items_failover_commit

    Execute commit failover
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}/failoverCommit'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_get(client):
    """Test case for replication_protected_items_get

    Gets the details of a Replication protected item.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_list(client):
    """Test case for replication_protected_items_list

    Gets the list of replication protected items.
    """
    params = [('api-version', 'api_version_example'),
                    ('skipToken', 'skip_token_example'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationProtectedItems'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_list_by_replication_protection_containers(client):
    """Test case for replication_protected_items_list_by_replication_protection_containers

    Gets the list of Replication protected items.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_planned_failover(client):
    """Test case for replication_protected_items_planned_failover

    Execute planned failover
    """
    failover_input = {"properties":{"providerSpecificDetails":{"instanceType":"instanceType"},"failoverDirection":"failoverDirection"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}/plannedFailover'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        json=failover_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_purge(client):
    """Test case for replication_protected_items_purge

    Purges protection.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_repair_replication(client):
    """Test case for replication_protected_items_repair_replication

    Resynchronize or repair replication.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}/repairReplication'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_reprotect(client):
    """Test case for replication_protected_items_reprotect

    Execute Reverse Replication\\Reprotect
    """
    rr_input = {"properties":{"providerSpecificDetails":{"instanceType":"instanceType"},"failoverDirection":"failoverDirection"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}/reProtect'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        json=rr_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_test_failover(client):
    """Test case for replication_protected_items_test_failover

    Execute test failover
    """
    failover_input = {"properties":{"skipTestFailoverCleanup":"skipTestFailoverCleanup","providerSpecificDetails":{"instanceType":"instanceType"},"networkId":"networkId","failoverDirection":"failoverDirection","networkType":"networkType"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}/testFailover'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        json=failover_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_test_failover_cleanup(client):
    """Test case for replication_protected_items_test_failover_cleanup

    Execute test failover cleanup.
    """
    cleanup_input = {"properties":{"comments":"comments"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}/testFailoverCleanup'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        json=cleanup_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_unplanned_failover(client):
    """Test case for replication_protected_items_unplanned_failover

    Execute unplanned failover
    """
    failover_input = {"properties":{"sourceSiteOperations":"sourceSiteOperations","providerSpecificDetails":{"instanceType":"instanceType"},"failoverDirection":"failoverDirection"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}/unplannedFailover'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        json=failover_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_update(client):
    """Test case for replication_protected_items_update

    Updates protection.
    """
    update_protection_input = {"properties":{"licenseType":"NotSpecified","vmNics":[{"enableAcceleratedNetworkingOnRecovery":True,"selectionType":"selectionType","nicId":"nicId","replicaNicStaticIPAddress":"replicaNicStaticIPAddress","recoveryVMSubnetName":"recoveryVMSubnetName"},{"enableAcceleratedNetworkingOnRecovery":True,"selectionType":"selectionType","nicId":"nicId","replicaNicStaticIPAddress":"replicaNicStaticIPAddress","recoveryVMSubnetName":"recoveryVMSubnetName"}],"providerSpecificDetails":{"instanceType":"instanceType"},"recoveryAvailabilitySetId":"recoveryAvailabilitySetId","enableRdpOnTargetOption":"enableRdpOnTargetOption","selectedSourceNicId":"selectedSourceNicId","recoveryAzureVMName":"recoveryAzureVMName","recoveryAzureVMSize":"recoveryAzureVMSize","selectedRecoveryAzureNetworkId":"selectedRecoveryAzureNetworkId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replicated_protected_item_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replicated_protected_item_name='replicated_protected_item_name_example'),
        headers=headers,
        json=update_protection_input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_protected_items_update_mobility_service(client):
    """Test case for replication_protected_items_update_mobility_service

    Update the mobility service on a protected item.
    """
    update_mobility_service_request = {"properties":{"runAsAccountId":"runAsAccountId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationFabrics/{fabric_name}/replicationProtectionContainers/{protection_container_name}/replicationProtectedItems/{replication_protected_item_name}/updateMobilityService'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', fabric_name='fabric_name_example', protection_container_name='protection_container_name_example', replication_protected_item_name='replication_protected_item_name_example'),
        headers=headers,
        json=update_mobility_service_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

