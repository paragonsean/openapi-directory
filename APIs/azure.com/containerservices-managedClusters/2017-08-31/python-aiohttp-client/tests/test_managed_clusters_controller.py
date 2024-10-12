# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.managed_cluster import ManagedCluster
from openapi_server.models.managed_cluster_access_profile import ManagedClusterAccessProfile
from openapi_server.models.managed_cluster_list_result import ManagedClusterListResult
from openapi_server.models.managed_cluster_upgrade_profile import ManagedClusterUpgradeProfile


pytestmark = pytest.mark.asyncio

async def test_managed_clusters_create_or_update(client):
    """Test case for managed_clusters_create_or_update

    Creates or updates a managed cluster.
    """
    parameters = {"name":"name","location":"location","id":"id","type":"type","properties":{"agentPoolProfiles":[{"fqdn":"fqdn","osDiskSizeGB":616,"storageProfile":"StorageAccount","count":8,"name":"name","osType":"Linux","dnsPrefix":"dnsPrefix","vnetSubnetID":"vnetSubnetID","vmSize":"Standard_A1","ports":[9607,9607]},{"fqdn":"fqdn","osDiskSizeGB":616,"storageProfile":"StorageAccount","count":8,"name":"name","osType":"Linux","dnsPrefix":"dnsPrefix","vnetSubnetID":"vnetSubnetID","vmSize":"Standard_A1","ports":[9607,9607]}],"fqdn":"fqdn","servicePrincipalProfile":{"clientId":"clientId","keyVaultSecretRef":{"secretName":"secretName","vaultID":"vaultID","version":"version"},"secret":"secret"},"dnsPrefix":"dnsPrefix","provisioningState":"provisioningState","linuxProfile":{"adminUsername":"adminUsername","ssh":{"publicKeys":[{"keyData":"keyData"},{"keyData":"keyData"}]}},"kubernetesVersion":"kubernetesVersion"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_clusters_delete(client):
    """Test case for managed_clusters_delete

    Deletes a managed cluster.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_clusters_get(client):
    """Test case for managed_clusters_get

    Gets a managed cluster.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_clusters_get_access_profile(client):
    """Test case for managed_clusters_get_access_profile

    Gets an access profile of a managed cluster.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}/accessProfiles/{role_name}/listCredential'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', role_name='role_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_clusters_get_access_profiles(client):
    """Test case for managed_clusters_get_access_profiles

    Gets access profile of a managed cluster.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}/accessProfiles/{role_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', role_name='role_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_clusters_get_upgrade_profile(client):
    """Test case for managed_clusters_get_upgrade_profile

    Gets upgrade profile for a managed cluster.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}/upgradeProfiles/default'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_clusters_list(client):
    """Test case for managed_clusters_list

    Gets a list of managed clusters in the specified subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ContainerService/managedClusters'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_clusters_list_by_resource_group(client):
    """Test case for managed_clusters_list_by_resource_group

    Lists managed clusters in the specified subscription and resource group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

