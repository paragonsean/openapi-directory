# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.agent_pool import AgentPool
from openapi_server.models.agent_pool_available_versions import AgentPoolAvailableVersions
from openapi_server.models.agent_pool_list_result import AgentPoolListResult
from openapi_server.models.agent_pool_upgrade_profile import AgentPoolUpgradeProfile
from openapi_server.models.cloud_error import CloudError


pytestmark = pytest.mark.asyncio

async def test_agent_pools_create_or_update(client):
    """Test case for agent_pools_create_or_update

    Creates or updates an agent pool.
    """
    parameters = {"name":"name","id":"id","type":"type","properties":{"osDiskSizeGB":576,"count":0,"vnetSubnetID":"vnetSubnetID","availabilityZones":["availabilityZones","availabilityZones"],"enableAutoScaling":True,"orchestratorVersion":"orchestratorVersion","provisioningState":"provisioningState","type":"VirtualMachineScaleSets","maxCount":6,"enableNodePublicIP":True,"scaleSetEvictionPolicy":"Delete","nodeTaints":["nodeTaints","nodeTaints"],"scaleSetPriority":"Regular","osType":"Linux","minCount":5,"vmSize":"Standard_A1","maxPods":1}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}/agentPools/{agent_pool_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', agent_pool_name='agent_pool_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_agent_pools_delete(client):
    """Test case for agent_pools_delete

    Deletes an agent pool.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}/agentPools/{agent_pool_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', agent_pool_name='agent_pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_agent_pools_get(client):
    """Test case for agent_pools_get

    Gets the agent pool.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}/agentPools/{agent_pool_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', agent_pool_name='agent_pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_agent_pools_get_available_agent_pool_versions(client):
    """Test case for agent_pools_get_available_agent_pool_versions

    Gets a list of supported versions for the specified agent pool.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}/availableAgentPoolVersions'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_agent_pools_get_upgrade_profile(client):
    """Test case for agent_pools_get_upgrade_profile

    Gets upgrade profile for an agent pool.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}/agentPools/{agent_pool_name}/upgradeProfiles/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', agent_pool_name='agent_pool_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_agent_pools_list(client):
    """Test case for agent_pools_list

    Gets a list of agent pools in the specified managed cluster.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}/agentPools'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

