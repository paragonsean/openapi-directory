# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.csrp_error import CSRPError
from openapi_server.models.dedicated_cloud_node import DedicatedCloudNode
from openapi_server.models.dedicated_cloud_node_list_response import DedicatedCloudNodeListResponse
from openapi_server.models.patch_payload import PatchPayload


pytestmark = pytest.mark.asyncio

async def test_dedicated_cloud_nodes_create_or_update(client):
    """Test case for dedicated_cloud_nodes_create_or_update

    Implements dedicated cloud node PUT method
    """
    dedicated_cloud_node_request = {"name":"name","location":"location","id":"id","sku":{"tier":"tier","name":"name","description":"description","family":"family","capacity":"capacity"},"type":"type","properties":{"availabilityZoneId":"availabilityZoneId","created":"{}","purchaseId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","skuDescription":{"name":"name","id":"id"},"privateCloudName":"privateCloudName","provisioningState":"provisioningState","vmwareClusterName":"vmwareClusterName","placementGroupName":"placementGroupName","availabilityZoneName":"availabilityZoneName","nodesCount":0,"placementGroupId":"placementGroupId","privateCloudId":"privateCloudId","cloudRackName":"cloudRackName","status":"unused"},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'referer': 'referer_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{dedicated_cloud_node_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', dedicated_cloud_node_name='dedicated_cloud_node_name_example'),
        headers=headers,
        json=dedicated_cloud_node_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_cloud_nodes_delete(client):
    """Test case for dedicated_cloud_nodes_delete

    Implements dedicated cloud node DELETE method
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{dedicated_cloud_node_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', dedicated_cloud_node_name='dedicated_cloud_node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_cloud_nodes_get(client):
    """Test case for dedicated_cloud_nodes_get

    Implements dedicated cloud node GET method
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{dedicated_cloud_node_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', dedicated_cloud_node_name='dedicated_cloud_node_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_cloud_nodes_list_by_resource_group(client):
    """Test case for dedicated_cloud_nodes_list_by_resource_group

    Implements list of dedicated cloud nodes within RG method
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_cloud_nodes_list_by_subscription(client):
    """Test case for dedicated_cloud_nodes_list_by_subscription

    Implements list of dedicated cloud nodes within subscription method
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skipToken', 'skip_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_dedicated_cloud_nodes_update(client):
    """Test case for dedicated_cloud_nodes_update

    Implements dedicated cloud node PATCH method
    """
    dedicated_cloud_node_request = {"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.VMwareCloudSimple/dedicatedCloudNodes/{dedicated_cloud_node_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', dedicated_cloud_node_name='dedicated_cloud_node_name_example'),
        headers=headers,
        json=dedicated_cloud_node_request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

