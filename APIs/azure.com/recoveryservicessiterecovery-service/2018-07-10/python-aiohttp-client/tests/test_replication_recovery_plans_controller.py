# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_recovery_plan_input import CreateRecoveryPlanInput
from openapi_server.models.recovery_plan import RecoveryPlan
from openapi_server.models.recovery_plan_collection import RecoveryPlanCollection
from openapi_server.models.recovery_plan_planned_failover_input import RecoveryPlanPlannedFailoverInput
from openapi_server.models.recovery_plan_test_failover_cleanup_input import RecoveryPlanTestFailoverCleanupInput
from openapi_server.models.recovery_plan_test_failover_input import RecoveryPlanTestFailoverInput
from openapi_server.models.recovery_plan_unplanned_failover_input import RecoveryPlanUnplannedFailoverInput
from openapi_server.models.update_recovery_plan_input import UpdateRecoveryPlanInput


pytestmark = pytest.mark.asyncio

async def test_replication_recovery_plans_create(client):
    """Test case for replication_recovery_plans_create

    Creates a recovery plan with the given details.
    """
    input = {"properties":{"recoveryFabricId":"recoveryFabricId","failoverDeploymentModel":"NotApplicable","groups":[{"groupType":"Shutdown","startGroupActions":[{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"},{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"}],"replicationProtectedItems":[{"virtualMachineId":"virtualMachineId","id":"id"},{"virtualMachineId":"virtualMachineId","id":"id"}],"endGroupActions":[{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"},{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"}]},{"groupType":"Shutdown","startGroupActions":[{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"},{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"}],"replicationProtectedItems":[{"virtualMachineId":"virtualMachineId","id":"id"},{"virtualMachineId":"virtualMachineId","id":"id"}],"endGroupActions":[{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"},{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"}]}],"primaryFabricId":"primaryFabricId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationRecoveryPlans/{recovery_plan_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', recovery_plan_name='recovery_plan_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_recovery_plans_delete(client):
    """Test case for replication_recovery_plans_delete

    Deletes the specified recovery plan.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationRecoveryPlans/{recovery_plan_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', recovery_plan_name='recovery_plan_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_recovery_plans_failover_commit(client):
    """Test case for replication_recovery_plans_failover_commit

    Execute commit failover of the recovery plan.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationRecoveryPlans/{recovery_plan_name}/failoverCommit'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', recovery_plan_name='recovery_plan_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_recovery_plans_get(client):
    """Test case for replication_recovery_plans_get

    Gets the requested recovery plan.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationRecoveryPlans/{recovery_plan_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', recovery_plan_name='recovery_plan_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_recovery_plans_list(client):
    """Test case for replication_recovery_plans_list

    Gets the list of recovery plans.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationRecoveryPlans'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_recovery_plans_planned_failover(client):
    """Test case for replication_recovery_plans_planned_failover

    Execute planned failover of the recovery plan.
    """
    input = {"properties":{"providerSpecificDetails":[{"instanceType":"instanceType"},{"instanceType":"instanceType"}],"failoverDirection":"PrimaryToRecovery"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationRecoveryPlans/{recovery_plan_name}/plannedFailover'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', recovery_plan_name='recovery_plan_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_recovery_plans_reprotect(client):
    """Test case for replication_recovery_plans_reprotect

    Execute reprotect of the recovery plan.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationRecoveryPlans/{recovery_plan_name}/reProtect'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', recovery_plan_name='recovery_plan_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_recovery_plans_test_failover(client):
    """Test case for replication_recovery_plans_test_failover

    Execute test failover of the recovery plan.
    """
    input = {"properties":{"skipTestFailoverCleanup":"skipTestFailoverCleanup","providerSpecificDetails":[{"instanceType":"instanceType"},{"instanceType":"instanceType"}],"networkId":"networkId","failoverDirection":"PrimaryToRecovery","networkType":"networkType"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationRecoveryPlans/{recovery_plan_name}/testFailover'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', recovery_plan_name='recovery_plan_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_recovery_plans_test_failover_cleanup(client):
    """Test case for replication_recovery_plans_test_failover_cleanup

    Execute test failover cleanup of the recovery plan.
    """
    input = {"properties":{"comments":"comments"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationRecoveryPlans/{recovery_plan_name}/testFailoverCleanup'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', recovery_plan_name='recovery_plan_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_recovery_plans_unplanned_failover(client):
    """Test case for replication_recovery_plans_unplanned_failover

    Execute unplanned failover of the recovery plan.
    """
    input = {"properties":{"sourceSiteOperations":"Required","providerSpecificDetails":[{"instanceType":"instanceType"},{"instanceType":"instanceType"}],"failoverDirection":"PrimaryToRecovery"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationRecoveryPlans/{recovery_plan_name}/unplannedFailover'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', recovery_plan_name='recovery_plan_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_replication_recovery_plans_update(client):
    """Test case for replication_recovery_plans_update

    Updates the given recovery plan.
    """
    input = {"properties":{"groups":[{"groupType":"Shutdown","startGroupActions":[{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"},{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"}],"replicationProtectedItems":[{"virtualMachineId":"virtualMachineId","id":"id"},{"virtualMachineId":"virtualMachineId","id":"id"}],"endGroupActions":[{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"},{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"}]},{"groupType":"Shutdown","startGroupActions":[{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"},{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"}],"replicationProtectedItems":[{"virtualMachineId":"virtualMachineId","id":"id"},{"virtualMachineId":"virtualMachineId","id":"id"}],"endGroupActions":[{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"},{"failoverDirections":["PrimaryToRecovery","PrimaryToRecovery"],"customDetails":{"instanceType":"instanceType"},"failoverTypes":["ReverseReplicate","ReverseReplicate"],"actionName":"actionName"}]}]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/Subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.RecoveryServices/vaults/{resource_name}/replicationRecoveryPlans/{recovery_plan_name}'.format(resource_name='resource_name_example', resource_group_name='resource_group_name_example', subscription_id='subscription_id_example', recovery_plan_name='recovery_plan_name_example'),
        headers=headers,
        json=input,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

