# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.open_shift_managed_cluster import OpenShiftManagedCluster
from openapi_server.models.open_shift_managed_cluster_list_result import OpenShiftManagedClusterListResult
from openapi_server.models.tags_object import TagsObject


pytestmark = pytest.mark.asyncio

async def test_open_shift_managed_clusters_create_or_update(client):
    """Test case for open_shift_managed_clusters_create_or_update

    Creates or updates an OpenShift managed cluster.
    """
    parameters = {"name":"name","location":"location","id":"id","type":"type","plan":{"product":"product","name":"name","promotionCode":"promotionCode","publisher":"publisher"},"properties":{"agentPoolProfiles":[{"subnetCidr":"10.0.0.0/24","role":"compute","count":0,"name":"name","osType":"Linux","vmSize":"Standard_D2s_v3"},{"subnetCidr":"10.0.0.0/24","role":"compute","count":0,"name":"name","osType":"Linux","vmSize":"Standard_D2s_v3"}],"publicHostname":"publicHostname","fqdn":"fqdn","openShiftVersion":"openShiftVersion","routerProfiles":[{"publicSubdomain":"publicSubdomain","fqdn":"fqdn","name":"name"},{"publicSubdomain":"publicSubdomain","fqdn":"fqdn","name":"name"}],"networkProfile":{"peerVnetId":"peerVnetId","vnetCidr":"10.0.0.0/8"},"provisioningState":"provisioningState","masterPoolProfile":{"subnetCidr":"subnetCidr","count":6,"name":"name"},"authProfile":{"identityProviders":[{"provider":{"kind":"kind"},"name":"name"},{"provider":{"kind":"kind"},"name":"name"}]}},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/openShiftManagedClusters/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_open_shift_managed_clusters_delete(client):
    """Test case for open_shift_managed_clusters_delete

    Deletes an OpenShift managed cluster.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/openShiftManagedClusters/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_open_shift_managed_clusters_get(client):
    """Test case for open_shift_managed_clusters_get

    Gets a OpenShift managed cluster.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/openShiftManagedClusters/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_open_shift_managed_clusters_list(client):
    """Test case for open_shift_managed_clusters_list

    Gets a list of OpenShift managed clusters in the specified subscription.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ContainerService/openShiftManagedClusters'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_open_shift_managed_clusters_list_by_resource_group(client):
    """Test case for open_shift_managed_clusters_list_by_resource_group

    Lists OpenShift managed clusters in the specified subscription and resource group.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/openShiftManagedClusters'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_open_shift_managed_clusters_update_tags(client):
    """Test case for open_shift_managed_clusters_update_tags

    Updates tags on an OpenShift managed cluster.
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ContainerService/openShiftManagedClusters/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

