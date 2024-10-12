# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.volume_resource_description import VolumeResourceDescription
from openapi_server.models.volume_resource_description_list import VolumeResourceDescriptionList


pytestmark = pytest.mark.asyncio

async def test_volume_create(client):
    """Test case for volume_create

    Creates or updates a volume resource.
    """
    volume_resource_description = {"properties":{"azureFileParameters":{"accountName":"accountName","shareName":"shareName","accountKey":"accountKey"},"provider":"SFAzureFile","description":"description","provisioningState":"provisioningState"}}
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/volumes/{volume_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', volume_name='volume_name_example'),
        headers=headers,
        json=volume_resource_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volume_delete(client):
    """Test case for volume_delete

    Deletes the volume resource.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/volumes/{volume_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', volume_name='volume_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volume_get(client):
    """Test case for volume_get

    Gets the volume resource.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/volumes/{volume_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', volume_name='volume_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volume_list_by_resource_group(client):
    """Test case for volume_list_by_resource_group

    Gets all the volume resources in a given resource group.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/volumes'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_volume_list_by_subscription(client):
    """Test case for volume_list_by_subscription

    Gets all the volume resources in a given subscription.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ServiceFabricMesh/volumes'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

