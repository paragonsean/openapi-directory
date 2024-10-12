# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.credential_results import CredentialResults
from openapi_server.models.managed_cluster import ManagedCluster
from openapi_server.models.managed_cluster_aad_profile import ManagedClusterAADProfile
from openapi_server.models.managed_cluster_access_profile import ManagedClusterAccessProfile
from openapi_server.models.managed_cluster_list_result import ManagedClusterListResult
from openapi_server.models.managed_cluster_service_principal_profile import ManagedClusterServicePrincipalProfile
from openapi_server.models.managed_cluster_upgrade_profile import ManagedClusterUpgradeProfile
from openapi_server.models.tags_object import TagsObject


pytestmark = pytest.mark.asyncio

async def test_managed_clusters_create_or_update(client):
    """Test case for managed_clusters_create_or_update

    Creates or updates a managed cluster.
    """
    parameters = {"name":"name","location":"location","id":"id","type":"type","properties":{"agentPoolProfiles":[{"osDiskSizeGB":576,"count":8,"name":"name","osType":"Linux","vnetSubnetID":"vnetSubnetID","minCount":5,"enableAutoScaling":True,"vmSize":"Standard_A1","maxPods":1,"type":"VirtualMachineScaleSets","maxCount":6},{"osDiskSizeGB":576,"count":8,"name":"name","osType":"Linux","vnetSubnetID":"vnetSubnetID","minCount":5,"enableAutoScaling":True,"vmSize":"Standard_A1","maxPods":1,"type":"VirtualMachineScaleSets","maxCount":6}],"enableRBAC":True,"fqdn":"fqdn","addonProfiles":"{}","servicePrincipalProfile":{"clientId":"clientId","secret":"secret"},"dnsPrefix":"dnsPrefix","networkProfile":{"networkPlugin":"kubenet","dockerBridgeCidr":"172.17.0.1/16","dnsServiceIP":"10.0.0.10","networkPolicy":"calico","podCidr":"10.244.0.0/16","serviceCidr":"10.0.0.0/16"},"aadProfile":{"serverAppSecret":"serverAppSecret","tenantID":"tenantID","serverAppID":"serverAppID","clientAppID":"clientAppID"},"provisioningState":"provisioningState","linuxProfile":{"adminUsername":"adminUsername","ssh":{"publicKeys":[{"keyData":"keyData"},{"keyData":"keyData"}]}},"nodeResourceGroup":"nodeResourceGroup","kubernetesVersion":"kubernetesVersion"},"tags":{"key":"tags"}}
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


pytestmark = pytest.mark.asyncio

async def test_managed_clusters_list_cluster_admin_credentials(client):
    """Test case for managed_clusters_list_cluster_admin_credentials

    Gets cluster admin credential of a managed cluster.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}/listClusterAdminCredential'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_clusters_list_cluster_user_credentials(client):
    """Test case for managed_clusters_list_cluster_user_credentials

    Gets cluster user credential of a managed cluster.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}/listClusterUserCredential'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_clusters_reset_aad_profile(client):
    """Test case for managed_clusters_reset_aad_profile

    Reset AAD Profile of a managed cluster.
    """
    parameters = {"serverAppSecret":"serverAppSecret","tenantID":"tenantID","serverAppID":"serverAppID","clientAppID":"clientAppID"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}/resetAADProfile'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_clusters_reset_service_principal_profile(client):
    """Test case for managed_clusters_reset_service_principal_profile

    Reset Service Principal Profile of a managed cluster.
    """
    parameters = {"clientId":"clientId","secret":"secret"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}/resetServicePrincipalProfile'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_clusters_update_tags(client):
    """Test case for managed_clusters_update_tags

    Updates tags on a managed cluster.
    """
    parameters = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/managedClusters/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

